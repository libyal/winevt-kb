#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script to extract the strings from Event Log message resource files."""

import argparse
import logging
import os
import re
import sys
import yaml

from acstore import sqlite_store

from dfvfs.helpers import command_line as dfvfs_command_line
from dfvfs.helpers import volume_scanner as dfvfs_volume_scanner
from dfvfs.lib import errors as dfvfs_errors

import pyfwevt
import pywrc

from winevtrc import definitions
from winevtrc import extractor
from winevtrc import resources
from winevtrc import storage  # pylint: disable=unused-import


class SQLite3OutputWriter(object):
  """SQLite3 output writer."""

  EVENT_PROVIDERS_DATABASE_FILENAME = 'winevt-kb.db'

  def __init__(self, databases_path):
    """Initializes an output writer object.

    Args:
      databases_path (str): path to the database files.
    """
    super(SQLite3OutputWriter, self).__init__()
    self._databases_path = databases_path
    self._database_writer = None

  def _GetDatabaseFilename(self, resource_file):
    """Determines the filename of the intermediate message resource database.

    Args:
      resource_file (WindowsResourceFile): message or template resource file.
    """
    filename = resource_file.windows_path.rsplit('\\', maxsplit=1)[-1]
    filename = filename.lower()
    return re.sub(r'\.mui', '', f'{filename:s}.db')

  def _WriteMessageIdentifierMappings(
        self, event_log_provider, template_resource_file, database_writer):
    """Writes the message identifier mappings.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
      template_resource_file (WindowsResourceFile): template resource file.
      database_writer (acstore.SQLiteAttributeContainerStore): message resource
          file attribute container store.
    """
    wrc_resource = template_resource_file.GetWEVTTemplateResource()
    if not wrc_resource:
      return

    if wrc_resource.number_of_items != 1:
      logging.warning((
          f'More than 1 WEVT_TEMPLATE resource item in resource file: '
          f'{template_resource_file.windows_path:s}.'))

    wrc_resource_item = wrc_resource.items[0]
    for wrc_resource_sub_item in wrc_resource_item.sub_items:
      resource_data = wrc_resource_sub_item.read()

      wevt_manifest = pyfwevt.manifest()
      wevt_manifest.copy_from_byte_stream(resource_data)

      for wevt_provider in iter(wevt_manifest.providers):
        # Ignore unrelated providers in the template resource file.
        if event_log_provider.identifier != f'{{{wevt_provider.identifier:s}}}':
          continue

        for wevt_event in wevt_provider.events:
          if wevt_event.message_identifier != 0xffffffff:
            descriptor = resources.MessageStringMappingDescriptor(
                event_identifier=wevt_event.identifier,
                event_version=wevt_event.version,
                message_identifier=wevt_event.message_identifier)
            database_writer.AddAttributeContainer(descriptor)

  def _WriteMessageTables(
        self, message_resource_file, message_file_identifier, database_writer):
    """Writes the message tables.

    Args:
      message_resource_file (WindowsResourceFile): message resource file.
      message_file_identifier (acstore.AttributeContainerIdentifier): message
          file attribute container identifier.
      database_writer (acstore.SQLiteAttributeContainerStore): message resource
          file attribute container store.
    """
    wrc_resource = message_resource_file.GetMessageTableResource()
    if not wrc_resource:
      return

    if wrc_resource.number_of_items != 1:
      logging.warning((
          f'More than 1 message table resource item in resource file: '
          f'{message_resource_file.windows_path:s}.'))

    wrc_resource_item = wrc_resource.items[0]
    for wrc_resource_sub_item in wrc_resource_item.sub_items:
      language_identifier = wrc_resource_sub_item.identifier

      descriptor = resources.MessageTableDescriptor(
          language_identifier=language_identifier)
      descriptor.SetMessageFileIdentifier(message_file_identifier)
      database_writer.AddAttributeContainer(descriptor)

      message_table_identifier = descriptor.GetIdentifier()

      resource_data = wrc_resource_sub_item.read()

      message_table_resource = pywrc.message_table_resource()
      message_table_resource.copy_from_byte_stream(resource_data)

      number_of_messages = message_table_resource.get_number_of_messages()
      for message_index in range(number_of_messages):
        message_identifier = message_table_resource.get_message_identifier(
            message_index)
        message_string = message_table_resource.get_string(message_index)

        descriptor = resources.MessageStringDescriptor(
            identifier=message_identifier, text=message_string)
        descriptor.SetMessageTableIdentifier(message_table_identifier)
        database_writer.AddAttributeContainer(descriptor)

  def Close(self):
    """Closes the output writer object."""
    self._database_writer.Close()
    self._database_writer = None

  def Open(self):
    """Opens the output writer object.

    Returns:
      bool: True if successful or False if not.
    """
    if not os.path.isdir(self._databases_path):
      logging.warning('invalid path to the database files not a directory.')
      return False

    event_providers_database_path = os.path.join(
        self._databases_path, self.EVENT_PROVIDERS_DATABASE_FILENAME)
    if os.path.exists(event_providers_database_path):
      logging.warning((
          f'event providers database: {event_providers_database_path:s} '
          f'already exists.'))
      return False

    self._database_writer = sqlite_store.SQLiteAttributeContainerStore()
    self._database_writer.Open(
        path=event_providers_database_path, read_only=False)

    return True

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
    """
    self._database_writer.AddAttributeContainer(event_log_provider)

  def WriteMessageIdentifierMappings(
      self, event_log_provider, template_resource_file):
    """Writes the message identifier mappings.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
      template_resource_file (WindowsResourceFile): template resource file.
    """
    database_filename = self._GetDatabaseFilename(template_resource_file)
    database_path = os.path.join(self._databases_path, database_filename)

    database_writer = sqlite_store.SQLiteAttributeContainerStore()
    database_writer.Open(path=database_path, read_only=False)

    try:
      self._WriteMessageIdentifierMappings(
          event_log_provider, template_resource_file, database_writer)

    finally:
      database_writer.Close()

  # pylint: disable=unused-argument
  def WriteMessageResourceFile(
      self, windows_version, message_resource_file, message_filename,
      message_file_type):
    """Writes the Windows Message Resource file.

    Args:
      windows_version (str): Windows version.
      message_resource_file (WindowsResourceFile): message resource file.
      message_filename (str): message filename.
      message_file_type (str): message file type.
    """
    database_filename = self._GetDatabaseFilename(message_resource_file)
    database_path = os.path.join(self._databases_path, database_filename)

    database_writer = sqlite_store.SQLiteAttributeContainerStore()
    database_writer.Open(path=database_path, read_only=False)

    try:
      descriptor = resources.MessageFileDescriptor(
          file_version=message_resource_file.file_version,
          message_filename=message_resource_file.windows_path,
          product_version=message_resource_file.product_version,
          windows_version=windows_version)
      database_writer.AddAttributeContainer(descriptor)

      message_file_identifier = descriptor.GetIdentifier()

      self._WriteMessageTables(
          message_resource_file, message_file_identifier, database_writer)

    finally:
      database_writer.Close()

    descriptor = resources.MessageFileDatabaseDescriptor(
        database_filename=database_filename, message_filename=message_filename)
    self._database_writer.AddAttributeContainer(descriptor)


class StdoutOutputWriter(object):
  """Stdout output writer."""

  def _WriteMessageTable(self,  message_resource_file):
    """Writes the Windows Message Resource file message table.

    Args:
      message_resource_file (WindowsResourceFile): message resource file.
    """
    wrc_resource = message_resource_file.GetMessageTableResource()
    if not wrc_resource:
      return

    if wrc_resource.number_of_items != 1:
      logging.warning((
          f'More than 1 message table resource item in resource file: '
          f'{message_resource_file.windows_path:s}.'))

    wrc_resource_item = wrc_resource.items[0]
    for wrc_resource_sub_item in wrc_resource_item.sub_items:
      language_identifier = wrc_resource_sub_item.identifier

      resource_data = wrc_resource_sub_item.read()

      message_table_resource = pywrc.message_table_resource()
      message_table_resource.copy_from_byte_stream(resource_data)

      number_of_messages = message_table_resource.get_number_of_messages()
      if number_of_messages > 0:
        print('Message table:')
        print(f'LCID\t\t: 0x{language_identifier:08x}')
        for message_index in range(0, number_of_messages):
          message_identifier = message_table_resource.get_message_identifier(
              message_index)
          message_string = message_table_resource.get_string(message_index)

          print(f'0x{message_identifier:08x}\t: {message_string:s}')

        print('')

  def Close(self):
    """Closes the output writer object."""
    return

  def Open(self):
    """Opens the output writer object.

    Returns:
      bool: True if successful or False if not.
    """
    return True

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
    """
    log_source = event_log_provider.log_sources[0]
    log_type = event_log_provider.log_types[0]

    print(f'Source\t\t: {log_source:s}')
    print(f'Event Log type\t: {log_type:s}')

    message_files = ';'.join(event_log_provider.category_message_files)
    print(f'Categories\t: {message_files:s}')

    message_files = ';'.join(event_log_provider.event_message_files)
    print(f'Messages\t: {message_files:s}')

    message_files = ';'.join(event_log_provider.parameter_message_files)
    print(f'Parameters\t: {message_files:s}')

    print('')

  # pylint: disable=unused-argument
  def WriteMessageResourceFile(
      self, windows_version, message_resource_file, message_filename,
      message_file_type):
    """Writes the Windows Message Resource file.

    Args:
      windows_version (str): Windows version.
      message_resource_file (WindowsResourceFile): message resource file.
      message_filename (str): message filename.
      message_file_type (str): message file type.
    """
    file_version = getattr(message_resource_file, 'file_version', '')
    product_version = getattr(message_resource_file, 'product_version', '')

    print('Message file:')
    print(f'Path\t\t: {message_resource_file.windows_path:s}')
    print(f'File version\t: {file_version:s}')
    print(f'Product version\t: {product_version:s}')

    self._WriteMessageTable( message_resource_file)


def Main():
  """Entry point of console script to extract Event Log message strings.

  Returns:
    int: exit code that is provided to sys.exit().
  """
  argument_parser = argparse.ArgumentParser(description=(
      'Extract strings from message resource files for Event Log sources.'))

  argument_parser.add_argument(
      '-d', '--debug', dest='debug', action='store_true', default=False,
      help='enable debug output.')

  # TODO: replace by --output
  argument_parser.add_argument(
      '--db', '--database', dest='database', action='store',
      metavar='./winevt-kb/', default=None, help=(
          'directory to write the SQLite3 databases to.'))

  argument_parser.add_argument(
      '-w', '--windows_version', '--windows-version',
      dest='windows_version', action='store', metavar='Windows XP',
      default=None, help='string that identifies the Windows version.')

  argument_parser.add_argument(
      'source', nargs='?', action='store', metavar='/mnt/c/',
      default=None, help=(
          'path of the volume containing C:\\Windows or the filename of '
          'a storage media image containing the C:\\Windows directory.'))

  options = argument_parser.parse_args()

  if not options.source:
    print('Source value is missing.')
    print('')
    argument_parser.print_help()
    print('')
    return 1

  logging.basicConfig(
      level=logging.INFO, format='[%(levelname)s] %(message)s')

  try:
    with open(options.source, 'r', encoding='utf-8') as file_object:
      source_definitions = list(yaml.safe_load_all(file_object))

  except (SyntaxError, UnicodeDecodeError, yaml.parser.ParserError):
    source_definitions = [{
        'source': options.source, 'windows_version': options.windows_version}]

  if options.database:
    if not os.path.exists(options.database):
      os.mkdir(options.database)

    if not os.path.isdir(options.database):
      print(f'{options.database:s} must be a directory')
      print('')
      return 1

    output_writer = SQLite3OutputWriter(options.database)
  else:
    output_writer = StdoutOutputWriter()

  if not output_writer.Open():
    print('Unable to open output writer.')
    print('')
    return 1

  mediator = dfvfs_command_line.CLIVolumeScannerMediator()

  volume_scanner_options = dfvfs_volume_scanner.VolumeScannerOptions()
  volume_scanner_options.partitions = ['all']
  volume_scanner_options.snapshots = ['none']
  volume_scanner_options.volumes = ['none']

  try:
    for source_definition in source_definitions:
      source_path = source_definition['source']
      logging.info(f'Processing: {source_path:s}')

      extractor_object = extractor.EventMessageStringExtractor(
          debug=options.debug, mediator=mediator)

      try:
        result = extractor_object.ScanForWindowsVolume(
            source_path, options=volume_scanner_options)
      except dfvfs_errors.ScannerError:
        result = False

      if not result:
        print((f'Unable to retrieve the volume with the Windows directory '
               f'from: {source_path:s}.'))
        print('')
        return 1

      if extractor_object.windows_version:
        windows_version = extractor_object.windows_version
        logging.info(f'Detected Windows version: {windows_version:s}')

        if source_definition['windows_version']:
          windows_version = source_definition['windows_version']

      else:
        print('Unable to determine Windows version.')

        windows_version = source_definition['windows_version']
        if not windows_version and options.database:
          print(('Database output requires a Windows version, specify one with '
                 '--windows-version.'))
          print('')
          return 1

      extractor_object.CollectSystemEnvironmentVariables()

      # TODO: handle $(runtime.X) notation

      for event_log_provider in extractor_object.CollectEventLogProviders():
        name = event_log_provider.name or event_log_provider.log_source
        logging.info(f'Processing Event Log provider: {name:s}')

        event_log_provider.windows_version = windows_version
        output_writer.WriteEventLogProvider(event_log_provider)

        if event_log_provider.event_message_files:
          for message_filename in event_log_provider.event_message_files:
            message_resource_file = extractor_object.GetMessageResourceFile(
                event_log_provider, message_filename)

            if message_resource_file:
              logging.info(
                  f'Processing event message file: {message_filename:s}')

              output_writer.WriteMessageResourceFile(
                  windows_version, message_resource_file,
                  message_resource_file.windows_path,
                  definitions.MESSAGE_FILE_TYPE_EVENT)
              message_resource_file.Close()

              template_resource_file = extractor_object.GetTemplateResourceFile(
                  message_filename)
              if template_resource_file:
                output_writer.WriteMessageIdentifierMappings(
                    event_log_provider, template_resource_file)

        if event_log_provider.category_message_files:
          for message_filename in event_log_provider.category_message_files:
            message_resource_file = extractor_object.GetMessageResourceFile(
                event_log_provider, message_filename)

            if message_resource_file:
              logging.info(
                  f'Processing category message file: {message_filename:s}')

              output_writer.WriteMessageResourceFile(
                  windows_version, message_resource_file,
                  message_resource_file.windows_path,
                  definitions.MESSAGE_FILE_TYPE_CATEGORY)
              message_resource_file.Close()

        if event_log_provider.parameter_message_files:
          for message_filename in event_log_provider.parameter_message_files:
            message_resource_file = extractor_object.GetMessageResourceFile(
                event_log_provider, message_filename)

            if message_resource_file:
              logging.info(
                  f'Processing parameter message file: {message_filename:s}')

              output_writer.WriteMessageResourceFile(
                  windows_version, message_resource_file,
                  message_resource_file.windows_path,
                  definitions.MESSAGE_FILE_TYPE_PARAMETER)
              message_resource_file.Close()

  finally:
    output_writer.Close()

  if len(source_definitions) == 1:
    if extractor_object.missing_message_filenames:
      print('')
      print('Message resource files not found or without resource section:')
      for filename in extractor_object.missing_message_filenames:
        print(filename)

    if extractor_object.missing_resources_message_filenames:
      print('')
      print('Message resource files without a message table resource:')
      for filename in extractor_object.missing_resources_message_filenames:
        print(filename)

    print('')

  return 0


if __name__ == '__main__':
  sys.exit(Main())

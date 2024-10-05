#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script to export strings extracted from Windows EventLog message files."""

import argparse
import logging
import os
import re
import sys

from acstore import sqlite_store

from winevtrc import database
from winevtrc import definitions
from winevtrc import documentation
from winevtrc import exporter
from winevtrc import resources


class MessageResourceAttributeContainerStore(
    sqlite_store.SQLiteAttributeContainerStore):
  """Message resource attribute container store.

  Attributes:
    format_version (int): storage format version.
    serialization_format (str): serialization format.
  """

  _FORMAT_VERSION = 20240929
  _APPEND_COMPATIBLE_FORMAT_VERSION = 20240929
  _UPGRADE_COMPATIBLE_FORMAT_VERSION = 20240929
  _READ_COMPATIBLE_FORMAT_VERSION = 20240929

  def __init__(self, string_format='wrc'):
    """Initializes a message resource attribute container store.

    Args:
      string_format (Optional[str]): string format. The default is the Windows
          Resource (wrc) format.
    """
    super(MessageResourceAttributeContainerStore, self).__init__()
    self._string_format = string_format

  def _ReadAndCheckStorageMetadata(self, check_readable_only=False):
    """Reads storage metadata and checks that the values are valid.

    Args:
      check_readable_only (Optional[bool]): whether the store should only be
          checked to see if it can be read. If False, the store will be checked
          to see if it can be read and written to.

    Raises:
      IOError: when there is an error querying the attribute container store.
      OSError: when there is an error querying the attribute container store.
    """
    metadata_values = self._ReadMetadata()

    self._CheckStorageMetadata(
        metadata_values, check_readable_only=check_readable_only)

    string_format = metadata_values.get('string_format', None)

    if not string_format:
      raise IOError('Missing string format.')

    self._string_format = metadata_values['string_format']
    self.format_version = metadata_values['format_version']
    self.serialization_format = metadata_values['serialization_format']

  def _WriteMetadata(self):
    """Writes metadata.

    Raises:
      IOError: when there is an error querying the attribute container store.
      OSError: when there is an error querying the attribute container store.
    """
    super(MessageResourceAttributeContainerStore, self)._WriteMetadata()
    self._WriteMetadataValue('string_format', self._string_format)


class DatabaseOutputWriter(exporter.ExporterOutputWriter):
  """Database output writer."""

  def __init__(
      self, database_path, database_version='20150315', string_format='wrc'):
    """Initializes a database output writer.

    Args:
      database_path (str): path to the database file.
      database_version (Optional[str]): database version.
      string_format (Optional[str]): string format.
    """
    super(DatabaseOutputWriter, self).__init__()
    self._database_version = database_version
    self._database_path = database_path
    self._database_writer = None
    self._event_log_providers = {}
    self._string_format = string_format

  def _WriteMessageFilesPerEventLogProvider(self):
    """Writes mappings between Event Log providers and message files."""
    for event_log_provider in self._event_log_providers.values():
      for message_filename in event_log_provider.event_message_files:
        self._database_writer.WriteMessageFilesPerEventLogProvider(
            event_log_provider, message_filename,
            definitions.MESSAGE_FILE_TYPE_EVENT)

  def Close(self):
    """Closes the output writer object."""
    if self._database_writer:
      if self._database_version == '20150315':
        self._WriteMessageFilesPerEventLogProvider()

      self._database_writer.Close()
      self._database_writer = None
      self._database_path = None

  def Open(self):
    """Opens the output writer object.

    Returns:
      bool: True if successful or False if not.
    """
    if os.path.isdir(self._database_path):
      return False

    if self._database_version == '20150315':
      self._database_writer = database.ResourcesSQLite3DatabaseWriter(
          string_format=self._string_format)
      self._database_writer.Open(path=self._database_path)
      self._database_writer.WriteMetadata()

    else:
      self._database_writer = MessageResourceAttributeContainerStore(
          string_format=self._string_format)
      self._database_writer.Open(path=self._database_path, read_only=False)

    return True

  def WriteEventLogProvider(self, export_event_log_provider):
    """Writes an Event Log provider.

    Args:
      export_event_log_provider (ExportEventLogProvider): Event Log provider.
    """
    if len(export_event_log_provider.providers_with_versions) > 1:
      logging.warning((
          f'More than one definitions for event provider: '
          f'{export_event_log_provider.name:s} defaulting to first.'))

    # TODO: add support for windows_versions.
    event_log_provider, _ = export_event_log_provider.providers_with_versions[0]

    # TODO: check if event provider already exists.

    if self._database_version == '20150315':
      self._database_writer.WriteEventLogProvider(event_log_provider)

      self._event_log_providers[event_log_provider.name] = event_log_provider
    else:
      self._database_writer.AddAttributeContainer(event_log_provider)

  def WriteMessageFile(self, message_file):
    """Writes a message file.

    Args:
      message_file (MessageFileAttributeContainerStore): message file.
    """
    if self._database_version == '20150315':
      self._database_writer.WriteMessageFile(message_file)

      for message_table in self.GetMessageTables(message_file):
        self._database_writer.WriteMessageTable(message_file, message_table)

    else:
      # TODO: add support to handle multiple versions.
      message_file_descriptor = resources.MessageFileDescriptor(
          windows_path=message_file.windows_path)
      self._database_writer.AddAttributeContainer(message_file_descriptor)

      message_file_identifier = message_file_descriptor.GetIdentifier()

      for message_table in self.GetMessageTables(message_file):
        message_table_descriptor = resources.MessageTableDescriptor(
            language_identifier=message_table.language_identifier)
        message_table_descriptor.SetMessageFileIdentifier(
            message_file_identifier)
        self._database_writer.AddAttributeContainer(message_table_descriptor)

        message_table_identifier = message_table_descriptor.GetIdentifier()

        for message_identifier, text in message_table.message_strings.items():
          message_string_descriptor = resources.MessageStringDescriptor(
              message_identifier=message_identifier, text=text)
          message_string_descriptor.SetMessageTableIdentifier(
              message_table_identifier)
          self._database_writer.AddAttributeContainer(message_string_descriptor)

      for string_mapping in message_file.GetAttributeContainers(
          resources.MessageStringMappingDescriptor.CONTAINER_TYPE):
        string_mapping.SetMessageFileIdentifier(message_file_identifier)
        self._database_writer.AddAttributeContainer(string_mapping)


class DocumentationFilesOutputWriter(exporter.ExporterOutputWriter):
  """Documentation files output writer."""

  def __init__(self, path):
    """Initializes the documentation output writer.

    Args:
      path (str): path to the directory containing the documentation files.
    """
    super(DocumentationFilesOutputWriter, self).__init__()
    self._event_log_providers_directory = None
    self._event_log_providers_index_writer = None
    self._message_files_directory = None
    self._message_files_index_writer = None
    self._path = path

  def Close(self):
    """Closes the output writer object."""
    if self._event_log_providers_index_writer:
      self._event_log_providers_index_writer.Close()
      self._event_log_providers_index_writer = None

    self._event_log_providers_directory = None

    if self._message_files_index_writer:
      self._message_files_index_writer.Close()
      self._message_files_index_writer = None

    self._message_files_directory = None

  def Open(self):
    """Opens the output writer object.

    Returns:
      bool: True if successful or False if not.
    """
    if not os.path.isdir(self._path):
      return False

    self._event_log_providers_directory = os.path.join(
        self._path, 'docs', 'sources', 'eventlog-providers')
    os.makedirs(self._event_log_providers_directory, exist_ok=True)

    index_rst_file_path = os.path.join(
        self._event_log_providers_directory, 'index.rst')
    self._event_log_providers_index_writer = (
        documentation.EventLogProvidersIndexRstWriter(index_rst_file_path))
    self._event_log_providers_index_writer.Open()

    self._message_files_directory = os.path.join(
        self._path, 'docs', 'sources', 'message-files')
    os.makedirs(self._message_files_directory, exist_ok=True)

    index_rst_file_path = os.path.join(
        self._message_files_directory, 'index.rst')
    self._message_files_index_writer = (
        documentation.MessageFilesIndexRstWriter(index_rst_file_path))
    self._message_files_index_writer.Open()

    return True

  def WriteEventLogProvider(self, export_event_log_provider):
    """Writes an Event Log provider.

    Args:
      export_event_log_provider (ExportEventLogProvider): Event Log provider.
    """
    name = export_event_log_provider.name

    output_filename = f'Provider-{name:s}.md'.replace(
        ' ', '-').replace('/', '-')

    path = os.path.join(self._event_log_providers_directory, output_filename)
    markdown_file_writer = documentation.EventLogProviderMarkdownWriter(path)

    markdown_file_writer.Open()

    try:
      for event_log_provider, windows_versions in (
          export_event_log_provider.providers_with_versions):
        markdown_file_writer.WriteEventLogProvider(
            event_log_provider, windows_versions)

    finally:
      markdown_file_writer.Close()

    self._event_log_providers_index_writer.WriteEventLogProvider(name)

  def WriteMessageFile(self, message_file):
    """Writes a message file.

    Args:
      message_file (MessageFileAttributeContainerStore): message file.
    """
    name = message_file.name

    output_filename = f'MessageFile-{name:s}.md'.replace(
        ' ', '-').replace('/', '-')

    path = os.path.join(self._message_files_directory, output_filename)
    markdown_file_writer = documentation.MessageFileMarkdownWriter(path)

    markdown_file_writer.Open()

    try:
      markdown_file_writer.WriteMessageFile(message_file)
    finally:
      markdown_file_writer.Close()

    self._message_files_index_writer.WriteMessageFile(name)


class StdoutOutputWriter(exporter.ExporterOutputWriter):
  """Stdout output writer."""

  def _WriteMessageTable(self, message_table):
    """Writes a message table.

    Args:
      message_table (MessageTable): message table.
    """
    language_identifier = int(message_table.lcid, 16)
    language = definitions.LANGUAGES.get(language_identifier, ['', ''])[0]
    print(f'{language:s} (LCID: {message_table.lcid:s})')
    print('')
    print('Message identifier\tMessage string')

    for identifier, string in message_table.message_strings.items():
      string = re.sub(r'\n', '\\\\n', string)
      string = re.sub(r'\r', '\\\\r', string)
      string = re.sub(r'\t', '\\\\t', string)

      print(f'0x{identifier:08x}\t{string:s}')

    print('')

  def Close(self):
    """Closes the output writer."""
    return

  def Open(self):
    """Opens the output writer.

    Returns:
      bool: True if successful or False if not.
    """
    return True

  def WriteEventLogProvider(self, export_event_log_provider):
    """Writes an Event Log provider.

    Args:
      export_event_log_provider (ExportEventLogProvider): Event Log provider.
    """
    for event_log_provider, _ in (
        export_event_log_provider.providers_with_versions):

      # TODO: print windows versions.

      if event_log_provider.name:
        print(f'Name\t: {event_log_provider.name:s}')

      if event_log_provider.identifier:
        print(f'Identifier\t: {event_log_provider.identifier:s}')

      for index, log_type in enumerate(event_log_provider.log_types):
        if index == 0:
          print(f'Log type(s)\t: {log_type:s}')
        else:
          print(f'\t\t: {log_type:s}')

      for index, log_source in enumerate(event_log_provider.log_sources):
        if index == 0:
          print(f'Log source(s)\t: {log_source:s}')
        else:
          print(f'\t\t: {log_source:s}')

      # TODO: print more details.

  def WriteMessageFile(self, message_file):
    """Writes a message file.

    Args:
      message_file (MessageFileAttributeContainerStore): message file.
    """
    print(message_file.name)
    print('Path:\t{message_file.windows_path:s}')

    for message_table in self.GetMessageTables(message_file):
      self._WriteMessageTable(message_table)


def Main():
  """Entry point of console script to export extracted strings.

  Returns:
    int: exit code that is provided to sys.exit().
  """
  argument_parser = argparse.ArgumentParser(description=(
      'Export strings extracted from message files.'))

  argument_parser.add_argument(
      'source', nargs='?', action='store', metavar='./winevt-db/', default=None,
      help='directory that contains the SQLite3 with the extracted strings.')

  # TODO: replace by --output
  argument_parser.add_argument(
      '--db', '--database', dest='database', action='store',
      metavar='winevt-rc.db', default=None, help=(
          'filename of the SQLite3 database to write to.'))

  argument_parser.add_argument(
      '--database_version', '--database-version', dest='database_version',
      action='store', metavar='VERSION', default='20150315',
      choices=['20150315', '20240929'], help='the database version.')

  argument_parser.add_argument(
      '--string_format', '--string-format', dest='string_format',
      action='store', metavar='FORMAT', default='wrc',
      choices=['pep3101', 'wrc'], help='the message string format.')

  argument_parser.add_argument(
      '--wiki', dest='wiki', action='store', metavar='./winevt-kb.wiki/',
      default=None, help='path to write the wiki pages to.')

  # TODO: allow to set preferred language.

  options = argument_parser.parse_args()

  if not options.source:
    print('Source value is missing.')
    print('')
    argument_parser.print_help()
    print('')
    return 1

  if not os.path.isdir(options.source):
    print('Invalid source.')
    print('')
    return 1

  logging.basicConfig(
      level=logging.INFO, format='[%(levelname)s] %(message)s')

  if options.database:
    output_writer = DatabaseOutputWriter(
        options.database, database_version=options.database_version,
        string_format=options.string_format)
  elif options.wiki:
    output_writer = DocumentationFilesOutputWriter(options.wiki)
  else:
    output_writer = StdoutOutputWriter()

  if not output_writer.Open():
    print('Unable to open output writer.')
    print('')
    return 1

  try:
    exporter_object = exporter.Exporter()
    exporter_object.Export(options.source, output_writer)

  finally:
    output_writer.Close()

  return 0


if __name__ == '__main__':
  sys.exit(Main())

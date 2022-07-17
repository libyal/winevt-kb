#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script to extract the strings from Event Log message resource files."""

import argparse
import logging
import os
import re
import sys

from dfvfs.helpers import command_line as dfvfs_command_line
from dfvfs.helpers import volume_scanner as dfvfs_volume_scanner
from dfvfs.lib import errors as dfvfs_errors

from winevtrc import database
from winevtrc import definitions
from winevtrc import extractor


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
      logging.warning('event providers database: {0:s} already exists.'.format(
          event_providers_database_path))
      return False

    self._database_writer = database.EventProvidersSQLite3DatabaseWriter()
    self._database_writer.Open(event_providers_database_path)

    return True

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
    """
    self._database_writer.WriteEventLogProvider(event_log_provider)

  def WriteMessageResourceFile(
      self, event_log_provider, message_resource_file, message_filename,
      message_file_type):
    """Writes the Windows Message Resource file.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
      message_resource_file (MessageResourceFile): message resource file.
      message_filename (str): message filename.
      message_file_type (str): message file type.
    """
    database_filename = message_resource_file.windows_path
    _, _, database_filename = database_filename.rpartition('\\')
    database_filename = '{0:s}.db'.format(database_filename.lower())
    database_filename = re.sub(r'\.mui', '', database_filename)

    database_writer = database.MessageResourceFileSQLite3DatabaseWriter(
        message_resource_file)
    database_writer.Open(
        os.path.join(self._databases_path, database_filename))
    database_writer.WriteResources()
    database_writer.Close()

    self._database_writer.WriteMessageFile(message_filename, database_filename)

    # TODO: write the relationship between the Event Log provider and
    # the message file and the Windows version?
    self._database_writer.WriteMessageFilesPerEventLogProvider(
        event_log_provider, message_filename, message_file_type)


class StdoutOutputWriter(object):
  """Stdout output writer."""

  def _WriteMessageTable(self, message_table):
    """Writes the Windows Message Resource file message table.

    Args:
      message_table (pywrc.message_table): message table resource.
    """
    try:
      number_of_languages = message_table.get_number_of_languages()
    except IOError as exception:
      number_of_languages = 0
      logging.warning(
          'Unable to retrieve number of languages with error: {0:s}.'.format(
              exception))

    if number_of_languages > 0:
      for language_identifier in message_table.language_identifiers:
        number_of_messages = message_table.get_number_of_messages(
            language_identifier)

        if number_of_messages > 0:
          print('Message table:')
          print('LCID\t\t: 0x{0:08x}'.format(language_identifier))
          for message_index in range(0, number_of_messages):
            message_identifier = message_table.get_message_identifier(
                language_identifier, message_index)
            message_string = message_table.get_string(
                language_identifier, message_index)

            ouput_string = '0x{0:08x}\t: {1:s}'.format(
                message_identifier, message_string)

            print(ouput_string.encode('utf8'))

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
    print('Source\t\t: {0:s}'.format(
        event_log_provider.log_sources[0]))

    print('Event Log type\t: {0:s}'.format(
        event_log_provider.log_types[0]))

    print('Categories\t: {0:s}'.format(
        event_log_provider.category_message_files))

    print('Messages\t: {0:s}'.format(
        event_log_provider.event_message_files))

    print('Parameters\t: {0:s}'.format(
        event_log_provider.parameter_message_files))

    print('')

  # pylint: disable=unused-argument
  def WriteMessageResourceFile(
      self, event_log_provider, message_resource_file, message_filename,
      message_file_type):
    """Writes the Windows Message Resource file.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
      message_resource_file (MessageResourceFile): message resource file.
      message_filename (str): message filename.
      message_file_type (str): message file type.
    """
    file_version = getattr(message_resource_file, 'file_version', '')
    product_version = getattr(message_resource_file, 'product_version', '')

    print('Message file:')
    print('Path\t\t: {0:s}'.format(message_resource_file.windows_path))
    print('File version\t: {0:s}'.format(file_version))
    print('Product version\t: {0:s}'.format(product_version))

    message_table = message_resource_file.GetMessageTableResource()
    self._WriteMessageTable(message_table)


def Main():
  """The main program function.

  Returns:
    bool: True if successful or False if not.
  """
  argument_parser = argparse.ArgumentParser(description=(
      'Extract strings from message resource files for Event Log sources.'))

  argument_parser.add_argument(
      '-d', '--debug', dest='debug', action='store_true', default=False,
      help='enable debug output.')

  argument_parser.add_argument(
      '--db', '--database', dest='database', action='store',
      metavar='./winevt-kb/', default=None, help=(
          'directory to write the sqlite3 databases to.'))

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
    return False

  logging.basicConfig(
      level=logging.INFO, format='[%(levelname)s] %(message)s')

  if options.database:
    if not os.path.exists(options.database):
      os.mkdir(options.database)

    if not os.path.isdir(options.database):
      print('{0:s} must be a directory'.format(options.database))
      print('')
      return False

    output_writer = SQLite3OutputWriter(options.database)
  else:
    output_writer = StdoutOutputWriter()

  mediator = dfvfs_command_line.CLIVolumeScannerMediator()
  extractor_object = extractor.EventMessageStringExtractor(
      debug=options.debug, mediator=mediator)

  volume_scanner_options = dfvfs_volume_scanner.VolumeScannerOptions()
  volume_scanner_options.partitions = ['all']
  volume_scanner_options.snapshots = ['none']
  volume_scanner_options.volumes = ['none']

  try:
    result = extractor_object.ScanForWindowsVolume(
        options.source, options=volume_scanner_options)
  except dfvfs_errors.ScannerError:
    result = False

  if not result:
    print(('Unable to retrieve the volume with the Windows directory from: '
           '{0:s}.').format(options.source))
    print('')
    return False

  if not extractor_object.windows_version:
    if not options.windows_version:
      print('Unable to determine Windows version.')

      if options.database:
        print('Database output requires a Windows version, specify one with '
              '--windows-version.')
        print('')
        return False

    extractor_object.windows_version = options.windows_version

  if not output_writer.Open():
    print('Unable to open output writer.')
    print('')
    return False

  try:
    logging.info('Detected Windows version: {0:s}'.format(
        extractor_object.windows_version))

    extractor_object.CollectSystemEnvironmentVariables()

    # TODO: handle $(runtime.X) notation

    for event_log_provider in extractor_object.CollectEventLogProviders():
      name = event_log_provider.name or event_log_provider.log_source
      logging.info('Processing Event Log provider: {0:s}'.format(name))
      output_writer.WriteEventLogProvider(event_log_provider)

      if event_log_provider.event_message_files:
        for message_filename in event_log_provider.event_message_files:
          message_resource_file = extractor_object.GetMessageResourceFile(
              event_log_provider, message_filename)

          if message_resource_file:
            logging.info('Processing event message file: {0:s}'.format(
                message_filename))

            output_writer.WriteMessageResourceFile(
                event_log_provider, message_resource_file,
                message_resource_file.windows_path,
                definitions.MESSAGE_FILE_TYPE_EVENT)
            message_resource_file.Close()

      if event_log_provider.category_message_files:
        for message_filename in event_log_provider.category_message_files:
          message_resource_file = extractor_object.GetMessageResourceFile(
              event_log_provider, message_filename)

          if message_resource_file:
            logging.info('Processing category message file: {0:s}'.format(
                message_filename))

            output_writer.WriteMessageResourceFile(
                event_log_provider, message_resource_file,
                message_resource_file.windows_path,
                definitions.MESSAGE_FILE_TYPE_CATEGORY)
            message_resource_file.Close()

      if event_log_provider.parameter_message_files:
        for message_filename in event_log_provider.parameter_message_files:
          message_resource_file = extractor_object.GetMessageResourceFile(
              event_log_provider, message_filename)

          if message_resource_file:
            logging.info('Processing parameter message file: {0:s}'.format(
                message_filename))

            output_writer.WriteMessageResourceFile(
                event_log_provider, message_resource_file,
                message_resource_file.windows_path,
                definitions.MESSAGE_FILE_TYPE_PARAMETER)
            message_resource_file.Close()

  finally:
    output_writer.Close()

  if extractor_object.missing_message_filenames:
    print('')
    print('Message resource files not found or without resource section:')
    for message_filename in extractor_object.missing_message_filenames:
      print('{0:s}'.format(message_filename))

  if extractor_object.missing_resources_message_filenames:
    print('')
    print('Message resource files without a string and message table resource:')
    for message_filename in (
        extractor_object.missing_resources_message_filenames):
      print('{0:s}'.format(message_filename))

  print('')
  return True


if __name__ == '__main__':
  if not Main():
    sys.exit(1)
  else:
    sys.exit(0)

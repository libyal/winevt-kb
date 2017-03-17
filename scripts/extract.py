#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Script to extract the strings from Event Log message resource files."""

from __future__ import print_function
import argparse
import logging
import os
import re
import sys

from winevtrc import database
from winevtrc import extractor


class Sqlite3OutputWriter(object):
  """Class that defines a sqlite3 output writer."""

  EVENT_PROVIDERS_DATABASE_FILENAME = u'winevt-kb.db'

  def __init__(self, databases_path):
    """Initializes an output writer object.

    Args:
      databases_path (str): path to the database files.
    """
    super(Sqlite3OutputWriter, self).__init__()
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
      return False

    self._database_writer = database.EventProvidersSqlite3DatabaseWriter()
    self._database_writer.Open(os.path.join(
        self._databases_path, self.EVENT_PROVIDERS_DATABASE_FILENAME))

    return True

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
    """
    self._database_writer.WriteEventLogProvider(event_log_provider)

  def WriteMessageFile(
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
    _, _, database_filename = database_filename.rpartition(u'\\')
    database_filename = u'{0:s}.db'.format(database_filename.lower())
    database_filename = re.sub(r'\.mui', '', database_filename)

    database_writer = database.MessageFileSqlite3DatabaseWriter(
        message_resource_file)
    database_writer.Open(
        os.path.join(self._databases_path, database_filename))
    database_writer.WriteResources()
    database_writer.Close()

    self._database_writer.WriteMessageFile(message_filename, database_filename)

    # TODO: write the relationship between the event log provider and
    # the message file and the Windows version?
    self._database_writer.WriteMessageFilesPerEventLogProvider(
        event_log_provider, message_filename, message_file_type)


class StdoutOutputWriter(object):
  """Class that defines a stdout output writer."""

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
          u'Unable to retrieve number of languages with error: {0:s}.'.format(
              exception))

    if number_of_languages > 0:
      for language_identifier in message_table.language_identifiers:
        number_of_messages = message_table.get_number_of_messages(
            language_identifier)

        if number_of_messages > 0:
          print(u'Message table:')
          print(u'LCID\t\t: 0x{0:08x}'.format(language_identifier))
          for message_index in range(0, number_of_messages):
            message_identifier = message_table.get_message_identifier(
                language_identifier, message_index)
            message_string = message_table.get_string(
                language_identifier, message_index)

            ouput_string = u'0x{0:08x}\t: {1:s}'.format(
                message_identifier, message_string)

            print(ouput_string.encode(u'utf8'))

          print(u'')

  def Close(self):
    """Closes the output writer object."""
    pass

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
    print(u'Source\t\t: {0:s}'.format(
        event_log_provider.log_source))

    print(u'Event Log type\t: {0:s}'.format(
        event_log_provider.log_type))

    print(u'Categories\t: {0:s}'.format(
        event_log_provider.category_message_files))

    print(u'Messages\t: {0:s}'.format(
        event_log_provider.event_message_files))

    print(u'Parameters\t: {0:s}'.format(
        event_log_provider.parameter_message_files))

    print(u'')

  def WriteMessageFile(
      self, unused_event_log_provider, message_file, unused_message_filename,
      unused_message_type):
    """Writes the Windows Message Resource file.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
      message_resource_file (MessageResourceFile): message resource file.
      message_filename (str): message filename.
      message_file_type (str): message file type.
    """
    file_version = getattr(message_file, u'file_version', u'')
    product_version = getattr(message_file, u'product_version', u'')

    print(u'Message file:')
    print(u'Path\t\t: {0:s}'.format(message_file.windows_path))
    print(u'File version\t: {0:s}'.format(file_version))
    print(u'Product version\t: {0:s}'.format(product_version))

    message_table = message_file.GetMessageTableResource()
    self._WriteMessageTable(message_table)


def Main():
  """The main program function.

  Returns:
    bool: True if successful or False if not.
  """
  argument_parser = argparse.ArgumentParser(description=(
      u'Extract strings from message resource files for Event Log sources.'))

  argument_parser.add_argument(
      u'-d', u'--debug', dest=u'debug', action=u'store_true', default=False,
      help=u'enable debug output.')

  argument_parser.add_argument(
      u'--db', u'--database', dest=u'database', action=u'store',
      metavar=u'./winevt-kb/', default=None, help=(
          u'directory to write the sqlite3 databases to.'))

  argument_parser.add_argument(
      u'--winver', dest=u'windows_version', action=u'store', metavar=u'xp',
      default=None, help=(
          u'string that identifies the Windows version in the database.'))

  argument_parser.add_argument(
      u'source', nargs=u'?', action=u'store', metavar=u'/mnt/c/',
      default=None, help=(
          u'path of the volume containing C:\\Windows or the filename of '
          u'a storage media image containing the C:\\Windows directory.'))

  options = argument_parser.parse_args()

  if not options.source:
    print(u'Source value is missing.')
    print(u'')
    argument_parser.print_help()
    print(u'')
    return False

  logging.basicConfig(
      level=logging.INFO, format=u'[%(levelname)s] %(message)s')

  if options.database:
    if not os.path.exists(options.database):
      os.mkdir(options.database)

    if not os.path.isdir(options.database):
      print(u'{0:s} must be a directory'.format(options.database))
      print(u'')
      return False

    output_writer = Sqlite3OutputWriter(options.database)
  else:
    output_writer = StdoutOutputWriter()

  if not output_writer.Open():
    print(u'Unable to open output writer.')
    print(u'')
    return False

  # TODO: pass mediator.
  extractor_object = extractor.EventMessageStringExtractor(debug=options.debug)

  if not extractor_object.ScanForWindowsVolume(options.source):
    print((u'Unable to retrieve the volume with the Windows directory from: '
           u'{0:s}.').format(options.source))
    print(u'')
    return False

  if not extractor_object.windows_version:
    if not options.windows_version:
      print(u'Unable to determine Windows version.')

      if options.database:
        print(u'Database output requires a Windows version, specify one with '
              u'--winver.')
        print(u'')
        return False

    extractor_object.windows_version = options.windows_version

  print(u'Windows version: {0:s}.'.format(extractor_object.windows_version))
  print(u'')

  extractor_object.ExtractEventLogMessageStrings(output_writer)
  output_writer.Close()

  if extractor_object.invalid_message_filenames:
    print(u'Message resource files not found or without resource section:')
    for message_filename in extractor_object.invalid_message_filenames:
      print(u'{0:s}'.format(message_filename))
    print(u'')

  if extractor_object.missing_table_message_filenames:
    print(u'Message resource files without a message table resource:')
    for message_filename in extractor_object.missing_table_message_filenames:
      print(u'{0:s}'.format(message_filename))
    print(u'')

  return True


if __name__ == u'__main__':
  if not Main():
    sys.exit(1)
  else:
    sys.exit(0)

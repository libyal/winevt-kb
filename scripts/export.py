#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script to export strings extracted from Windows EventLog message files."""

import argparse
import logging
import os
import re
import sys

from winevtrc import database
from winevtrc import definitions
from winevtrc import exporter


class SQLite3OutputWriter(object):
  """Class that defines a SQLite3 output writer."""

  def __init__(self, database_path, string_format='wrc'):
    """Initializes an output writer object.

    Args:
      database_path (str): path to the database file.
      string_format (Optional[str]): string format.
    """
    super(SQLite3OutputWriter, self).__init__()
    self._database_path = database_path
    self._database_writer = None
    self._string_format = string_format

  def _WriteMetadata(self):
    """Writes the metadata."""
    self._database_writer.WriteMetadataAttribute(
        'version', '20150315')
    self._database_writer.WriteMetadataAttribute(
        'string_format', self._string_format)

  def Close(self):
    """Closes the output writer object."""
    self._database_writer.Close()
    self._database_writer = None

  def Open(self):
    """Opens the output writer object.

    Returns:
      bool: True if successful or False if not.
    """
    if os.path.isdir(self._database_path):
      return False

    self._database_writer = database.ResourcesSQLite3DatabaseWriter(
        string_format=self._string_format)
    self._database_writer.Open(self._database_path)
    self._WriteMetadata()

    return True

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
    """
    # TODO: check if already exists.
    self._database_writer.WriteEventLogProvider(event_log_provider)

  def WriteMessageFile(self, message_file):
    """Writes a message file.

    Args:
      message_file (MessageFile): message file.
    """
    self._database_writer.WriteMessageFile(message_file)

  def WriteMessageFilesPerEventLogProvider(
      self, event_log_provider, message_file):
    """Writes the Windows Message Resource file per Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
      message_file (MessageFile): message file.
    """
    self._database_writer.WriteMessageFilesPerEventLogProvider(
        event_log_provider, message_file, definitions.MESSAGE_FILE_TYPE_EVENT)

  def WriteMessageTable(self, message_file, message_table):
    """Writes a message table.

    Args:
      message_file (MessageFile): message file.
      message_table (MessageTable): message table.
    """
    self._database_writer.WriteMessageTable(message_file, message_table)


class StdoutOutputWriter(object):
  """Class that defines a stdout output writer."""

  def Open(self):
    """Opens the file.

    Returns:
      bool: True if successful or False if not.
    """
    return True

  def Close(self):
    """Closes the file."""

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
    """
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
      message_file (MessageFile): message file.
    """
    print(message_file.name)
    print('Path:\t{message_file.windows_path:s}')

  # pylint: disable=unused-argument
  def WriteMessageFilesPerEventLogProvider(
      self, event_log_provider, message_file):
    """Writes the Windows Message Resource file per Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
      message_file (MessageFile): message file.
    """
    return

  def WriteMessageTable(self, message_file, message_table):
    """Writes a message table.

    Args:
      message_file (MessageFile): message file.
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


class MarkdownFileWriter(object):
  """Class to represent a Markdown file writer."""

  def __init__(self):
    """Initializes the Markdown file writer object."""
    super(MarkdownFileWriter, self).__init__()
    self._file = None

  def Open(self, filename):
    """Opens the file.

    Args:
      filename (str): name of the file.

    Returns:
      bool: True if successful or False if not.
    """
    # Using binary mode to make sure to write Unix end of lines.
    self._file = open(filename, 'wb')  # pylint: disable=consider-using-with
    return True

  def Close(self):
    """Closes the file."""
    self._file.close()

  def WriteLine(self, line):
    """Writes a line."""
    self._file.write(f'{line:s}\n'.encode('utf8'))

  def WriteLines(self, lines):
    """Writes lines."""
    for line in lines:
      self.WriteLine(line)


class MarkdownOutputWriter(object):
  """Class that defines a Markdown output writer."""

  def __init__(self, path):
    """Initializes the Markdown output writer object.

    Args:
      path (str): path to the directory containing the Markdown files.
    """
    super(MarkdownOutputWriter, self).__init__()
    self._message_file_writer = None
    self._path = path

  def Close(self):
    """Closes the output writer object."""
    if self._message_file_writer:
      self._message_file_writer.Close()
      self._message_file_writer = None

  def Open(self):
    """Opens the output writer object.

    Returns:
      bool: True if successful or False if not.
    """
    if not os.path.isdir(self._path):
      return False
    return True

  # pylint: disable=unused-argument
  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
    """
    # TODO: print details.
    return

  def WriteMessageFile(self, message_file):
    """Writes a message file.

    Args:
      message_file (MessageFile): message file.
    """
    if self._message_file_writer:
      self._message_file_writer.Close()
      self._message_file_writer = None

    self._message_file_writer = MarkdownFileWriter()
    path = os.path.join(self._path, f'{message_file.name:s}.md')

    if self._message_file_writer.Open(path):
      self._message_file_writer.WriteLines([
          f'## {message_file.name:s}',
          '',
          'Path: {message_file.windows_path:s}',
          ''])

  def WriteMessageFilesPerEventLogProvider(
      self, event_log_provider, message_file):
    """Writes the Windows Message Resource file per Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
      message_file (MessageFile): message file.
    """
    return

  def WriteMessageTable(self, message_file, message_table):
    """Writes a message table.

    Args:
      message_file (MessageFile): message file.
      message_table (MessageTable): message table.
    """
    language_identifier = int(message_table.lcid, 16)
    language = definitions.LANGUAGES.get(language_identifier, ['', ''])[0]
    self._message_file_writer.WriteLines([
        f'### {language:s} (LCID: {message_table.lcid:s})',
        '',
        'Message identifier | Message string',
        '--- | ---'])

    for identifier, string in message_table.message_strings.items():
      string = re.sub(r'\n', '\\\\n', string)
      string = re.sub(r'\r', '\\\\r', string)
      string = re.sub(r'\t', '\\\\t', string)

      self._message_file_writer.WriteLine(f'0x{identifier:08x} | {string:s}')

    self._message_file_writer.WriteLine('')


def Main():
  """The main program function.

  Returns:
    bool: True if successful or False if not.
  """
  argument_parser = argparse.ArgumentParser(description=(
      'Export strings extracted from message files.'))

  argument_parser.add_argument(
      'source', nargs='?', action='store', metavar='./winevt-db/',
      default=None, help=(
          'directory that contains the SQLite3 with the extracted strings.'))

  # TODO: replace by --output
  argument_parser.add_argument(
      '--db', '--database', dest='database', action='store',
      metavar='winevt-rc.db', default=None, help=(
          'filename of the SQLite3 database to write to.'))

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
    return False

  if not os.path.isdir(options.source):
    print('Invalid source.')
    print('')
    return False

  logging.basicConfig(
      level=logging.INFO, format='[%(levelname)s] %(message)s')

  if options.database:
    output_writer = SQLite3OutputWriter(
        options.database, string_format=options.string_format)
  elif options.wiki:
    output_writer = MarkdownOutputWriter(options.wiki)
  else:
    output_writer = StdoutOutputWriter()

  if not output_writer.Open():
    print('Unable to open output writer.')
    print('')
    return False

  try:
    exporter_object = exporter.Exporter()
    exporter_object.Export(options.source, output_writer)

  finally:
    output_writer.Close()

  return True


if __name__ == '__main__':
  if not Main():
    sys.exit(1)
  else:
    sys.exit(0)

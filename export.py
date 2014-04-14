#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Script to export strings extracted from message files.
#
# Copyright (c) 2013-2014, Joachim Metz <joachim.metz@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import os

import sqlite3


class Exporter(object):
  """Class that exports the strings extracted from message files."""

  EVENT_PROVIDERS_DATABASE_FILENAME = u'winevt-kb.db'

  def __init__(self):
    """Initializes the exporter object."""
    super(Exporter, self).__init__()

  def _ExportMessageFiles(
      self, source_path, event_provider_database, output_writer):
    """Exports the message files an event provider database.

    Args:
      source_path: the source path.
      event_provider_database: the event provider database (instance of
                               Sqlite3DatabaseFile).
      output_writer: the output writer (instance of OutputWriter).
    """
    table_names = ['message_files']
    column_names = ['database_filename']
    condition = ''

    for values in event_provider_database.GetValues(
        table_names, column_names, condition):
      message_file_path = os.path.join(source_path, values['database_filename'])

      if not os.path.exists(message_file_path):
        logging.warning(u'Missing message file database: {0:s}.'.format(
            values['database_filename']))
        continue

      message_file_database = Sqlite3DatabaseFile()
      message_file_database.Open(message_file_path)

      self._ExportMessageStrings(message_file_database, output_writer)
      self._ExportStrings(message_file_database, output_writer)

      message_file_database.Close()

  def _ExportMessageStrings(self, message_file_database, output_writer):
    """Exports the message strings in a message file database.

    Args:
      message_file_database: the message file database (instance of
                             Sqlite3DatabaseFile).
      output_writer: the output writer (instance of OutputWriter).
    """
    table_names = ['message_files', 'languague_per_message_file']
    column_names = ['file_version', 'lcid']
    condition = (
        'message_files.message_file_key = '
        'languague_per_message_file.message_file_key')

    message_strings_tables = []
    for values in event_provider_database.GetValues(
        table_names, column_names, condition):
       table_name = 'message_table_{0:s}_{1:s}'.format(
           values['lcid'], values['file_version'])

       message_strings_tables.append(table_name)

    column_names = ['message_identifier', 'message_string']
    condition = ''

    # TODO: create objects to track message strings and versions.
    message_strings = {}

    for table_name in message_strings_tables:
      for values in event_provider_database.GetValues(
          [table_name], column_names, condition):
        message_identifier = values['message_identifier']
        message_string = values['message_string']

        if message_identifier not in message_strings:
          message_strings[message_identifier] = message_string

        elif message_strings[message_identifier] != message_string:
          logging.warning((
              u'Found duplicate alternating message string: {0:s} '
              u'in {1:s}.\nPrevious: {1:s}\nNew:{2:s}\n').format(
                  message_identifier, table_name,
                  message_strings[message_identifier], message_string)

        # TODO: determine which string to use.

    # TODO: write message_strings to output.

  def _ExportStrings(self, message_file_database, output_writer):
    """Exports the strings in a message file database.

    Args:
      message_file_database: the message file database (instance of
                             Sqlite3DatabaseFile).
      output_writer: the output writer (instance of OutputWriter).
    """
    # TODO: iterate and merge the strings tables.
    pass

  def Export(self, source_path, output_writer):
    """Exports the strings extracted from message files.

    Args:
      source_path: the source path.
      output_writer: the output writer (instance of OutputWriter).
    """
    event_provider_database = Sqlite3DatabaseFile()
    event_provider_database.Open(os.path.join(
        source_path, self.EVENT_PROVIDERS_DATABASE_FILENAME))

    # TODO: read the table with event providers
    # messages and categories.

    table_names = []
    column_names = []
    condition = ''

    for values in event_provider_database.GetValues(
        table_names, column_names, condition):
      # TODO: create a look up if the messages per event provider
      pass

    self._ExportMessageFiles(
        source_path, event_provider_database, output_writer)

    event_provider_database.Close()


class Sqlite3DatabaseFile(object):
  """Class that defines a sqlite3 database file."""

  _HAS_TABLE_QUERY = (
      u'SELECT name FROM sqlite_master '
      u'WHERE type = "table" AND name = "{0:s}"')

  def __init__(self):
    """Initializes the database file object."""
    super(Sqlite3DatabaseFile, self).__init__()
    self._connection = None
    self._cursor = None
    self.filename = None

  def Close(self):
    """Closes the database file."""
    # We need to run commit or not all data is stored in the database.
    self._connection.commit()
    self._connection.close()

    self._connection = None
    self._cursor = None
    self.filename = None

  def CreateTable(self, table_name, column_definitions):
    """Creates a table.

    Args:
      table_name: the table name.
      column_definitions: list of strings containing column definitions.
    """
    sql_query = u'CREATE TABLE {0:s} ( {1:s} )'.format(
        table_name, u', '.join(column_definitions))

    self._cursor.execute(sql_query)

  def HasTable(self, table_name):
    """Determines if a specific table exists.

    Args:
      table_name: the table name.

    Returns:
      True if the table exists, false otheriwse.
    """
    sql_query = self._HAS_TABLE_QUERY.format(table_name)

    self._cursor.execute(sql_query)
    if self._cursor.fetchone():
      has_table = True
    else:
      has_table = False
    return has_table

  def GetValues(self, table_names, column_names, condition):
    """Retrieves values from a table.

    Args:
      table_names: list of table names.
      column_names: list of column names.
      condition: string containing the condition.

    Yields:
      A row object (instance of sqlite3.row).
    """
    if condition:
      condition = u' WHERE {0:s}'.format(condition)

    sql_query = u'SELECT {1:s} FROM {0:s}{2:s}'.format(
        u', '.join(table_names), u', '.join(column_names), condition)

    self._cursor.execute(sql_query)

    for row in self._cursor:
      values = {}
      for column_index in range(0, len(column_names)):
        column_name = column_names[column_index]
        values[column_name] = row[column_index]
      yield values

  def InsertValues(self, table_name, column_names, values):
    """Inserts values into a table.

    Args:
      table_name: the table name.
      column_names: list of column names.
      values: list of values formatted as a string.

    Raises:
      RuntimeError: if an unsupported value type is encountered.
    """
    if not values:
      return

    sql_values = []
    for value in values:
      if isinstance(value, basestring):
        # In sqlite3 the double quote is escaped with a second double quote.
        value = u'"{0:s}"'.format(re.sub('"', '""', value))
      elif isinstance(value, (int, long)):
        value = u'{0:d}'.format(value)
      elif isinstance(value, float):
        value = u'{0:f}'.format(value)
      else:
        raise RuntimeError(u'Unsupported value type.')
      sql_values.append(value)

    sql_query = u'INSERT INTO {0:s} ( {1:s} ) VALUES ( {2:s} )'.format(
        table_name, u', '.join(column_names), u', '.join(sql_values))

    self._cursor.execute(sql_query)

  def Open(self, filename):
    """Opens the database file.

    Args:
      filename: the filename of the database.

    Returns:
      A boolean containing True if successful or False if not.
    """
    self.filename = filename
    self._connection = sqlite3.connect(filename)
    if not self._connection:
      return False

    self._cursor = self._connection.cursor()
    if not self._cursor:
      return False

    return True


# TODO: refactor
class Sqlite3OutputWriter(object):
  """Class that defines a sqlite3 output writer."""

  def __init__(self, databases_path):
    """Initializes the output writer object.

    Args:
      databases_path: the path to the database files.
    """
    super(Sqlite3OutputWriter, self).__init__()
    self._databases_path = databases_path
    self._event_providers_writer = None

  def Close(self):
    """Closes the output writer object."""
    self._event_providers_writer.Close()
    self._event_providers_writer = None

  def Open(self):
    """Opens the output writer object.

    Returns:
      A boolean containing True if successful or False if not.
    """
    if not os.path.isdir(self._databases_path):
      return False

    self._event_providers_writer = Sqlite3EventProvidersWriter()
    self._event_providers_writer.Open(
        os.path.join(self._databases_path, 'winevt-kb.db'))

    return True


class StdoutOutputWriter(object):
  """Class that defines a stdout output writer."""


class WikiMessageFileWriter(object):
  """Class to represent a Google Code wiki message file writer."""
  # TODO: aparantly the filename should only contain 1 dot and end with .wiki

  def Open(self, filename):
    """Opens the file.

    Args:
      filename: the filename.
    """
    # Using binary mode to make sure to write Unix end of lines.
    self._file = open(filename, 'wb')

  def Close(self):
    """Closes the file."""
    self._file.close()

  def WriteLine(self, line):
    """Writes a line."""
    self._file.write('{0:s}\r\n'.format(line))

  def WriteLines(self, lines):
    """Writes lines."""
    for line in lines:
      self.WriteLine(line)


class WikiOutputWriter(object):
  """Class that defines a Google Code wiki output writer."""

  def __init__(self, wiki_path):
    """Initializes the Windows volume collector object.

    Args:
      wiki_path: the path to the directory containing the wiki files.
    """
    super(WikiOutputWriter, self).__init__()
    self._wiki_path = wiki_path

  def _WriteMessageTable(self, message_table):
    """Writes the Windows Message Resource file message table.

    Args:
      message_table: the message table (instance of pywrc.message_table).
    """
    if message_table.number_of_languages > 0:
      for language_identifier in message_table.language_identifiers:
        number_of_messages = message_table.get_number_of_messages(
            language_identifier)

        if number_of_messages > 0:
          print '== LCID: 0x{0:08x} =='.format(language_identifier)
          print '|| *Message identifier* || *Message string* ||'

          for message_index in range(0, number_of_messages):
            message_identifier = message_table.get_message_identifier(
                language_identifier, message_index)
            message_string = message_table.get_string(
                language_identifier, message_index)

            message_string = re.sub(r'\n', '\\\\n', message_string)
            message_string = re.sub(r'\r', '\\\\r', message_string)
            message_string = re.sub(r'\t', '\\\\t', message_string)

            ouput_string = u'|| 0x{0:08x} || {{{{{{ {1:s} }}}}}} ||'.format(
                message_identifier, message_string)

            print ouput_string.encode('utf8')

          print ''

  def Close(self):
    """Closes the output writer object."""
    pass

  def Open(self):
    """Opens the output writer object.

    Returns:
      A boolean containing True if successful or False if not.
    """
    if not os.path.isdir(self._wiki_path):
      return False
    return True

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
    """
    # TODO: implement.
    return

  def WriteMessageFile(
      self, event_log_provider, message_file, message_filename):
    """Writes the Windows Message Resource file.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
      message_file: the message file (instance of MessageResourceFile).
      message_filename: the message filename.
    """
    # TODO: create file.

    file_version = getattr(message_file, 'file_version', '')
    product_version = getattr(message_file, 'product_version', '')

    print u'= Message file ='
    print u'|| *Path:* || {0:s} ||'.format(message_file.windows_path)
    print u'|| *File version:* || {0:s} ||'.format(file_version)
    print u'|| *Product version:* || {0:s} ||'.format(product_version)
    print ''

    message_table = message_file.GetMessageTableResource()
    self.WriteMessageTable(message_table)


def Main():
  """The main program function.

  Returns:
    A boolean containing True if successful or False if not.
  """
  args_parser = argparse.ArgumentParser(description=(
      'Export strings extracted from message files.'))

  args_parser.add_argument(
      'source', nargs='?', action='store', metavar='./winevt-db/',
      default=None, help=('path of the directory that contains the sqlite3 '
                          'with the extracted strings.'))

  args_parser.add_argument(
      '--db', dest='database', action='store', metavar='winevt.db',
      default=None, help='filename to write the sqlite3 database to.')

  args_parser.add_argument(
      '--wiki', dest='wiki', action='store', metavar='./winevt-kb.wiki/',
      default=None, help='path to write the wiki pages to.')

  # TODO: allow to set preferred language.

  options = args_parser.parse_args()

  if not options.source:
    print u'Source value is missing.'
    print u''
    args_parser.print_help()
    print u''
    return False

  if not os.path.isdir(options.source):
    print u'Invalid source.'
    print u''
    return False

  logging.basicConfig(
      level=logging.INFO, format=u'[%(levelname)s] %(message)s')

  if options.database:
    output_writer = Sqlite3OutputWriter(options.database)
  elif options.wiki:
    output_writer = WikiOutputWriter(options.wiki)
  else:
    output_writer = StdoutOutputWriter()

  if not output_writer.Open():
    print u'Unable to open output writer.'
    print u''
    return False

  exporter = Exporter()
  exporter.Export(options.source, output_writer)
  output_writer.Close()

  return True


if __name__ == '__main__':
  if not Main():
    sys.exit(1)
  else:
    sys.exit(0)

#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Script to export strings extracted from message files.
#
# Copyright (c) 2013-2015, Joachim Metz <joachim.metz@gmail.com>
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

import argparse
import logging
import os
import re
import sys

import sqlite3


class EventLogProvider(object):
  """Class that defines a Windows Event Log provider."""

  def __init__(
      self, log_type, log_source, category_message_filenames,
      event_message_filenames, parameter_message_filenames):
    """Initializes the Windows Event Log provider.

    Args:
      log_type: the Event Log type.
      log_source: the Event Log source.
      category_message_filenames: the message filenames that contain
                                  the category strings.
      event_message_filenames: the message filenames that contain
                               the event messages.
      parameter_message_filenames: the message filenames that contain
                                   the parameter strings.
    """
    super(EventLogProvider, self).__init__()
    self.log_type = log_type
    self.log_source = log_source

    # It not empty the messages filenames can contain a list
    # of message file paths separated by ;
    if category_message_filenames:
      self.category_message_files = category_message_filenames.split(';')
    else:
      self.category_message_files = category_message_filenames

    if event_message_filenames:
      self.event_message_files = event_message_filenames.split(';')
    else:
      self.event_message_files = event_message_filenames

    if parameter_message_filenames:
      self.parameter_message_files = parameter_message_filenames.split(';')
    else:
      self.parameter_message_files = parameter_message_filenames


class MessageFile(object):
  """Class that contains the messages per file."""

  def __init__(self, name):
    """Initializes the message file object.

    Args:
      name: the name.
    """
    super(MessageFile, self).__init__()
    self.name = name
    self.file_version = None
    self.product_version = None
    self.tables_per_language = {}
    self.windows_path = None

  def AppendTable(self, lcid, language, table_name):
    """Appends a table for a specific language.

    Args:
      lcid: the language identifier.
      language: the language.
      table_name: the table name.
    """
    if lcid not in self.tables_per_language:
      self.tables_per_language[lcid] = MessageTable(lcid, language)

    self.tables_per_language[lcid].tables.append(table_name)

  def GetMessageTable(self, lcid):
    """Retrieves the message table for a specific language.

    Args:
      lcid: the language identifier.

    Returns:
      The message table (instance of MessageTable).
    """
    return self.tables_per_language.get(lcid, None)

  def GetMessageTables(self):
    """Retrieves the message tables.

    Yields:
      Message tables (instances of MessageTable).
    """
    for message_table in self.tables_per_language.itervalues():
      yield message_table


class MessageTable(object):
  """Class that contains the messages per language."""

  def __init__(self, lcid, language):
    """Initializes the message table object.

    Args:
      lcid: the language identifier.
      language: the language.
    """
    super(MessageTable, self).__init__()
    self.language = language
    self.lcid = lcid
    self.message_strings = {}
    self.tables = []


class Exporter(object):
  """Class that exports the strings extracted from message files."""

  EVENT_PROVIDERS_DATABASE_FILENAME = u'winevt-kb.db'

  def __init__(self):
    """Initializes the exporter object."""
    super(Exporter, self).__init__()

  def _ExportEventLogProviders(self, event_provider_database, output_writer):
    """Exports the event log provides from an event provider database.

    Args:
      event_provider_database: the event provider database (instance of
                               Sqlite3DatabaseFile).
      output_writer: the output writer (instance of OutputWriter).
    """
    # TODO
    return

  def _ExportMessageFiles(
      self, source_path, event_provider_database, output_writer):
    """Exports the message files from an event provider database.

    Args:
      source_path: the source path.
      event_provider_database: the event provider database (instance of
                               Sqlite3DatabaseFile).
      output_writer: the output writer (instance of OutputWriter).
    """
    table_names = ['message_files']
    column_names = ['message_filename', 'database_filename']
    condition = ''

    for values in event_provider_database.GetValues(
        table_names, column_names, condition):
      database_filename = values['database_filename']
      message_file_path = os.path.join(source_path, database_filename)

      if not os.path.exists(message_file_path):
        logging.warning(
            u'Missing message file database: {0:s}.'.format(database_filename))
        continue

      logging.info('Processing: {0:s}'.format(database_filename))
      message_file_database = Sqlite3DatabaseFile()
      message_file_database.Open(message_file_path)

      message_file = MessageFile(database_filename[:-3])

      # TODO: fill file version and product version
      message_file.windows_path = values['message_filename']

      self._ExportMessageStrings(message_file, message_file_database)
      self._ExportStrings(message_file, message_file_database)

      message_file_database.Close()

      output_writer.WriteMessageFile(message_file)

  def _ExportMessageStrings(self, message_file, message_file_database):
    """Exports the message strings from a message file database.

    Args:
      message_file: the message file (instance of MessageFile).
      message_file_database: the message file database (instance of
                             Sqlite3DatabaseFile).
    """
    table_names = ['message_files', 'language_per_message_file']
    column_names = ['file_version', 'lcid', 'identifier']
    condition = (
        'message_files.message_file_key = '
        'language_per_message_file.message_file_key')

    for values in message_file_database.GetValues(
        table_names, column_names, condition):
      lcid = values['lcid']
      file_version = re.sub('\.', '_', values['file_version'])
      table_name = 'message_table_{0:s}_{1:s}'.format(lcid, file_version)

      message_file.AppendTable(lcid, values['identifier'], table_name)

    column_names = ['message_identifier', 'message_string']
    condition = ''

    for message_table in message_file.GetMessageTables():
      for table_name in message_table.tables:
        for values in message_file_database.GetValues(
            [table_name], column_names, condition):
          message_identifier = values['message_identifier']
          message_string = values['message_string']

          stored_message_string = message_table.message_strings.get(
              message_identifier, None)

          if not stored_message_string:
            message_table.message_strings[message_identifier] = message_string

          elif message_string != stored_message_string:
            logging.warning((
                u'Found duplicate alternating message string: {0:s} '
                u'in {1:s}.\nPrevious: {2:s}\nNew:{3:s}\n').format(
                    message_identifier, table_name, stored_message_string,
                    message_string))

            # TODO: is there a better way to determine which string to use.
            # E.g. latest build version?

  def _ExportStrings(self, message_file, message_file_database):
    """Exports the strings in a message file database.

    Args:
      message_file: the message file (instance of MessageFile).
      message_file_database: the message file database (instance of
                             Sqlite3DatabaseFile).
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

    table_names = ['event_log_providers']
    column_names = ['log_source', 'log_type']
    condition = ''

    # TODO: create a look up if the messages per event provider
    for values in event_provider_database.GetValues(
        table_names, column_names, condition):
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
        raise RuntimeError(u'Unsupported value type: {0:s}.'.format(type(value)))
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


class Sqlite3EventResourcesWriter(object):
  """Class to represent a sqlite3 Event Log resources writer."""

  def __init__(self):
    """Initializes the Event Log resources writer object."""
    super(Sqlite3EventResourcesWriter, self).__init__()
    self._database_file = Sqlite3DatabaseFile()

  def _GetMessageFileKey(self, message_file, message_filename):
    """Retrieves the key of a message file.

    Args:
      message_file: the message file (instance of MessageResourceFile).
      message_filename: the message filename.

    Returns:
      An integer containing the message file key or None if no such value.

    Raises:
      RuntimeError: if more than one value is found in the database.
    """
    table_names = ['message_files']
    column_names = ['message_file_key']
    condition = 'path = "{0:s}"'.format(message_filename)
    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return

    if number_of_values == 1:
      values = values_list[0]
      return values['message_file_key']

    raise RuntimeError(u'More than one value found in database.')

  def _WriteLanguage(self, message_file, message_file_key, language_identifier):
    """Writes a language.

    Args:
      message_file: the message file (instance of MessageResourceFile).
      message_file_key: the message file key.
      language_identifier: the language identifier (LCID).
    """
    table_name = 'language_per_message_file'
    column_names = ['lcid', 'message_file_key', 'identifier']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          'lcid TEXT', 'message_file_key INT', 'identifier TEXT']
      self._database_file.CreateTable(table_name, column_definitions)

    if not has_table:
      insert_values = True

    else:
      condition = 'lcid = "0x{0:08x}" AND message_file_key = "{1:d}"'.format(
          language_identifier, message_file_key)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 0:
        insert_values = True
      else:
        insert_values = False

    if insert_values:
      values = [
          '0x{0:08x}'.format(language_identifier), message_file_key,
          LANGUAGES.get(language_identifier, ['', ''])[0]]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteMessage(
      self, message_file, message_table, language_identifier,
      message_identifier, message_string, table_name, has_table):
    """Writes a message to a specific message table.

    Args:
      message_file: the message file (instance of MessageResourceFile).
      message_table: the message table (instance of pywrc.message_table).
      language_identifier: the language identifier (LCID).
      message_identifier: the message identifier.
      message_string: the message string.
      table_name: the name of the table.
      has_table: boolean value to indicate the table previously existed in
                 the database.
    """
    column_names = ['message_identifier', 'message_string']

    if not has_table:
      insert_values = True

    else:
      condition = 'message_identifier = "{0:s}"'.format(message_identifier)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 1:
        values = values_list[0]
        if message_string != values['message_string']:
          logging.warning((
              u'Message string mismatch for LCID: {0:s}, '
              u'file version: {1:s}, message identifier: {2:s}.\n'
              u'Found: {2:s}\nStored: {3:s}\n').format(
                  language_identifier, message_file.file_version,
                  message_identifier, message_string,
                  values['message_string']))

      elif number_of_values != 0:
        logging.warning((
             u'More than one message string found for LCID: {0:s}, '
             u'file version: {1:s}, message identifier: {2:s}.').format(
                 language_identifier, message_file.file_version,
                 message_identifier))

      # TODO: warn if new message has been found.
      insert_values = False

    if insert_values:
      values = [message_identifier, message_string]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteMessageFile(self, message_file):
    """Writes a message file.

    Args:
      message_file: the message file (instance of MessageResourceFile).
    """
    table_name = 'message_files'
    column_names = ['path']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          'message_file_key INTEGER PRIMARY KEY AUTOINCREMENT', 'path TEXT']
      self._database_file.CreateTable(table_name, column_definitions)

    if not has_table:
      insert_values = True

    else:
      condition = 'path = "{0:s}"'.format(message_file.windows_path)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 0:
        insert_values = True
      else:
        insert_values = False

    if insert_values:
      values = [message_file.windows_path]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteMessageTable(self, message_file, message_table):
    """Writes a message table for a specific language identifier.

    Args:
      message_file: the message file (instance of MessageResourceFile).
      message_table: the message table (instance of MessageTable).
    """
    if message_table.message_strings:
      message_file_key = self._GetMessageFileKey(
          message_file, message_file.windows_path)
      if message_file_key is None:
        logging.warning(u'Missing message file key for: {0:s}'.format(
            message_file.windows_path))

      self._WriteLanguage(message_file, message_file_key, message_file.lcid)

      table_name = u'message_table_{0:d}_{1:s}'.format(
          message_file_key, message_table.lcid)

      has_table = self._database_file.HasTable(table_name)
      if not has_table:
        column_definitions = ['message_identifier TEXT', 'message_string TEXT']
        self._database_file.CreateTable(table_name, column_definitions)

      for message_identifier, message_string in message_table.message_strings.iteritems():
        self._WriteMessage(
            message_file, message_table, message_table.lcid, message_identifier,
            message_string, table_name, has_table)

  def Close(self):
    """Closes the Event Log providers writer object."""
    self._database_file.Close()

  def Open(self, filename):
    """Opens the Event Log providers writer object.

    Args:
      filename: the filename of the database.

    Returns:
      A boolean containing True if successful or False if not.
    """
    self._database_file.Open(filename)

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
    """
    table_name = 'event_log_providers'
    column_names = ['log_source', 'log_type']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          'event_log_provider_key INTEGER PRIMARY KEY AUTOINCREMENT',
          'log_source TEXT', 'log_type TEXT']
      self._database_file.CreateTable(table_name, column_definitions)
      insert_values = True

    else:
      condition = 'log_source = "{0:s}" AND log_type = "{1:s}"'.format(
          event_log_provider.log_source, event_log_provider.log_type)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 0:
        insert_values = True
      else:
        # TODO: check if more than 1 result.
        insert_values = False

    if insert_values:
      values = [event_log_provider.log_source, event_log_provider.log_type]
      self._database_file.InsertValues(table_name, column_names, values)

  def WriteMessageFile(self, message_file):
    """Writes the Windows Message Resource file.

    Args:
      message_file: the message file (instance of MessageResourceFile).
    """
    self._WriteMessageFile(message_file)

    for message_table in message_file.GetMessageTables():
      # TODO track the languages in a table.
      self._WriteMessageTable(message_file, message_table)


class Sqlite3OutputWriter(object):
  """Class that defines a sqlite3 output writer."""

  def __init__(self, database_path):
    """Initializes the output writer object.

    Args:
      database_path: the path to the database file.
    """
    super(Sqlite3OutputWriter, self).__init__()
    self._database_path = database_path
    self._event_resources_writer = None

  def Close(self):
    """Closes the output writer object."""
    self._event_resources_writer.Close()
    self._event_resources_writer = None

  def Open(self):
    """Opens the output writer object.

    Returns:
      A boolean containing True if successful or False if not.
    """
    if os.path.isdir(self._database_path):
      return False

    self._event_resources_writer = Sqlite3EventResourcesWriter()
    self._event_resources_writer.Open(self._database_path)

    return True

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
    """
    self._event_resources_writer.WriteEventLogProvider(event_log_provider)

  def WriteMessageFile(self, message_file):
    """Writes the Windows Message Resource file.

    Args:
      message_file: the message file (instance of MessageFile).
    """
    self._event_resources_writer.WriteMessageFile(message_file)


class StdoutOutputWriter(object):
  """Class that defines a stdout output writer."""

  def _WriteMessageTable(self, message_table):
    """Writes the message table.

    Args:
      message_table: the message table (instance of MessageTable).
    """
    print('{0:s} (LCID: {1:s})'.format(
        message_table.language, message_table.lcid))
    print(u'')
    print(u'Message identifier\tMessage string')

    for identifier, string in message_table.message_strings.iteritems():
      string = re.sub(r'\n', '\\\\n', string)
      string = re.sub(r'\r', '\\\\r', string)
      string = re.sub(r'\t', '\\\\t', string)

      ouput_string = u'{0:s}\t{1:s}'.format(identifier, string)

      print(ouput_string.encode('utf8'))

    print(u'')

  def Open(self):
    """Opens the file.

    Returns:
      A boolean containing True if successful or False if not.
    """
    return True

  def Close(self):
    """Closes the file."""

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
    """
    print(u'Log type:\t{0:s}'.format(event_log_provider.log_type))
    print(u'Log source:\t{0:s}'.format(event_log_provider.log_source))

    # TODO: print more details.

  def WriteMessageFile(self, message_file):
    """Writes the Windows Message Resource file.

    Args:
      message_file: the message file (instance of MessageFile).
    """
    print(u'{0:s}'.format(message_file.name))
    print(u'Path:\t{0:s}'.format(message_file.windows_path))
    print(u'File version:\t{0:s}'.format(message_file.file_version))
    print(u'Product version:\t{0:s}'.format(message_file.product_version))

    for message_table in message_file.GetMessageTables():
      self._WriteMessageTable(message_table)


class AsciidocFileWriter(object):
  """Class to represent an asciidoc file writer."""
  # TODO: aparantly the filename should only contain 1 dot and end with .asciidoc

  def Open(self, filename):
    """Opens the file.

    Args:
      filename: the filename.

    Returns:
      A boolean containing True if successful or False if not.
    """
    # Using binary mode to make sure to write Unix end of lines.
    self._file = open(filename, 'wb')
    return True

  def Close(self):
    """Closes the file."""
    self._file.close()

  def WriteLine(self, line):
    """Writes a line."""
    self._file.write('{0:s}\n'.format(line))

  def WriteLines(self, lines):
    """Writes lines."""
    for line in lines:
      self.WriteLine(line)


class AsciidocOutputWriter(object):
  """Class that defines an asciidoc output writer."""

  def __init__(self, path):
    """Initializes the asciidoc output writer object.

    Args:
      path: the path to the directory containing the asciidoc files.
    """
    super(AsciidocOutputWriter, self).__init__()
    self._path = path

  def _WriteMessageTable(self, message_table, file_writer):
    """Writes the message table.

    Args:
      message_table: the message table (instance of MessageTable).
      file_writer: the file writer (instance of AsciidocFileWriter).
    """
    file_writer.WriteLines([
        u'=== {0:s} (LCID: {1:s})'.format(message_table.language, message_table.lcid),
        u'',
        u'[cols="1,5",options="header"]',
        u'|===',
        u'| Message identifier | Message string'])

    for identifier, string in message_table.message_strings.iteritems():
      string = re.sub(r'\n', '\\\\n', string)
      string = re.sub(r'\r', '\\\\r', string)
      string = re.sub(r'\t', '\\\\t', string)

      ouput_string = u'| {0:s} | {1:s}'.format(identifier, string)

      file_writer.WriteLine(ouput_string.encode('utf8'))

    file_writer.WriteLines([
        u'|===',
        u''])

  def Close(self):
    """Closes the output writer object."""
    pass

  def Open(self):
    """Opens the output writer object.

    Returns:
      A boolean containing True if successful or False if not.
    """
    if not os.path.isdir(self._path):
      return False
    return True

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
    """
    # TODO: implement.
    return

  def WriteMessageFile(self, message_file):
    """Writes the Windows Message Resource file.

    Args:
      message_file: the message file (instance of MessageFile).
    """
    file_writer = AsciidocFileWriter()
    path = os.path.join(
        self._path, u'{0:s}.asciidoc'.format(message_file.name))

    if file_writer.Open(path):

      file_writer.WriteLines([
          u'== {0:s}'.format(message_file.name),
          u'|===',
          u'| Path: | {0:s}'.format(message_file.windows_path),
          u'| File version: | {0:s}'.format(message_file.file_version),
          u'| Product version: | {0:s}'.format(message_file.product_version),
          u'|===',
          u''])

      for message_table in message_file.GetMessageTables():
        self._WriteMessageTable(message_table, file_writer)

      file_writer.Close()


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
      '--db', dest='database', action='store', metavar='winevt-rc.db',
      default=None, help='filename to write the sqlite3 database to.')

  args_parser.add_argument(
      '--wiki', dest='wiki', action='store', metavar='./winevt-kb.wiki/',
      default=None, help='path to write the wiki pages to.')

  # TODO: allow to set preferred language.

  options = args_parser.parse_args()

  if not options.source:
    print(u'Source value is missing.')
    print(u'')
    args_parser.print_help()
    print(u'')
    return False

  if not os.path.isdir(options.source):
    print(u'Invalid source.')
    print(u'')
    return False

  logging.basicConfig(
      level=logging.INFO, format=u'[%(levelname)s] %(message)s')

  if options.database:
    output_writer = Sqlite3OutputWriter(options.database)
  elif options.wiki:
    output_writer = AsciidocOutputWriter(options.wiki)
  else:
    output_writer = StdoutOutputWriter()

  if not output_writer.Open():
    print(u'Unable to open output writer.')
    print(u'')
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

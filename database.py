#!/usr/bin/python
# -*- coding: utf-8 -*-
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

import logging
import re

import sqlite3

import resources


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
    self.read_only = None

  def Close(self):
    """Closes the database file.

    Raises:
      RuntimeError: if the database is not opened.
    """
    if not self._connection:
      raise RuntimeError(u'Cannot close database not opened.')

    # We need to run commit or not all data is stored in the database.
    self._connection.commit()
    self._connection.close()

    self._connection = None
    self._cursor = None
    self.filename = None
    self.read_only = None

  def CreateTable(self, table_name, column_definitions):
    """Creates a table.

    Args:
      table_name: the table name.
      column_definitions: list of strings containing column definitions.

    Raises:
      RuntimeError: if the database is not opened or
                    if the database is in read-only mode.
    """
    if not self._connection:
      raise RuntimeError(u'Cannot create table database not opened.')

    if self.read_only:
      raise RuntimeError(u'Cannot create table database in read-only mode.')

    sql_query = u'CREATE TABLE {0:s} ( {1:s} )'.format(
        table_name, u', '.join(column_definitions))

    self._cursor.execute(sql_query)

  def HasTable(self, table_name):
    """Determines if a specific table exists.

    Args:
      table_name: the table name.

    Returns:
      True if the table exists, false otheriwse.

    Raises:
      RuntimeError: if the database is not opened.
    """
    if not self._connection:
      raise RuntimeError(
          u'Cannot determine if table exists database not opened.')

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

    Raises:
      RuntimeError: if the database is not opened.
    """
    if not self._connection:
      raise RuntimeError(u'Cannot retrieve values database not opened.')

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
      RuntimeError: if the database is not opened or
                    if the database is in read-only mode or
                    if an unsupported value type is encountered.
    """
    if not self._connection:
      raise RuntimeError(u'Cannot insert values database not opened.')

    if self.read_only:
      raise RuntimeError(u'Cannot insert values database in read-only mode.')

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
        raise RuntimeError(u'Unsupported value type: {0:s}.'.format(
            type(value)))
      sql_values.append(value)

    sql_query = u'INSERT INTO {0:s} ( {1:s} ) VALUES ( {2:s} )'.format(
        table_name, u', '.join(column_names), u', '.join(sql_values))

    self._cursor.execute(sql_query)

  def Open(self, filename, read_only=False):
    """Opens the database file.

    Args:
      filename: the filename of the database.
      read_only: optional boolean value to indicate the database should be
                 opened in read-only mode. The default is false. Since sqlite3
                 does not support a real read-only mode we fake it by only
                 permitting SELECT queries.

    Returns:
      A boolean containing True if successful or False if not.

    Raises:
      RuntimeError: if the database is already opened.
    """
    if self._connection:
      raise RuntimeError(u'Cannot open database already opened.')

    self.filename = filename
    self.read_only = read_only

    self._connection = sqlite3.connect(filename)
    if not self._connection:
      return False

    self._cursor = self._connection.cursor()
    if not self._cursor:
      return False

    return True


class Sqlite3DatabaseReader(object):
  """Class to represent a sqlite3 database reader."""

  def __init__(self):
    """Initializes the database reader object."""
    super(Sqlite3DatabaseReader, self).__init__()
    self._database_file = Sqlite3DatabaseFile()

  def Close(self):
    """Closes the database reader object."""
    self._database_file.Close()

  def Open(self, filename):
    """Opens the database reader object.

    Args:
      filename: the filename of the database.

    Returns:
      A boolean containing True if successful or False if not.
    """
    self._database_file.Open(filename, read_only=True)


class Sqlite3DatabaseWriter(object):
  """Class to represent a sqlite3 database writer."""

  def __init__(self):
    """Initializes the database writer object."""
    super(Sqlite3DatabaseWriter, self).__init__()
    self._database_file = Sqlite3DatabaseFile()

  def Close(self):
    """Closes the database writer object."""
    self._database_file.Close()

  def Open(self, filename):
    """Opens the database writer object.

    Args:
      filename: the filename of the database.

    Returns:
      A boolean containing True if successful or False if not.
    """
    self._database_file.Open(filename)


class Sqlite3EventProvidersDatabaseReader(Sqlite3DatabaseReader):
  """Class to represent a sqlite3 Event Log providers database reader."""

  def GetEventLogProviders(self):
    """Retrieves the Event Log providers.

    Yields:
      A tuple of an Event Log source and type.
    """
    table_names = ['event_log_providers']
    column_names = ['log_source', 'log_type']
    condition = ''

    for values in self._database_file.GetValues(
        table_names, column_names, condition):
      yield values['log_source'], values['log_type']

  def GetMessageFiles(self):
    """Retrieves the message filenames.

    Yields:
      A tuple of a message filename and the corresponding database filename.
    """
    table_names = ['message_files']
    column_names = ['message_filename', 'database_filename']
    condition = ''

    for values in self._database_file.GetValues(
        table_names, column_names, condition):
      yield values['message_filename'], values['database_filename']


class Sqlite3EventProvidersDatabaseWriter(Sqlite3DatabaseWriter):
  """Class to represent a sqlite3 Event Log providers database writer."""

  def _GetEventLogProviderKey(self, event_log_provider):
    """Retrieves the key of an Event Log provider.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).

    Returns:
      An integer containing the Event Log provider key or None if no such value.

    Raises:
      RuntimeError: if more than one value is found in the database.
    """
    table_names = ['event_log_providers']
    column_names = ['event_log_provider_key']
    condition = 'log_source = "{0:s}" AND log_type = "{1:s}"'.format(
        event_log_provider.log_source, event_log_provider.log_type)
    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return

    if number_of_values == 1:
      values = values_list[0]
      return values['event_log_provider_key']

    raise RuntimeError(u'More than one value found in database.')

  def _GetMessageFileKey(self, message_filename):
    """Retrieves the key of a message file.

    Args:
      message_filename: the message filename.

    Returns:
      An integer containing the message file key or None if no such value.

    Raises:
      RuntimeError: if more than one value is found in the database.
    """
    table_names = ['message_files']
    column_names = ['message_file_key']
    condition = 'message_filename = "{0:s}"'.format(message_filename)
    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return

    if number_of_values == 1:
      values = values_list[0]
      return values['message_file_key']

    raise RuntimeError(u'More than one value found in database.')

  def WriteMessageFilePerEventLogProvider(
      self, event_log_provider, message_filename):
    """Writes the message files used by an Event Log provider.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
      message_filename: the message filename.
    """
    table_name = 'message_file_per_event_log_provider'
    column_names = ['message_file_key', 'event_log_provider_key']

    event_log_provider_key = self._GetEventLogProviderKey(event_log_provider)
    if event_log_provider_key is None:
      logging.warning(u'Missing event log provider key for: {0:s}'.format(
          event_log_provider.log_source))

    message_file_key = self._GetMessageFileKey(message_filename)
    if message_file_key is None:
      logging.warning(u'Missing message file key for: {0:s}'.format(
          message_filename))

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          'message_file_key INTEGER', 'event_log_provider_key INTEGER']
      self._database_file.CreateTable(table_name, column_definitions)
      insert_values = True

    else:
      condition = (
          'message_file_key = {0:d} AND event_log_provider_key = {1:d}').format(
              message_file_key, event_log_provider_key)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 0:
        insert_values = True
      else:
        # TODO: check if more than 1 result.
        insert_values = False

    if insert_values:
      values = [message_file_key, event_log_provider_key]
      self._database_file.InsertValues(table_name, column_names, values)

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

  def WriteMessageFile(self, message_filename, database_filename):
    """Writes the Windows Message Resource file.

    Args:
      message_filename: the message filename.
      database_filename: the database filename.
    """
    table_name = 'message_files'
    column_names = ['message_filename', 'database_filename']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          'message_file_key INTEGER PRIMARY KEY AUTOINCREMENT',
          'message_filename TEXT', 'database_filename TEXT']
      self._database_file.CreateTable(table_name, column_definitions)
      insert_values = True

    else:
      condition = 'message_filename = "{0:s}"'.format(message_filename)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 0:
        insert_values = True
      else:
        # TODO: check if more than 1 result.
        insert_values = False

    if insert_values:
      values = [message_filename, database_filename]
      self._database_file.InsertValues(table_name, column_names, values)


class Sqlite3MessageFileDatabaseReader(Sqlite3DatabaseReader):
  """Class to represent a sqlite3 message file database reader."""

  def GetMessageTables(self):
    """Retrieves the message tables.

    Yields:
      A tuple of a language code identifier (LCID) and the message file
      file version.
    """
    table_names = ['message_files', 'message_table_languages']
    column_names = ['file_version', 'lcid', 'identifier']
    condition = (
        'message_files.message_file_key = '
        'message_table_languages.message_file_key')

    for values in self._database_file.GetValues(
        table_names, column_names, condition):
      yield values['lcid'], values['file_version']

  def GetMessages(self, lcid, file_version):
    """Retrieves the messages of a specific message table.

    Args:
      lcid: the language code identifier (LCID).
      file_version: the message file file version.

    Yields:
      A tuple of a message identifier and string.
    """
    table_name = 'message_table_{0:s}_{1:s}'.format(
        lcid, re.sub(r'\.', '_', file_version))
    column_names = ['message_identifier', 'message_string']
    condition = ''

    for values in self._database_file.GetValues(
        [table_name], column_names, condition):
      yield values['message_identifier'], values['message_string']

  def GetStringTables(self):
    """Retrieves the string tables.

    Yields:
      A tuple of a language code identifier (LCID) and the message file
      file version.
    """
    table_names = ['message_files', 'string_table_languages']
    column_names = ['file_version', 'lcid', 'identifier']
    condition = (
        'message_files.message_file_key = '
        'string_table_languages.message_file_key')

    for values in self._database_file.GetValues(
        table_names, column_names, condition):
      yield values['lcid'], values['file_version']

  def GetStrings(self, lcid, file_version):
    """Retrieves the strings of a specific string table.

    Args:
      lcid: the language code identifier (LCID).
      file_version: the message file file version.

    Yields:
      A tuple of a string identifier and string.
    """
    table_name = 'string_table_{0:s}_{1:s}'.format(
        lcid, re.sub(r'\.', '_', file_version))
    column_names = ['string_identifier', 'string']
    condition = ''

    for values in self._database_file.GetValues(
        [table_name], column_names, condition):
      yield values['string_identifier'], values['string']


class Sqlite3MessageFileDatabaseWriter(Sqlite3DatabaseWriter):
  """Class to represent a sqlite3 message file database writer."""

  def __init__(self, message_resource_file):
    """Initializes the message file database writer object.

    Args:
      message_resource_file: the message file (instance of MessageResourceFile).
    """
    super(Sqlite3MessageFileDatabaseWriter, self).__init__()
    self._message_resource_file = message_resource_file

  def _GetMessageFileKey(self, message_resource_file):
    """Retrieves the key of a message file.

    Args:
      message_resource_file: the message file (instance of MessageResourceFile).

    Returns:
      An integer containing the message file key or None if no such value.

    Raises:
      RuntimeError: if more than one value is found in the database.
    """
    table_names = ['message_files']
    column_names = ['message_file_key']
    condition = (
        'path = "{0:s}" AND file_version = "{1:s}" AND '
        'product_version = "{2:s}"').format(
            message_resource_file.windows_path,
            message_resource_file.file_version,
            message_resource_file.product_version)
    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return

    if number_of_values == 1:
      values = values_list[0]
      return values['message_file_key']

    raise RuntimeError(u'More than one value found in database.')

  def _WriteMessage(
      self, message_resource_file, message_table, language_identifier,
      message_index, table_name, has_table):
    """Writes a message to a specific message table.

    Args:
      message_resource_file: the message file (instance of MessageResourceFile).
      message_table: the message table (instance of pywrc.message_table).
      language_identifier: the language identifier (LCID).
      message_index: the message index.
      table_name: the name of the table.
      has_table: boolean value to indicate the table previously existed in
                 the database.
    """
    column_names = ['message_identifier', 'message_string']

    message_identifier = message_table.get_message_identifier(
        language_identifier, message_index)
    message_identifier = '0x{0:08x}'.format(message_identifier)

    message_string = message_table.get_string(
        language_identifier, message_index)

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
              u'Message string mismatch for LCID: 0x{0:08x}, '
              u'file version: {1:s}, message identifier: {2:s}.\n'
              u'Found: {2:s}\nStored: {3:s}\n').format(
                  language_identifier, message_resource_file.file_version,
                  message_identifier, message_string,
                  values['message_string']))

      elif number_of_values != 0:
        logging.warning((
             u'More than one message string found for LCID: 0x{0:08x}, '
             u'file version: {1:s}, message identifier: {2:s}.').format(
                 language_identifier, message_resource_file.file_version,
                 message_identifier))

      # TODO: warn if new message has been found.
      insert_values = False

    if insert_values:
      values = [message_identifier, message_string]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteMessageFile(self, message_resource_file):
    """Writes a message file.

    Args:
      message_resource_file: the message file (instance of MessageResourceFile).
    """
    table_name = 'message_files'
    column_names = ['path', 'file_version', 'product_version']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          'message_file_key INTEGER PRIMARY KEY AUTOINCREMENT',
          'path TEXT', 'file_version TEXT', 'product_version TEXT']
      self._database_file.CreateTable(table_name, column_definitions)

    if not has_table:
      insert_values = True

    else:
      condition = (
          'path = "{0:s}" AND file_version = "{1:s}" AND '
          'product_version = "{2:s}"').format(
              message_resource_file.windows_path,
              message_resource_file.file_version,
              message_resource_file.product_version)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 0:
        insert_values = True
      else:
        insert_values = False

    if insert_values:
      values = [
          message_resource_file.windows_path,
          message_resource_file.file_version,
          message_resource_file.product_version]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteMessageTable(
      self, message_resource_file, message_table, language_identifier):
    """Writes a message table for a specific language identifier.

    Args:
      message_resource_file: the message file (instance of MessageResourceFile).
      message_table: the message table (instance of pywrc.message_table).
      language_identifier: the language identifier (LCID).
    """
    number_of_messages = message_table.get_number_of_messages(
        language_identifier)

    if number_of_messages > 0:
      message_file_key = self._GetMessageFileKey(message_resource_file)
      if message_file_key is None:
        logging.warning(u'Missing message file key for: {0:s}'.format(
            message_resource_file.windows_path))

      self._WriteMessageTableLanguage(message_file_key, language_identifier)

      table_name = u'message_table_0x{0:08x}_{1:s}'.format(
          language_identifier, message_resource_file.file_version)
      table_name = re.sub(r'\.', '_', table_name)

      has_table = self._database_file.HasTable(table_name)
      if not has_table:
        column_definitions = ['message_identifier TEXT', 'message_string TEXT']
        self._database_file.CreateTable(table_name, column_definitions)

      for message_index in range(0, number_of_messages):
        self._WriteMessage(
            message_resource_file, message_table, language_identifier,
            message_index, table_name, has_table)

  def _WriteMessageTableLanguage(self, message_file_key, language_identifier):
    """Writes a message table language.

    Args:
      message_file_key: the message file key.
      language_identifier: the language identifier (LCID).
    """
    table_name = 'message_table_languages'
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
          resources.LANGUAGES.get(language_identifier, ['', ''])[0]]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteMessageTables(self):
    """Writes the message tables."""
    message_table = self._message_resource_file.GetMessageTableResource()
    try:
      number_of_languages = message_table.get_number_of_languages()
    except IOError as exception:
      number_of_languages = 0
      logging.warning(
          u'Unable to retrieve number of languages from: {0:s} '
          u'with error: {1:s}.'.format(self._message_resource_file, exception))

    if number_of_languages > 0:
      for language_identifier in message_table.language_identifiers:
        self._WriteMessageTable(
            self._message_resource_file, message_table, language_identifier)

  def _WriteString(
      self, message_resource_file, string_table, language_identifier,
      string_index, table_name, has_table):
    """Writes a string to a specific string table.

    Args:
      message_resource_file: the message file (instance of MessageResourceFile).
      string_table: the string table (instance of pywrc.strings).
      language_identifier: the language identifier (LCID).
      string_index: the string index.
      table_name: the name of the table.
      has_table: boolean value to indicate the table previously existed in
                 the database.
    """
    column_names = ['string_identifier', 'string']

    string_identifier = string_table.get_string_identifier(
        language_identifier, string_index)
    string_identifier = '0x{0:08x}'.format(string_identifier)

    string = string_table.get_string(language_identifier, string_index)

    if not has_table:
      insert_values = True

    else:
      condition = 'string_identifier = "{0:s}"'.format(string_identifier)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 1:
        values = values_list[0]
        if string != values['string']:
          logging.warning((
              u'String mismatch for LCID: 0x{0:08x}, '
              u'file version: {1:s}, string identifier: {2:s}.\n'
              u'Found: {2:s}\nStored: {3:s}\n').format(
                  language_identifier, message_resource_file.file_version,
                  string_identifier, string, values['string']))

      elif number_of_values != 0:
        logging.warning((
             u'More than one string found for LCID: 0x{0:08x}, '
             u'file version: {1:s}, string identifier: {2:s}.').format(
                 language_identifier, message_resource_file.file_version,
                 string_identifier))

      # TODO: warn if new string has been found.
      insert_values = False

    if insert_values:
      values = [string_identifier, string]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteStringTable(
      self, message_resource_file, string_table, language_identifier):
    """Writes a string table for a specific language identifier.

    Args:
      message_resource_file: the message file (instance of MessageResourceFile).
      string_table: the string table (instance of pywrc.strings).
      language_identifier: the language identifier (LCID).
    """
    number_of_strings = string_table.get_number_of_strings(
        language_identifier)

    if number_of_strings > 0:
      message_file_key = self._GetMessageFileKey(message_resource_file)
      if message_file_key is None:
        logging.warning(u'Missing message file key for: {0:s}'.format(
            message_resource_file.windows_path))

      self._WriteStringTableLanguage(message_file_key, language_identifier)

      table_name = u'string_table_0x{0:08x}_{1:s}'.format(
          language_identifier, message_resource_file.file_version)
      table_name = re.sub(r'\.', '_', table_name)

      has_table = self._database_file.HasTable(table_name)
      if not has_table:
        column_definitions = ['string_identifier TEXT', 'string TEXT']
        self._database_file.CreateTable(table_name, column_definitions)

      for string_index in range(0, number_of_strings):
        self._WriteString(
            message_resource_file, string_table, language_identifier,
            string_index, table_name, has_table)

  def _WriteStringTableLanguage(self, message_file_key, language_identifier):
    """Writes a string table language.

    Args:
      message_file_key: the message file key.
      language_identifier: the language identifier (LCID).
    """
    table_name = 'string_table_languages'
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
          resources.LANGUAGES.get(language_identifier, ['', ''])[0]]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteStringTables(self):
    """Writes the string tables."""
    string_table = self._message_resource_file.GetStringResource()
    if not string_table:
      return

    try:
      number_of_languages = string_table.get_number_of_languages()
    except IOError as exception:
      number_of_languages = 0
      logging.warning(
          u'Unable to retrieve number of languages from: {0:s} '
          u'with error: {1:s}.'.format(self._message_resource_file, exception))

    if number_of_languages > 0:
      for language_identifier in string_table.language_identifiers:
        self._WriteStringTable(
            self._message_resource_file, string_table, language_identifier)

  def WriteResources(self):
    """Writes the resources."""
    self._WriteMessageFile(self._message_resource_file)
    self._WriteMessageTables()
    # TODO: only write the string resources of Event Log parameter files.
    # self._WriteStringTables()


class Sqlite3ResourcesDatabaseWriter(Sqlite3DatabaseWriter):
  """Class to represent a sqlite3 Event Log resources database writer."""

  def _GetMessageFileKey(self, message_file):
    """Retrieves the key of a message file.

    Args:
      message_file: the message file (instance of MessageFile).

    Returns:
      An integer containing the message file key or None if no such value.

    Raises:
      RuntimeError: if more than one value is found in the database.
    """
    table_names = ['message_files']
    column_names = ['message_file_key']
    condition = 'path = "{0:s}"'.format(message_file.windows_path)
    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return

    if number_of_values == 1:
      values = values_list[0]
      return values['message_file_key']

    raise RuntimeError(u'More than one value found in database.')

  def _WriteMessage(
      self, message_file, language_identifier, message_identifier,
      message_string, table_name, has_table):
    """Writes a message to a specific message table.

    Args:
      message_file: the message file (instance of MessageFile).
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
      message_file: the message file (instance of MessageFile).
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
      message_file: the message file (instance of MessageFile).
      message_table: the message table (instance of MessageTable).
    """
    if message_table.message_strings:
      message_file_key = self._GetMessageFileKey(message_file)
      if message_file_key is None:
        logging.warning(u'Missing message file key for: {0:s}'.format(
            message_file.windows_path))

      table_name = u'message_table_{0:d}_{1:s}'.format(
          message_file_key, message_table.lcid)

      has_table = self._database_file.HasTable(table_name)
      if not has_table:
        column_definitions = ['message_identifier TEXT', 'message_string TEXT']
        self._database_file.CreateTable(table_name, column_definitions)

      message_strings = message_table.message_strings
      for message_identifier, message_string in message_strings.iteritems():
        self._WriteMessage(
            message_file, message_table.lcid, message_identifier,
            message_string, table_name, has_table)

      self._WriteMessageTableLanguage(message_file_key, message_table.lcid)

  def _WriteMessageTableLanguage(self, message_file_key, language_identifier):
    """Writes a message table language.

    Args:
      message_file_key: the message file key.
      language_identifier: the language identifier (LCID).
    """
    table_name = 'message_table_languages'
    column_names = ['lcid', 'message_file_key']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = ['lcid TEXT', 'message_file_key INT']
      self._database_file.CreateTable(table_name, column_definitions)

    if not has_table:
      insert_values = True

    else:
      condition = 'lcid = "{0:s}" AND message_file_key = "{1:d}"'.format(
          language_identifier, message_file_key)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 0:
        insert_values = True
      else:
        insert_values = False

    if insert_values:
      values = [language_identifier, message_file_key]
      self._database_file.InsertValues(table_name, column_names, values)

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
      message_file: the message file (instance of MessageFile).
    """
    self._WriteMessageFile(message_file)

    for message_table in message_file.GetMessageTables():
      # TODO track the languages in a table.
      self._WriteMessageTable(message_file, message_table)

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
        raise RuntimeError(u'Unsupported value type: {0:s}.'.format(
            type(value)))
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


class Sqlite3MessageFileDatabaseWriter(object):
  """Class to represent a sqlite3 message file database writer."""

  def __init__(self, message_file):
    """Initializes the message file database writer object.

    Args:
      message_file: the message file (instance of MessageResourceFile).
    """
    super(Sqlite3MessageFileDatabaseWriter, self).__init__()
    self._database_file = Sqlite3DatabaseFile()
    self._message_file = message_file

  def _GetMessageFileKey(self, message_file):
    """Retrieves the key of a message file.

    Args:
      message_file: the message file (instance of MessageResourceFile).

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
            message_file.windows_path, message_file.file_version,
            message_file.product_version)
    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return

    if number_of_values == 1:
      values = values_list[0]
      return values['message_file_key']

    raise RuntimeError(u'More than one value found in database.')

  def _WriteLanguage(self, message_file_key, language_identifier):
    """Writes a language.

    Args:
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
          resources.LANGUAGES.get(language_identifier, ['', ''])[0]]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteMessage(
      self, message_file, message_table, language_identifier, message_index,
      table_name, has_table):
    """Writes a message to a specific message table.

    Args:
      message_file: the message file (instance of MessageResourceFile).
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
                  language_identifier, message_file.file_version,
                  message_identifier, message_string,
                  values['message_string']))

      elif number_of_values != 0:
        logging.warning((
             u'More than one message string found for LCID: 0x{0:08x}, '
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
              message_file.windows_path, message_file.file_version,
              message_file.product_version)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 0:
        insert_values = True
      else:
        insert_values = False

    if insert_values:
      values = [
          message_file.windows_path, message_file.file_version,
          message_file.product_version]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteMessageTable(
      self, message_file, message_table, language_identifier):
    """Writes a message table for a specific language identifier.

    Args:
      message_file: the message file (instance of MessageResourceFile).
      message_table: the message table (instance of pywrc.message_table).
      language_identifier: the language identifier (LCID).
    """
    number_of_messages = message_table.get_number_of_messages(
        language_identifier)

    if number_of_messages > 0:
      message_file_key = self._GetMessageFileKey(message_file)
      if message_file_key is None:
        logging.warning(u'Missing message file key for: {0:s}'.format(
            message_file.windows_path))

      self._WriteLanguage(message_file_key, language_identifier)

      table_name = u'message_table_0x{0:08x}_{1:s}'.format(
          language_identifier, message_file.file_version)
      table_name = re.sub(r'\.', '_', table_name)

      has_table = self._database_file.HasTable(table_name)
      if not has_table:
        column_definitions = ['message_identifier TEXT', 'message_string TEXT']
        self._database_file.CreateTable(table_name, column_definitions)

      for message_index in range(0, number_of_messages):
        self._WriteMessage(
            message_file, message_table, language_identifier, message_index,
            table_name, has_table)

  def Close(self):
    """Closes the message file writer object."""
    self._database_file.Close()

  def Open(self, filename):
    """Opens the message file writer object.

    Args:
      filename: the filename of the database.

    Returns:
      A boolean containing True if successful or False if not.
    """
    self._database_file.Open(filename)

  def WriteMessageTables(self):
    """Writes the message tables."""
    self._WriteMessageFile(self._message_file)

    message_table = self._message_file.GetMessageTableResource()
    try:
      number_of_languages = message_table.get_number_of_languages()
    except IOError as exception:
      number_of_languages = 0
      logging.warning(
          u'Unable to retrieve number of languages from: {0:s} '
          u'with error: {1:s}.'.format(self._message_file, exception))

    if number_of_languages > 0:
      for language_identifier in message_table.language_identifiers:
        # TODO track the languages in a table.
        self._WriteMessageTable(
            self._message_file, message_table, language_identifier)


class Sqlite3ResourcesDatabaseWriter(object):
  """Class to represent a sqlite3 Event Log resources database writer."""

  def __init__(self):
    """Initializes the Event Log resources database writer object."""
    super(Sqlite3ResourcesDatabaseWriter, self).__init__()
    self._database_file = Sqlite3DatabaseFile()

  def _GetMessageFileKey(self, message_file):
    """Retrieves the key of a message file.

    Args:
      message_file: the message file (instance of MessageResourceFile).

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

  def _WriteLanguage(self, message_file_key, language_identifier):
    """Writes a language.

    Args:
      message_file_key: the message file key.
      language_identifier: the language identifier (LCID).
    """
    table_name = 'language_per_message_file'
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

  def _WriteMessage(
      self, message_file, language_identifier, message_identifier,
      message_string, table_name, has_table):
    """Writes a message to a specific message table.

    Args:
      message_file: the message file (instance of MessageResourceFile).
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

      self._WriteLanguage(message_file_key, message_table.lcid)

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

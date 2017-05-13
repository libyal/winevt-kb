# -*- coding: utf-8 -*-
"""Classes to read from and write to SQLite databases."""

import difflib
import logging
import re

try:
  from pysqlite2 import dbapi2 as sqlite3
except ImportError:
  import sqlite3

from winevtrc import definitions
from winevtrc import errors
from winevtrc import py2to3
from winevtrc import resources


class SQLite3DatabaseFile(object):
  """Class that defines a sqlite3 database file."""

  _HAS_TABLE_QUERY = (
      u'SELECT name FROM sqlite_master '
      u'WHERE type = "table" AND name = "{0:s}"')

  def __init__(self):
    """Initializes the database file."""
    super(SQLite3DatabaseFile, self).__init__()
    self._connection = None
    self._cursor = None
    self.filename = None
    self.read_only = None

  def Close(self):
    """Closes the database file.

    Raises:
      IOError: if the database is not opened.
    """
    if not self._connection:
      raise IOError(u'Cannot close database not opened.')

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
      table_name (str): table name.
      column_definitions (list[str]): column definitions.

    Raises:
      BackendError: if the database back-end raises an exception.
      IOError: if the database is not opened or
          if the database is in read-only mode.
    """
    if not self._connection:
      raise IOError(u'Cannot create table database not opened.')

    if self.read_only:
      raise IOError(u'Cannot create table database in read-only mode.')

    sql_query = u'CREATE TABLE {0:s} ( {1:s} )'.format(
        table_name, u', '.join(column_definitions))

    try:
      self._cursor.execute(sql_query)
    except sqlite3.OperationalError as exception:
      raise errors.BackendError(exception)

  def GetValues(self, table_names, column_names, condition):
    """Retrieves values from a table.

    Args:
      table_names (list[str]): table names.
      column_names (list[str]): column names.
      condition (str): condition.

    Returns:
      generator: values generator.

    Raises:
      BackendError: if the database back-end raises an exception.
      IOError: if the database is not opened.
    """
    def _GetValues(cursor, table_names, column_names, condition):
      """Values generator function.

      Args:
        cursor (sqlite3.Cursor): SQLite database cursor.
        table_names (list[str]): table names.
        column_names (list[str]): column names.
        condition (str): condition.

      Yields:
        dict[str, object]: value.
      """
      if condition:
        condition = u' WHERE {0:s}'.format(condition)

      sql_query = u'SELECT {1:s} FROM {0:s}{2:s}'.format(
          u', '.join(table_names), u', '.join(column_names), condition)

      try:
        cursor.execute(sql_query)
      except sqlite3.OperationalError as exception:
        raise errors.BackendError(exception)

      for row in cursor:
        values = {}
        for column_index in range(0, len(column_names)):
          column_name = column_names[column_index]
          values[column_name] = row[column_index]
        yield values

    if not self._connection:
      raise IOError(u'Cannot retrieve values database not opened.')

    return _GetValues(self._cursor, table_names, column_names, condition)

  def HasTable(self, table_name):
    """Determines if a specific table exists.

    Args:
      table_name (str): table name.

    Returns:
      bool: True if the table exists, false otheriwse.

    Raises:
      BackendError: if the database back-end raises an exception.
      IOError: if the database is not opened.
    """
    if not self._connection:
      raise IOError(u'Cannot determine if table exists database not opened.')

    sql_query = self._HAS_TABLE_QUERY.format(table_name)

    try:
      self._cursor.execute(sql_query)

      if self._cursor.fetchone():
        has_table = True
      else:
        has_table = False

    except sqlite3.OperationalError as exception:
      raise errors.BackendError(exception)

    return has_table

  def InsertValues(self, table_name, column_names, values):
    """Inserts values into a table.

    Args:
      table_name (str): table name.
      column_names (list[str]): column names.
      values (list[str]): values formatted as a string.

    Raises:
      BackendError: if the database back-end raises an exception.
      IOError: if the database is not opened or
          if the database is in read-only mode or
          if an unsupported value type is encountered.
    """
    if not self._connection:
      raise IOError(u'Cannot insert values database not opened.')

    if self.read_only:
      raise IOError(u'Cannot insert values database in read-only mode.')

    if not values:
      return

    sql_values = []
    for value in values:
      # TODO: handle bool.
      if isinstance(value, py2to3.STRING_TYPES):
        # In sqlite3 the double quote is escaped with a second double quote.
        value = u'"{0:s}"'.format(re.sub('"', '""', value))
      elif isinstance(value, py2to3.INTEGER_TYPES):
        value = u'{0:d}'.format(value)
      elif isinstance(value, float):
        value = u'{0:f}'.format(value)
      elif value is None:
        value = u'NULL'
      else:
        raise IOError(u'Unsupported value type: {0!s}.'.format(type(value)))
      sql_values.append(value)

    sql_query = u'INSERT INTO {0:s} ( {1:s} ) VALUES ( {2:s} )'.format(
        table_name, u', '.join(column_names), u', '.join(sql_values))

    try:
      self._cursor.execute(sql_query)
    except sqlite3.OperationalError as exception:
      raise errors.BackendError(exception)

  def Open(self, filename, read_only=False):
    """Opens the database file.

    Args:
      filename (str): filename of the database.
      read_only (Optional[bool]): True if the database should be opened in
          read-only mode. Since sqlite3 does not support a real read-only
          mode we fake it by only permitting SELECT queries.

    Returns:
      bool: True if successful or False if not.

    Raises:
      BackendError: if the database back-end raises an exception.
      IOError: if the database is already opened.
    """
    if self._connection:
      raise IOError(u'Cannot open database already opened.')

    self.filename = filename
    self.read_only = read_only

    self._connection = sqlite3.connect(filename)
    if not self._connection:
      return False

    try:
      self._cursor = self._connection.cursor()
    except sqlite3.OperationalError as exception:
      raise errors.BackendError(exception)

    if not self._cursor:
      return False

    return True


class Sqlite3DatabaseReader(object):
  """Class to represent a sqlite3 database reader."""

  def __init__(self):
    """Initializes the database reader."""
    super(Sqlite3DatabaseReader, self).__init__()
    self._database_file = SQLite3DatabaseFile()

  def Close(self):
    """Closes the database reader."""
    self._database_file.Close()

  def Open(self, filename):
    """Opens the database reader.

    Args:
      filename (str): filename of the database.

    Returns:
      bool: True if successful or False if not.
    """
    return self._database_file.Open(filename, read_only=True)


class Sqlite3DatabaseWriter(object):
  """Class to represent a sqlite3 database writer."""

  def __init__(self):
    """Initializes the database writer."""
    super(Sqlite3DatabaseWriter, self).__init__()
    self._database_file = SQLite3DatabaseFile()

  def Close(self):
    """Closes the database writer."""
    self._database_file.Close()

  def Open(self, filename):
    """Opens the database writer.

    Args:
      filename (str): filename of the database.

    Returns:
      bool: True if successful or False if not.
    """
    self._database_file.Open(filename)


class EventProvidersSqlite3DatabaseReader(Sqlite3DatabaseReader):
  """Class to represent an Event Log providers sqlite3 database reader."""

  def _GetMessageFilenames(self, log_source, message_file_type):
    """Retrieves the message filenames of a specific Event Log provider.

    Args:
      log_source (str): source of the Event Log provider.
      message_file_type (str): message file type.

    Returns:
      list[str]: message filenames.
    """
    table_names = [
        u'event_log_providers', u'message_file_per_event_log_provider',
        u'message_files']
    column_names = [u'message_files.message_filename']
    condition = (
        u'{0:s}.log_source == "{3:s}" AND '
        u'{1:s}.message_file_type == "{4:s}" AND '
        u'{0:s}.event_log_provider_key == {1:s}.event_log_provider_key AND '
        u'{1:s}.message_file_key == {2:s}.message_file_key').format(
            u'event_log_providers', u'message_file_per_event_log_provider',
            u'message_files', log_source, message_file_type)

    message_filenames = []
    for values in self._database_file.GetValues(
        table_names, column_names, condition):
      message_filename = values[u'message_files.message_filename']
      message_filenames.append(message_filename)

    return message_filenames

  def GetEventLogProviders(self):
    """Retrieves the Event Log providers.

    Yields:
      EventLogProvider: event log provider.
    """
    table_names = [u'event_log_providers']
    column_names = [u'log_source', u'log_type', u'provider_guid']
    condition = u''

    event_log_providers = []
    for values in self._database_file.GetValues(
        table_names, column_names, condition):
      event_log_provider = resources.EventLogProvider(
          values[u'log_type'], values[u'log_source'], values[u'provider_guid'])
      event_log_providers.append(event_log_provider)

    for event_log_provider in event_log_providers:
      message_filenames = self._GetMessageFilenames(
          event_log_provider.log_source,
          definitions.MESSAGE_FILE_TYPE_CATEGORY)
      event_log_provider.SetCategoryMessageFilenames(message_filenames)

      message_filenames = self._GetMessageFilenames(
          event_log_provider.log_source, definitions.MESSAGE_FILE_TYPE_EVENT)
      event_log_provider.SetEventMessageFilenames(message_filenames)

      message_filenames = self._GetMessageFilenames(
          event_log_provider.log_source,
          definitions.MESSAGE_FILE_TYPE_PARAMETER)
      event_log_provider.SetParameterMessageFilenames(message_filenames)

      yield event_log_provider

  def GetMessageFiles(self):
    """Retrieves the message filenames.

    Yields:
      tuple[str, str]: message filename and corresponding database filename.
    """
    table_names = [u'message_files']
    column_names = [u'message_filename', u'database_filename']
    condition = u''

    for values in self._database_file.GetValues(
        table_names, column_names, condition):
      yield values[u'message_filename'], values[u'database_filename']


class EventProvidersSqlite3DatabaseWriter(Sqlite3DatabaseWriter):
  """Class to represent an Event Log providers sqlite3 database writer."""

  def _GetEventLogProviderKey(self, event_log_provider):
    """Retrieves the key of an Event Log provider.

    Args:
      event_log_provider (EventLogProvider): event log provider.

    Returns:
      int: Event Log provider key or None if no such value.

    Raises:
      IOError: if more than one value is found in the database.
    """
    table_names = [u'event_log_providers']
    column_names = [u'event_log_provider_key']
    condition = u'log_source = "{0:s}" AND log_type = "{1:s}"'.format(
        event_log_provider.log_source, event_log_provider.log_type)
    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return

    if number_of_values == 1:
      values = values_list[0]
      return values[u'event_log_provider_key']

    raise IOError(u'More than one value found in database.')

  def _GetMessageFileKey(self, message_filename):
    """Retrieves the key of a message file.

    Args:
      message_filename (str): message filename.

    Returns:
      int: message file key or None if no such value.

    Raises:
      IOError: if more than one value is found in the database.
    """
    table_names = [u'message_files']
    column_names = [u'message_file_key']
    condition = u'LOWER(message_filename) = LOWER("{0:s}")'.format(
        message_filename)
    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return

    if number_of_values == 1:
      values = values_list[0]
      return values[u'message_file_key']

    raise IOError(u'More than one value found in database.')

  def WriteMessageFilesPerEventLogProvider(
      self, event_log_provider, message_filename, message_file_type):
    """Writes the message files used by an Event Log provider.

    Args:
      event_log_provider (EventLogProvider): event log provider.
      message_filename (str): message filename.
      message_file_type (str): message file type.
    """
    table_name = u'message_file_per_event_log_provider'
    column_names = [
        u'message_file_key', u'message_file_type', u'event_log_provider_key']

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
          u'message_file_key INTEGER', u'message_file_type TEXT',
          u'event_log_provider_key INTEGER']
      self._database_file.CreateTable(table_name, column_definitions)
      insert_values = True

    else:
      condition = (
          u'message_file_key = {0:d} AND message_file_type = "{1:s}" AND '
          u'event_log_provider_key = {2:d}').format(
              message_file_key, message_file_type, event_log_provider_key)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 0:
        insert_values = True
      else:
        # TODO: check if more than 1 result.
        insert_values = False

    if insert_values:
      values = [message_file_key, message_file_type, event_log_provider_key]
      self._database_file.InsertValues(table_name, column_names, values)

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider (EventLogProvider): event log provider.
    """
    table_name = u'event_log_providers'
    column_names = [u'log_source', u'log_type', u'provider_guid']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          u'event_log_provider_key INTEGER PRIMARY KEY AUTOINCREMENT',
          u'log_source TEXT', u'log_type TEXT', u'provider_guid TEXT']
      self._database_file.CreateTable(table_name, column_definitions)
      insert_values = True

    else:
      condition = u'log_source = "{0:s}" AND log_type = "{1:s}"'.format(
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
      values = [
          event_log_provider.log_source, event_log_provider.log_type,
          event_log_provider.provider_guid]
      self._database_file.InsertValues(table_name, column_names, values)

  def WriteMessageFile(self, message_filename, database_filename):
    """Writes the Windows Message Resource file.

    Args:
      message_filename (str): message filename.
      database_filename (str): database filename.
    """
    table_name = u'message_files'
    column_names = [u'message_filename', u'database_filename']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          u'message_file_key INTEGER PRIMARY KEY AUTOINCREMENT',
          u'message_filename TEXT', u'database_filename TEXT']
      self._database_file.CreateTable(table_name, column_definitions)
      insert_values = True

    else:
      condition = u'LOWER(message_filename) = LOWER("{0:s}")'.format(
          message_filename)
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


class MessageFileSqlite3DatabaseReader(Sqlite3DatabaseReader):
  """Class to represent a message file sqlite3 database reader."""

  def GetMessageTables(self):
    """Retrieves the message tables.

    Yields:
      tuple[int, str]: language code identifier (LCID) and the message file
          version.
    """
    table_names = [u'message_files', u'message_table_languages']
    column_names = [u'file_version', u'lcid', u'identifier']
    condition = (
        u'message_files.message_file_key = '
        u'message_table_languages.message_file_key')

    for values in self._database_file.GetValues(
        table_names, column_names, condition):
      yield values[u'lcid'], values[u'file_version']

  def GetMessages(self, lcid, file_version):
    """Retrieves the messages of a specific message table.

    Args:
      lcid (str): language code identifier (LCID).
      file_version (str): message file file version.

    Yields:
      tuple[int, str]: message identifier and message string.
    """
    table_name = u'message_table_{0:s}'.format(lcid)
    if file_version:
      table_name = u'{0:s}_{1:s}'.format(table_name, file_version)
      table_name = re.sub(r'\.', r'_', table_name)

    column_names = [u'message_identifier', u'message_string']
    condition = u''

    for values in self._database_file.GetValues(
        [table_name], column_names, condition):
      yield values[u'message_identifier'], values[u'message_string']

  def GetStringTables(self):
    """Retrieves the string tables.

    Yields:
      tuple[int, str]: language code identifier (LCID) and the message file
          version.
    """
    table_names = [u'message_files', u'string_table_languages']
    column_names = [u'file_version', u'lcid', u'identifier']
    condition = (
        u'message_files.message_file_key = '
        u'string_table_languages.message_file_key')

    for values in self._database_file.GetValues(
        table_names, column_names, condition):
      yield values[u'lcid'], values[u'file_version']

  def GetStrings(self, lcid, file_version):
    """Retrieves the strings of a specific string table.

    Args:
      lcid (str): language code identifier (LCID).
      file_version (str): message file file version.

    Yields:
      tuple[int, str]: string identifier and string.
    """
    table_name = u'string_table_{0:s}_{1:s}'.format(
        lcid, re.sub(r'\.', '_', file_version))
    column_names = [u'string_identifier', u'string']
    condition = u''

    for values in self._database_file.GetValues(
        [table_name], column_names, condition):
      yield values[u'string_identifier'], values[u'string']


class MessageFileSqlite3DatabaseWriter(Sqlite3DatabaseWriter):
  """Class to represent a message file sqlite3 database writer."""

  def __init__(self, message_resource_file):
    """Initializes the message file database writer.

    Args:
      message_resource_file (MessageResourceFile): message resource file.
    """
    super(MessageFileSqlite3DatabaseWriter, self).__init__()
    self._message_resource_file = message_resource_file

  def _GetMessageFileKey(self, message_resource_file):
    """Retrieves the key of a message file.

    Args:
      message_resource_file (MessageResourceFile): message resource file.

    Returns:
      int: message file key or None if no such value.

    Raises:
      IOError: if more than one value is found in the database.
    """
    table_names = [u'message_files']
    column_names = [u'message_file_key']
    condition = u'LOWER(path) = LOWER("{0:s}")'.format(
        message_resource_file.windows_path)

    if message_resource_file.file_version:
      condition = u'{0:s} AND file_version = "{1:s}"'.format(
          condition, message_resource_file.file_version)

    if message_resource_file.product_version:
      condition = u'{0:s} AND product_version = "{1:s}"'.format(
          condition, message_resource_file.product_version)

    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return

    if number_of_values == 1:
      values = values_list[0]
      return values[u'message_file_key']

    raise IOError(u'More than one value found in database.')

  def _WriteMessage(
      self, message_resource_file, message_table, language_identifier,
      message_index, table_name, has_table):
    """Writes a message to a specific message table.

    Args:
      message_resource_file (MessageResourceFile): message resource file.
      message_table (pywrc.message_table): message table resource.
      language_identifier (int): language identifier (LCID).
      message_index (int): message index.
      table_name (str): name of the table.
      has_table (bool): True if the table previously existed in the database.
    """
    column_names = [u'message_identifier', u'message_string']

    message_identifier = message_table.get_message_identifier(
        language_identifier, message_index)
    message_identifier = u'0x{0:08x}'.format(message_identifier)

    message_string = message_table.get_string(
        language_identifier, message_index)

    if not has_table:
      insert_values = True

    else:
      condition = u'message_identifier = "{0:s}"'.format(message_identifier)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 1:
        values = values_list[0]
        if message_string != values[u'message_string']:
          differ = difflib.Differ()
          diff_list = list(differ.compare(
              [values[u'message_string']], [message_string]))
          logging.warning((
              u'Message string mismatch for LCID: 0x{0:08x}, '
              u'file version: {1:s}, message identifier: {2:s}.\n'
              u'{3:s}\n').format(
                  language_identifier, message_resource_file.file_version,
                  message_identifier, u'\n'.join(diff_list)))

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
      message_resource_file (MessageResourceFile): message resource file.
    """
    table_name = u'message_files'
    column_names = [u'path', u'file_version', u'product_version']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          u'message_file_key INTEGER PRIMARY KEY AUTOINCREMENT',
          u'path TEXT', u'file_version TEXT', u'product_version TEXT']
      self._database_file.CreateTable(table_name, column_definitions)

    if not has_table:
      insert_values = True

    else:
      condition = u'LOWER(path) = LOWER("{0:s}")'.format(
          message_resource_file.windows_path)

      if message_resource_file.file_version:
        condition = u'{0:s} AND file_version = "{1:s}"'.format(
            condition, message_resource_file.file_version)

      if message_resource_file.product_version:
        condition = u'{0:s} AND product_version = "{1:s}"'.format(
            condition, message_resource_file.product_version)

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
      message_resource_file (MessageResourceFile): message resource file.
      message_table (pywrc.message_table): message table resource.
      language_identifier (int): language identifier (LCID).
    """
    number_of_messages = message_table.get_number_of_messages(
        language_identifier)

    if number_of_messages > 0:
      message_file_key = self._GetMessageFileKey(message_resource_file)
      if message_file_key is None:
        logging.warning(u'Missing message file key for: {0:s}'.format(
            message_resource_file.windows_path))
      else:
        self._WriteMessageTableLanguage(message_file_key, language_identifier)

      table_name = u'message_table_0x{0:08x}'.format(language_identifier)
      if message_resource_file.file_version:
        table_name = u'{0:s}_{1:s}'.format(
            table_name, message_resource_file.file_version)
        table_name = re.sub(r'\.', r'_', table_name)

      has_table = self._database_file.HasTable(table_name)
      if not has_table:
        column_definitions = [
            u'message_identifier TEXT', u'message_string TEXT']
        self._database_file.CreateTable(table_name, column_definitions)

      for message_index in range(0, number_of_messages):
        self._WriteMessage(
            message_resource_file, message_table, language_identifier,
            message_index, table_name, has_table)

  def _WriteMessageTableLanguage(self, message_file_key, language_identifier):
    """Writes a message table language.

    Args:
      message_file_key (int): message file key.
      language_identifier (int): language identifier (LCID).
    """
    table_name = u'message_table_languages'
    column_names = [u'lcid', u'message_file_key', u'identifier']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          u'lcid TEXT', u'message_file_key INT', u'identifier TEXT']
      self._database_file.CreateTable(table_name, column_definitions)

    if not has_table:
      insert_values = True

    else:
      condition = u'lcid = "0x{0:08x}" AND message_file_key = "{1:d}"'.format(
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
          u'0x{0:08x}'.format(language_identifier), message_file_key,
          definitions.LANGUAGES.get(language_identifier, [u'', u''])[0]]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteMessageTables(self):
    """Writes the message tables."""
    message_table = self._message_resource_file.GetMessageTableResource()
    try:
      number_of_languages = message_table.get_number_of_languages()
    except IOError as exception:
      number_of_languages = 0
      logging.warning((
          u'Unable to retrieve number of languages from: {0:s} '
          u'with error: {1:s}.').format(self._message_resource_file, exception))

    if number_of_languages > 0:
      for language_identifier in message_table.language_identifiers:
        self._WriteMessageTable(
            self._message_resource_file, message_table, language_identifier)

  def _WriteString(
      self, message_resource_file, string_table, language_identifier,
      string_index, table_name, has_table):
    """Writes a string to a specific string table.

    Args:
      message_resource_file (MessageResourceFile): message resource file.
      string_table (pywrc.strings): string table.
      language_identifier (int): language identifier (LCID).
      string_index (int): string index.
      table_name (str): name of the table.
      has_table (bool): True if the table previously existed in the database.
    """
    column_names = [u'string_identifier', u'string']

    string_identifier = string_table.get_string_identifier(
        language_identifier, string_index)
    string_identifier = u'0x{0:08x}'.format(string_identifier)

    string = string_table.get_string(language_identifier, string_index)

    if not has_table:
      insert_values = True

    else:
      condition = u'string_identifier = "{0:s}"'.format(string_identifier)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 1:
        values = values_list[0]
        if string != values[u'string']:
          logging.warning((
              u'String mismatch for LCID: 0x{0:08x}, '
              u'file version: {1:s}, string identifier: {2:s}.\n'
              u'Found: {3:s}\nStored: {4:s}\n').format(
                  language_identifier, message_resource_file.file_version,
                  string_identifier, string, values[u'string']))

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
      message_resource_file (MessageResourceFile): message resource file.
      string_table (pywrc.strings): string table.
      language_identifier (int): language identifier (LCID).
    """
    number_of_strings = string_table.get_number_of_strings(
        language_identifier)

    if number_of_strings > 0:
      message_file_key = self._GetMessageFileKey(message_resource_file)
      if message_file_key is None:
        logging.warning(u'Missing message file key for: {0:s}'.format(
            message_resource_file.windows_path))

      self._WriteStringTableLanguage(message_file_key, language_identifier)

      table_name = u'message_table_0x{0:08x}'.format(language_identifier)
      if message_resource_file.file_version:
        table_name = u'{0:s}_{1:s}'.format(
            table_name, message_resource_file.file_version)
        table_name = re.sub(r'\.', r'_', table_name)

      has_table = self._database_file.HasTable(table_name)
      if not has_table:
        column_definitions = [u'string_identifier TEXT', u'string TEXT']
        self._database_file.CreateTable(table_name, column_definitions)

      for string_index in range(0, number_of_strings):
        self._WriteString(
            message_resource_file, string_table, language_identifier,
            string_index, table_name, has_table)

  def _WriteStringTableLanguage(self, message_file_key, language_identifier):
    """Writes a string table language.

    Args:
      message_file_key (int): message file key.
      language_identifier (int): language identifier (LCID).
    """
    table_name = u'string_table_languages'
    column_names = [u'lcid', u'message_file_key', u'identifier']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          u'lcid TEXT', u'message_file_key INT', u'identifier TEXT']
      self._database_file.CreateTable(table_name, column_definitions)

    if not has_table:
      insert_values = True

    else:
      condition = u'lcid = "0x{0:08x}" AND message_file_key = "{1:d}"'.format(
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
          u'0x{0:08x}'.format(language_identifier), message_file_key,
          definitions.LANGUAGES.get(language_identifier, [u'', u''])[0]]
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
      logging.warning((
          u'Unable to retrieve number of languages from: {0:s} '
          u'with error: {1:s}.').format(self._message_resource_file, exception))

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


class ResourcesSqlite3DatabaseReader(Sqlite3DatabaseReader):
  """Class to represent an Event Log resources sqlite3 database reader."""

  def _GetEventLogProviderKey(self, log_source):
    """Retrieves the Event Log provider key.

    Args:
      log_source (str): Event Log source.

    Returns:
      int: An Event Log provider key or None if not available.

    Raises:
      IOError: if more than one value is found in the database.
    """
    table_names = [u'event_log_providers']
    column_names = [u'event_log_provider_key']
    condition = u'log_source == "{0:s}"'.format(log_source)

    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return

    elif number_of_values == 1:
      values = values_list[0]
      return values[u'event_log_provider_key']

    raise IOError(u'More than one value found in database.')

  def _GetMessage(self, message_file_key, lcid, message_identifier):
    """Retrieves a specific message from a specific message table.

    Args:
      message_file_key (int): message file key.
      lcid (int): language code identifier (LCID).
      message_identifier (int): message identifier.

    Returns:
      The message string or None if not available.

    Raises:
      IOError: if more than one value is found in the database.
    """
    table_name = u'message_table_{0:d}_0x{1:08x}'.format(message_file_key, lcid)

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      return

    column_names = [u'message_string']
    condition = u'message_identifier == "0x{0:08x}"'.format(message_identifier)

    values = list(self._database_file.GetValues(
        [table_name], column_names, condition))

    number_of_values = len(values)
    if number_of_values == 0:
      return

    elif number_of_values == 1:
      return values[0][u'message_string']

    raise IOError(u'More than one value found in database.')

  def _GetMessageFileKeys(self, event_log_provider_key):
    """Retrieves the message file keys.

    Args:
      event_log_provider_key: the Event Log provider key.

    Yields:
      A message file key.
    """
    table_names = [u'message_file_per_event_log_provider']
    column_names = [u'message_file_key']
    condition = u'event_log_provider_key == {0:d}'.format(
        event_log_provider_key)

    generator = self._database_file.GetValues(
        table_names, column_names, condition)

    # pylint: disable=not-an-iterable
    for values in generator:
      yield values[u'message_file_key']

  def _GetMessageFilenames(self, log_source, message_file_type):
    """Retrieves the message filenames of a specific Event Log provider.

    Args:
      log_source (str): Event Log source.
      message_file_type (str): message file type.

    Returns:
      list[str]: message filenames.
    """
    table_names = [
        u'event_log_providers', u'message_file_per_event_log_provider',
        u'message_files']
    column_names = [u'message_files.path']
    condition = (
        u'{0:s}.log_source == "{3:s}" AND '
        u'{1:s}.message_file_type == "{4:s}" AND '
        u'{0:s}.event_log_provider_key == {1:s}.event_log_provider_key AND '
        u'{1:s}.message_file_key == {2:s}.message_file_key').format(
            u'event_log_providers', u'message_file_per_event_log_provider',
            u'message_files', log_source, message_file_type)

    message_filenames = []
    for values in self._database_file.GetValues(
        table_names, column_names, condition):
      message_filename = values[u'message_files.path']
      message_filenames.append(message_filename)

    return message_filenames

  def _GetMessages(self, message_file_key, lcid):
    """Retrieves the messages of a specific message table.

    Args:
      message_file_key (int): message file key.
      lcid (int): language code identifier (LCID).

    Yields:
      A tuple of a message identifier and string.
    """
    table_name = u'message_table_{0:d}_0x{1:08x}'.format(message_file_key, lcid)

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      return

    column_names = [u'message_identifier', u'message_string']
    condition = u''

    for values in self._database_file.GetValues(
        [table_name], column_names, condition):
      yield values[u'message_identifier'], values[u'message_string']

  def GetEventLogProviders(self):
    """Retrieves the Event Log providers.

    Yields:
      An Event Log provider (instance of EventLogProvider).
    """
    table_names = [u'event_log_providers']
    column_names = [u'log_source', u'provider_guid']
    condition = u''

    event_log_providers = []
    for values in self._database_file.GetValues(
        table_names, column_names, condition):
      event_log_provider = resources.EventLogProvider(
          None, values[u'log_source'], values[u'provider_guid'])
      event_log_providers.append(event_log_provider)

    for event_log_provider in event_log_providers:
      message_filenames = self._GetMessageFilenames(
          event_log_provider.log_source,
          definitions.MESSAGE_FILE_TYPE_CATEGORY)
      event_log_provider.SetCategoryMessageFilenames(message_filenames)

      message_filenames = self._GetMessageFilenames(
          event_log_provider.log_source, definitions.MESSAGE_FILE_TYPE_EVENT)
      event_log_provider.SetEventMessageFilenames(message_filenames)

      message_filenames = self._GetMessageFilenames(
          event_log_provider.log_source,
          definitions.MESSAGE_FILE_TYPE_PARAMETER)
      event_log_provider.SetParameterMessageFilenames(message_filenames)

      yield event_log_provider

  def GetMessage(self, log_source, lcid, message_identifier):
    """Retrieves a specific message for a specific Event Log source.

    Args:
      log_source (str): Event Log source.
      lcid (int): language code identifier (LCID).
      message_identifier (int): message identifier.

    Returns:
      The message string or None if not available.
    """
    event_log_provider_key = self._GetEventLogProviderKey(log_source)
    if not event_log_provider_key:
      return

    generator = self._GetMessageFileKeys(event_log_provider_key)
    if not generator:
      return

    message_string = None
    for message_file_key in generator:
      message_string = self._GetMessage(
          message_file_key, lcid, message_identifier)

      if message_string:
        break

    return message_string

  def GetMessages(self, log_source, lcid):
    """Retrieves the messages of a specific Event Log source.

    Args:
      log_source (str): Event Log source.
      lcid (int): language code identifier (LCID).

    Yields:
      A tuple of a message identifier and string.
    """
    event_log_provider_key = self._GetEventLogProviderKey(log_source)
    if not event_log_provider_key:
      return

    generator = self._GetMessageFileKeys(event_log_provider_key)
    if not generator:
      return

    for message_file_key in generator:
      for message_identifier, message_string in self._GetMessages(
          message_file_key, lcid):
        yield message_identifier, message_string

  def GetMetadataAttribute(self, attribute_name):
    """Retrieves the metadata attribute.

    Args:
      attribute_name (str): name of the metadata attribute.

    Returns:
      str: value of the metadata attribute or None.

    Raises:
      IOError: if more than one value is found in the database.
    """
    table_name = u'metadata'

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      return

    column_names = [u'value']
    condition = u'name == "{0:s}"'.format(attribute_name)

    values = list(self._database_file.GetValues(
        [table_name], column_names, condition))

    number_of_values = len(values)
    if number_of_values == 0:
      return

    elif number_of_values == 1:
      return values[0][u'value']

    raise IOError(u'More than one value found in database.')


class ResourcesSqlite3DatabaseWriter(Sqlite3DatabaseWriter):
  """Class to represent a sqlite3 Event Log resources database writer."""

  # Message string specifiers that are considered white space.
  _WHITE_SPACE_SPECIFIER_RE = re.compile(r'(%[0b]|[\r\n])')
  # Message string specifiers that expand to text.
  _TEXT_SPECIFIER_RE = re.compile(r'%([ .!%nrt])')
  # Curly brackets in a message string.
  _CURLY_BRACKETS = re.compile(r'([\{\}])')
  # Message string specifiers that expand to a variable place holder.
  _PLACE_HOLDER_SPECIFIER_RE = re.compile(r'%([1-9][0-9]?)[!]?[s]?[!]?')

  def __init__(self, string_format=u'wrc'):
    """Initializes the database writer.

    Args:
      string_format: optional string format. The default is the Windows
          Resource (wrc) format.
    """
    super(ResourcesSqlite3DatabaseWriter, self).__init__()
    self._string_format = string_format

  def _GetEventLogProviderKey(self, event_log_provider):
    """Retrieves the key of an Event Log provider.

    Args:
      event_log_provider (EventLogProvider): event log provider.

    Returns:
      An integer containing the Event Log provider key or None if no such value.

    Raises:
      IOError: if more than one value is found in the database.
    """
    table_names = [u'event_log_providers']
    column_names = [u'event_log_provider_key']
    condition = u'log_source = "{0:s}"'.format(
        event_log_provider.log_source)
    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return

    if number_of_values == 1:
      values = values_list[0]
      return values[u'event_log_provider_key']

    raise IOError(u'More than one value found in database.')

  def _GetMessageFileKey(self, message_file):
    """Retrieves the key of a message file.

    Args:
      message_file (MessageFile): message file.

    Returns:
      An integer containing the message file key or None if no such value.

    Raises:
      IOError: if more than one value is found in the database.
    """
    table_names = [u'message_files']
    column_names = [u'message_file_key']
    condition = u'LOWER(path) = LOWER("{0:s}")'.format(
        message_file.windows_path)
    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return

    if number_of_values == 1:
      values = values_list[0]
      return values[u'message_file_key']

    raise IOError(u'More than one value found in database.')

  def _GetMessageFileKeyByPath(self, message_filename):
    """Retrieves the key of a message file for a specific path.

    Args:
      message_filename (str): message filename.

    Returns:
      An integer containing the message file key or None if no such value.

    Raises:
      IOError: if more than one value is found in the database.
    """
    table_names = [u'message_files']
    column_names = [u'message_file_key']
    condition = u'LOWER(path) = LOWER("{0:s}")'.format(message_filename)
    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return

    if number_of_values == 1:
      values = values_list[0]
      return values[u'message_file_key']

    raise IOError(u'More than one value found in database.')

  def _ReformatMessageString(self, message_string):
    """Reformats the message string.

    Args:
      message_string (str): message string.

    Returns:
      The message string in Python format() (PEP 3103) style.
    """
    def place_holder_specifier_replacer(match_object):
      """Replaces message string place holders into Python format() style."""
      expanded_groups = []
      for group in match_object.groups():
        try:
          place_holder_number = int(group, 10) - 1
          expanded_group = u'{{{0:d}:s}}'.format(place_holder_number)
        except ValueError:
          expanded_group = group

        expanded_groups.append(expanded_group)

      return u''.join(expanded_groups)

    if not message_string:
      return

    message_string = self._WHITE_SPACE_SPECIFIER_RE.sub(r'', message_string)
    message_string = self._TEXT_SPECIFIER_RE.sub(r'\\\1', message_string)
    message_string = self._CURLY_BRACKETS.sub(r'\1\1', message_string)
    return self._PLACE_HOLDER_SPECIFIER_RE.sub(
        place_holder_specifier_replacer, message_string)

  def _WriteMessage(
      self, message_file, language_identifier, message_identifier,
      message_string, table_name, has_table):
    """Writes a message to a specific message table.

    Args:
      message_file (MessageFile): message file.
      language_identifier (int): language identifier (LCID).
      message_identifier (int): message identifier.
      message_string (str): message string.
      table_name (str): name of the table.
      has_table (bool): True if the table previously existed in the database.
    """
    column_names = [u'message_identifier', u'message_string']

    if not has_table:
      insert_values = True

    else:
      condition = u'message_identifier = "{0:s}"'.format(message_identifier)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 1:
        values = values_list[0]
        if message_string != values[u'message_string']:
          logging.warning((
              u'Message string mismatch for LCID: {0:s}, '
              u'file version: {1:s}, message identifier: {2:s}.\n'
              u'Found: {3:s}\nStored: {4:s}\n').format(
                  language_identifier, message_file.file_version,
                  message_identifier, message_string,
                  values[u'message_string']))

      elif number_of_values != 0:
        logging.warning((
            u'More than one message string found for LCID: {0:s}, '
            u'file version: {1:s}, message identifier: {2:s}.').format(
                language_identifier, message_file.file_version,
                message_identifier))

      # TODO: warn if new message has been found.
      insert_values = False

    if insert_values:
      if self._string_format == u'pep3101':
        message_string = self._ReformatMessageString(message_string)

      values = [message_identifier, message_string]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteMessageFile(self, message_file):
    """Writes a message file.

    Args:
      message_file (MessageFile): message file.
    """
    table_name = u'message_files'
    column_names = [u'path']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          u'message_file_key INTEGER PRIMARY KEY AUTOINCREMENT', u'path TEXT']
      self._database_file.CreateTable(table_name, column_definitions)

    if not has_table:
      insert_values = True

    else:
      condition = u'LOWER(path) = LOWER("{0:s}")'.format(
          message_file.windows_path)
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
      message_file (MessageFile): message file.
      message_table (MessageTable): message table.
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
        column_definitions = [
            u'message_identifier TEXT', u'message_string TEXT']
        self._database_file.CreateTable(table_name, column_definitions)

      message_strings = message_table.message_strings
      for message_identifier, message_string in iter(message_strings.items()):
        self._WriteMessage(
            message_file, message_table.lcid, message_identifier,
            message_string, table_name, has_table)

      self._WriteMessageTableLanguage(message_file_key, message_table.lcid)

  def _WriteMessageTableLanguage(self, message_file_key, language_identifier):
    """Writes a message table language.

    Args:
      message_file_key (int): message file key.
      language_identifier (int): language identifier (LCID).
    """
    table_name = u'message_table_languages'
    column_names = [u'lcid', u'message_file_key']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [u'lcid TEXT', u'message_file_key INT']
      self._database_file.CreateTable(table_name, column_definitions)

    if not has_table:
      insert_values = True

    else:
      condition = u'lcid = "{0:s}" AND message_file_key = "{1:d}"'.format(
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
      event_log_provider (EventLogProvider): event log provider.
    """
    table_name = u'event_log_providers'
    column_names = [u'log_source', u'provider_guid']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          u'event_log_provider_key INTEGER PRIMARY KEY AUTOINCREMENT',
          u'log_source TEXT', u'provider_guid TEXT']
      self._database_file.CreateTable(table_name, column_definitions)
      insert_values = True

    else:
      condition = u'log_source = "{0:s}"'.format(event_log_provider.log_source)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 0:
        insert_values = True
      else:
        # TODO: check if more than 1 result.
        insert_values = False

    if insert_values:
      values = [
          event_log_provider.log_source, event_log_provider.provider_guid]
      self._database_file.InsertValues(table_name, column_names, values)

  def WriteMessageFile(self, message_file):
    """Writes the Windows Message Resource file.

    Args:
      message_file (MessageFile): message file.
    """
    self._WriteMessageFile(message_file)

    for message_table in message_file.GetMessageTables():
      # TODO track the languages in a table.
      self._WriteMessageTable(message_file, message_table)

  def WriteMessageFilesPerEventLogProvider(
      self, event_log_provider, message_filename, message_file_type):
    """Writes the message files used by an Event Log provider.

    Args:
      event_log_provider (EventLogProvider): event log provider.
      message_filename (str): message filename.
    """
    table_name = u'message_file_per_event_log_provider'
    column_names = [
        u'message_file_key', u'message_file_type', u'event_log_provider_key']

    event_log_provider_key = self._GetEventLogProviderKey(event_log_provider)
    if event_log_provider_key is None:
      logging.warning(u'Missing event log provider key for: {0:s}'.format(
          event_log_provider.log_source))

    message_file_key = self._GetMessageFileKeyByPath(message_filename)
    if message_file_key is None:
      logging.warning(u'Missing message file key for: {0:s}'.format(
          message_filename))

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          u'message_file_key INTEGER', u'message_file_type TEXT',
          u'event_log_provider_key INTEGER']
      self._database_file.CreateTable(table_name, column_definitions)
      insert_values = True

    else:
      condition = (
          u'message_file_key = {0:d} AND message_file_type = "{1:s}" AND '
          u'event_log_provider_key = {2:d}').format(
              message_file_key, message_file_type, event_log_provider_key)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 0:
        insert_values = True
      else:
        # TODO: check if more than 1 result.
        insert_values = False

    if insert_values:
      values = [message_file_key, message_file_type, event_log_provider_key]
      self._database_file.InsertValues(table_name, column_names, values)

  def WriteMetadataAttribute(self, attribute_name, attribute_value):
    """Writes a metadata attribute.

    Args:
      attribute_name (str): name of the metadata attribute.
      attribute_value (str): value of the metadata attribute.
    """
    table_name = u'metadata'
    column_names = [u'name', u'value']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [u'name TEXT', u'value TEXT']
      self._database_file.CreateTable(table_name, column_definitions)
      insert_values = True

    else:
      condition = u'name = "{0:s}"'.format(attribute_name)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 0:
        insert_values = True
      else:
        # TODO: check if more than 1 result.
        insert_values = False

    if insert_values:
      values = [attribute_name, attribute_value]
      self._database_file.InsertValues(table_name, column_names, values)

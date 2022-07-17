# -*- coding: utf-8 -*-
"""Read from and write to SQLite databases."""

import difflib
import logging
import re
import sqlite3

import pywrc

from winevtrc import definitions
from winevtrc import errors
from winevtrc import resources


class SQLite3DatabaseFile(object):
  """A SQLite database file."""

  _HAS_TABLE_QUERY = (
      'SELECT name FROM sqlite_master '
      'WHERE type = "table" AND name = "{0:s}"')

  def __init__(self):
    """Initializes the database file."""
    super(SQLite3DatabaseFile, self).__init__()
    self._connection = None
    self._cursor = None
    self.filename = None
    self.read_only = None

  def _GetValues(self, cursor, table_names, column_names, condition):
    """Values generator function.

    Args:
      cursor (sqlite3.Cursor): SQLite database cursor.
      table_names (list[str]): table names.
      column_names (list[str]): column names.
      condition (str): condition.

    Yields:
      dict[str, object]: value.

    Raises:
      BackendError: if the database back-end raises an exception.
    """
    if condition:
      condition = ' WHERE {0:s}'.format(condition)

    sql_query = 'SELECT {1:s} FROM {0:s}{2:s}'.format(
        ', '.join(table_names), ', '.join(column_names), condition)

    try:
      cursor.execute(sql_query)
    except sqlite3.OperationalError as exception:
      raise errors.BackendError(exception)

    for row in cursor:
      values = {}
      for column_index, column_name in enumerate(column_names):
        values[column_name] = row[column_index]
      yield values

  def Close(self):
    """Closes the database file.

    Raises:
      IOError: if the database is not opened.
      OSError: if the database is not opened.
    """
    if not self._connection:
      raise IOError('Cannot close database not opened.')

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
      OSError: if the database is not opened or
          if the database is in read-only mode.
    """
    if not self._connection:
      raise IOError('Cannot create table database not opened.')

    if self.read_only:
      raise IOError('Cannot create table database in read-only mode.')

    sql_query = 'CREATE TABLE {0:s} ( {1:s} )'.format(
        table_name, ', '.join(column_definitions))

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
      IOError: if the database is not opened.
      OSError: if the database is not opened.
    """
    if not self._connection:
      raise IOError('Cannot retrieve values database not opened.')

    cursor = self._connection.cursor()
    return self._GetValues(cursor, table_names, column_names, condition)

  def HasTable(self, table_name):
    """Determines if a specific table exists.

    Args:
      table_name (str): table name.

    Returns:
      bool: True if the table exists, false otherwise.

    Raises:
      BackendError: if the database back-end raises an exception.
      IOError: if the database is not opened.
      OSError: if the database is not opened.
    """
    if not self._connection:
      raise IOError('Cannot determine if table exists database not opened.')

    sql_query = self._HAS_TABLE_QUERY.format(table_name)

    try:
      self._cursor.execute(sql_query)

      has_table = bool(self._cursor.fetchone())

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
      OSError: if the database is not opened or
          if the database is in read-only mode or
          if an unsupported value type is encountered.
    """
    if not self._connection:
      raise IOError('Cannot insert values database not opened.')

    if self.read_only:
      raise IOError('Cannot insert values database in read-only mode.')

    if not values:
      return

    sql_values = []
    for value in values:
      # TODO: handle bool.
      if isinstance(value, str):
        # In sqlite3 the double quote is escaped with a second double quote.
        value = '"{0:s}"'.format(re.sub('"', '""', value))
      elif isinstance(value, int):
        value = '{0:d}'.format(value)
      elif isinstance(value, float):
        value = '{0:f}'.format(value)
      elif value is None:
        value = 'NULL'
      else:
        raise IOError('Unsupported value type: {0!s}.'.format(type(value)))
      sql_values.append(value)

    sql_query = 'INSERT INTO {0:s} ( {1:s} ) VALUES ( {2:s} )'.format(
        table_name, ', '.join(column_names), ', '.join(sql_values))

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
      OSError: if the database is already opened.
    """
    if self._connection:
      raise IOError('Cannot open database already opened.')

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


class SQLite3DatabaseReader(object):
  """SQLite database reader."""

  def __init__(self):
    """Initializes the database reader."""
    super(SQLite3DatabaseReader, self).__init__()
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


class SQLite3DatabaseWriter(object):
  """SQLite database writer."""

  def __init__(self):
    """Initializes the database writer."""
    super(SQLite3DatabaseWriter, self).__init__()
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
    return self._database_file.Open(filename)


class EventProvidersSQLite3DatabaseReader(SQLite3DatabaseReader):
  """Event Log providers SQLite database reader."""

  def _GetMessageFilenames(self, event_log_provider_key, message_file_type):
    """Retrieves the message filenames of a specific Event Log provider.

    Args:
      event_log_provider_key (int): the Event Log provider key.
      message_file_type (str): message file type.

    Returns:
      list[str]: message filenames.
    """
    table_names = [
        'message_file_per_event_log_provider', 'message_files']
    column_names = ['message_files.message_filename']
    condition = (
        '{0:s}.event_log_provider_key == {2:d} AND '
        '{0:s}.message_file_type == "{3:s}" AND '
        '{0:s}.message_file_key == {1:s}.message_file_key').format(
            'message_file_per_event_log_provider', 'message_files',
            event_log_provider_key, message_file_type)

    message_filenames = []
    for values in self._database_file.GetValues(
        table_names, column_names, condition):
      message_filename = values['message_files.message_filename']
      message_filenames.append(message_filename)

    return message_filenames

  def GetEventLogProviders(self):
    """Retrieves the Event Log providers.

    Yields:
      EventLogProvider: Event Log provider.
    """
    table_names = ['event_log_providers']
    column_names = [
        'event_log_provider_key', 'identifier', 'additional_identifier',
        'name', 'log_source1', 'log_source2', 'log_source3', 'log_type']
    condition = ''

    for values in self._database_file.GetValues(
        table_names, column_names, condition):
      event_log_provider = resources.EventLogProvider()
      event_log_provider.identifier = values['identifier']

      if values['additional_identifier']:
        event_log_provider.additional_identifier = values[
            'additional_identifier']

      event_log_provider.name = values['name']

      if values['log_type']:
        event_log_provider.log_types.append(values['log_type'])
      if values['log_source1']:
        event_log_provider.log_sources.append(values['log_source1'])
      if values['log_source2']:
        event_log_provider.log_sources.append(values['log_source2'])
      if values['log_source3']:
        event_log_provider.log_sources.append(values['log_source3'])

      message_filenames = self._GetMessageFilenames(
          values['event_log_provider_key'],
          definitions.MESSAGE_FILE_TYPE_CATEGORY)
      event_log_provider.SetCategoryMessageFilenames(message_filenames)

      message_filenames = self._GetMessageFilenames(
          values['event_log_provider_key'], definitions.MESSAGE_FILE_TYPE_EVENT)
      event_log_provider.SetEventMessageFilenames(message_filenames)

      message_filenames = self._GetMessageFilenames(
          values['event_log_provider_key'],
          definitions.MESSAGE_FILE_TYPE_PARAMETER)
      event_log_provider.SetParameterMessageFilenames(message_filenames)

      yield event_log_provider

  def GetMessageFiles(self):
    """Retrieves the message filenames.

    Yields:
      tuple[str, str]: message filename and corresponding database filename.
    """
    table_names = ['message_files']
    column_names = ['message_filename', 'database_filename']
    condition = ''

    for values in self._database_file.GetValues(
        table_names, column_names, condition):
      yield values['message_filename'], values['database_filename']


class EventProvidersSQLite3DatabaseWriter(SQLite3DatabaseWriter):
  """Event Log providers SQLite database writer."""

  def _GetEventLogProviderCondition(self, event_log_provider):
    """Retrieves the condition to find the Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.

    Returns:
      str: condition.
    """
    condition = ''

    log_sources = event_log_provider.log_sources + [None, None, None]
    log_source1, log_source2, log_source3 = log_sources[:3]

    if log_source1:
      condition = (
          'log_source1 = "{0:s}" OR log_source2 = "{0:s}" OR '
          'log_source3 = "{0:s}"').format(log_source1)

    if log_source2:
      condition = (
          '{0:s} OR log_source1 = "{1:s}" OR log_source2 = "{1:s}" OR '
          'log_source3 = "{1:s}"').format(condition, log_source2)

    if log_source3:
      condition = (
          '{0:s} OR log_source1 = "{1:s}" OR log_source2 = "{1:s}" OR '
          'log_source3 = "{1:s}"').format(condition, log_source3)

    if event_log_provider.identifier:
      if condition:
        condition = '{0:s} OR '.format(condition)

      condition = (
          '{0:s}identifier = "{1:s}" OR additional_identifier = '
          '"{1:s}"').format(condition, event_log_provider.identifier)

    if event_log_provider.additional_identifier:
      condition = (
          '{0:s} OR identifier = "{1:s}" OR additional_identifier = '
          '"{1:s}"').format(
              condition, event_log_provider.additional_identifier)

    return condition

  def _GetEventLogProviderKey(self, event_log_provider):
    """Retrieves the key of an Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.

    Returns:
      int: Event Log provider key or None if no such value.

    Raises:
      IOError: if more than one value is found in the database.
      OSError: if more than one value is found in the database.
    """
    table_names = ['event_log_providers']
    column_names = ['event_log_provider_key']
    condition = self._GetEventLogProviderCondition(event_log_provider)
    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return None

    if number_of_values == 1:
      values = values_list[0]
      return values['event_log_provider_key']

    raise IOError(
        'More than one value found in database for log source: {0:s}.'.format(
            event_log_provider.name or event_log_provider.log_source))

  def _GetMessageFileKey(self, message_filename):
    """Retrieves the key of a message file.

    Args:
      message_filename (str): message filename.

    Returns:
      int: message file key or None if no such value.

    Raises:
      IOError: if more than one value is found in the database.
      OSError: if more than one value is found in the database.
    """
    table_names = ['message_files']
    column_names = ['message_file_key']
    condition = 'LOWER(message_filename) = LOWER("{0:s}")'.format(
        message_filename)
    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return None

    if number_of_values == 1:
      values = values_list[0]
      return values['message_file_key']

    raise IOError((
        'More than one value found in database for message filename: '
        '{0:s}').format(message_filename))

  def WriteMessageFilesPerEventLogProvider(
      self, event_log_provider, message_filename, message_file_type):
    """Writes the message files used by an Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
      message_filename (str): message filename.
      message_file_type (str): message file type.
    """
    table_name = 'message_file_per_event_log_provider'
    column_names = [
        'message_file_key', 'message_file_type', 'event_log_provider_key']

    event_log_provider_key = self._GetEventLogProviderKey(event_log_provider)
    if event_log_provider_key is None:
      logging.warning('Missing Event Log provider key for: {0:s}'.format(
          event_log_provider.log_sources[0]))

    message_file_key = self._GetMessageFileKey(message_filename)
    if message_file_key is None:
      logging.warning('Missing message file key for: {0:s}'.format(
          message_filename))

    if not self._database_file.HasTable(table_name):
      column_definitions = [
          'message_file_key INTEGER', 'message_file_type TEXT',
          'event_log_provider_key INTEGER']
      self._database_file.CreateTable(table_name, column_definitions)

    values = [message_file_key, message_file_type, event_log_provider_key]
    self._database_file.InsertValues(table_name, column_names, values)

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
    """
    table_name = 'event_log_providers'
    column_names = [
        'identifier', 'additional_identifier', 'name', 'log_source1',
        'log_source2', 'log_source3', 'log_type']

    insert_values = True

    if not self._database_file.HasTable(table_name):
      column_definitions = [
          'event_log_provider_key INTEGER PRIMARY KEY AUTOINCREMENT',
          'identifier TEXT', 'additional_identifier TEXT', 'name TEXT',
          'log_source1 TEXT', 'log_source2 TEXT', 'log_source3 TEXT',
          'log_type TEXT']
      self._database_file.CreateTable(table_name, column_definitions)

    else:
      condition = self._GetEventLogProviderCondition(event_log_provider)
      if not condition:
        logging.warning(
            'Unable to create condition for Event Log provider: {0:s}.'.format(
                event_log_provider.name or event_log_provider.log_source))

      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values > 0:
        # TODO: determine if Event Log provider should be updated.
        logging.warning('Event log provider: {0:s} already exists.'.format(
            event_log_provider.name or event_log_provider.log_source))
        insert_values = False

    if insert_values:
      log_sources = event_log_provider.log_sources + [None, None, None]
      log_source1, log_source2, log_source3 = log_sources[:3]

      values = [
          event_log_provider.identifier,
          event_log_provider.additional_identifier, event_log_provider.name,
          log_source1, log_source2, log_source3, event_log_provider.log_type]
      self._database_file.InsertValues(table_name, column_names, values)

  def WriteMessageFile(self, message_filename, database_filename):
    """Writes a Windows message file to the database.

    Args:
      message_filename (str): message filename.
      database_filename (str): database filename.
    """
    table_name = 'message_files'
    column_names = ['message_filename', 'database_filename']

    if not self._database_file.HasTable(table_name):
      column_definitions = [
          'message_file_key INTEGER PRIMARY KEY AUTOINCREMENT',
          'message_filename TEXT', 'database_filename TEXT']
      self._database_file.CreateTable(table_name, column_definitions)

    values = [message_filename, database_filename]
    self._database_file.InsertValues(table_name, column_names, values)


class MessageFileSQLite3DatabaseReader(SQLite3DatabaseReader):
  """Event Log message file SQLite database reader."""

  def GetMessageTables(self):
    """Retrieves the message tables.

    Yields:
      tuple[int, str]: language code identifier (LCID) and the message file
          version.
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
      lcid (str): language code identifier (LCID).
      file_version (str): message file file version.

    Yields:
      tuple[int, str]: message identifier and message string.
    """
    table_name = 'message_table_{0:s}'.format(lcid)
    if file_version:
      table_name = '{0:s}_{1:s}'.format(table_name, file_version)
      table_name = re.sub(r'\.', r'_', table_name)

    column_names = ['message_identifier', 'message_string']
    condition = ''

    for values in self._database_file.GetValues(
        [table_name], column_names, condition):
      yield values['message_identifier'], values['message_string']

  def GetStringTables(self):
    """Retrieves the string tables.

    Yields:
      tuple[int, str]: language code identifier (LCID) and the message file
          version.
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
      lcid (str): language code identifier (LCID).
      file_version (str): message file file version.

    Yields:
      tuple[int, str]: string identifier and string.
    """
    table_name = 'string_table_{0:s}_{1:s}'.format(
        lcid, re.sub(r'\.', '_', file_version))
    column_names = ['string_identifier', 'string']
    condition = ''

    for values in self._database_file.GetValues(
        [table_name], column_names, condition):
      yield values['string_identifier'], values['string']


class MessageResourceFileSQLite3DatabaseWriter(SQLite3DatabaseWriter):
  """Event Log message resource file SQLite database writer."""

  def __init__(self, message_resource_file):
    """Initializes an Event Log message resource file SQLite database writer.

    Args:
      message_resource_file (MessageResourceFile): message resource file.
    """
    super(MessageResourceFileSQLite3DatabaseWriter, self).__init__()
    self._message_resource_file = message_resource_file

  def _GetMessageFileKey(self, message_resource_file):
    """Retrieves the key of a message file.

    Args:
      message_resource_file (MessageResourceFile): message resource file.

    Returns:
      int: message file key or None if no such value.

    Raises:
      IOError: if more than one value is found in the database.
      OSError: if more than one value is found in the database.
    """
    table_names = ['message_files']
    column_names = ['message_file_key']
    condition = 'LOWER(path) = LOWER("{0:s}")'.format(
        message_resource_file.windows_path)

    if message_resource_file.file_version:
      condition = '{0:s} AND file_version = "{1:s}"'.format(
          condition, message_resource_file.file_version)

    if message_resource_file.product_version:
      condition = '{0:s} AND product_version = "{1:s}"'.format(
          condition, message_resource_file.product_version)

    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return None

    if number_of_values == 1:
      values = values_list[0]
      return values['message_file_key']

    raise IOError('More than one value found in database.')

  def _WriteMessage(
      self, message_resource_file, message_table_resource, language_identifier,
      message_index, table_name, has_table):
    """Writes a message to a specific message table.

    Args:
      message_resource_file (MessageResourceFile): message resource file.
      message_table_resource (pywrc.message_table_resource): message table
          resource.
      language_identifier (int): language identifier (LCID).
      message_index (int): message index.
      table_name (str): name of the table.
      has_table (bool): True if the table previously existed in the database.
    """
    column_names = ['message_identifier', 'message_string']

    message_identifier = message_table_resource.get_message_identifier(
        message_index)
    message_identifier = '0x{0:08x}'.format(message_identifier)

    message_string = message_table_resource.get_string(message_index)

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
          differ = difflib.Differ()
          diff_list = list(differ.compare(
              [values['message_string']], [message_string]))
          logging.warning((
              'Message string mismatch for LCID: 0x{0:08x}, '
              'file version: {1:s}, message identifier: {2:s}.\n'
              '{3:s}\n').format(
                  language_identifier, message_resource_file.file_version,
                  message_identifier, '\n'.join(diff_list)))

      elif number_of_values != 0:
        logging.warning((
            'More than one message string found for LCID: 0x{0:08x}, '
            'file version: {1:s}, message identifier: {2:s}.').format(
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
      condition = 'LOWER(path) = LOWER("{0:s}")'.format(
          message_resource_file.windows_path)

      if message_resource_file.file_version:
        condition = '{0:s} AND file_version = "{1:s}"'.format(
            condition, message_resource_file.file_version)

      if message_resource_file.product_version:
        condition = '{0:s} AND product_version = "{1:s}"'.format(
            condition, message_resource_file.product_version)

      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      insert_values = number_of_values == 0

    if insert_values:
      values = [
          message_resource_file.windows_path,
          message_resource_file.file_version,
          message_resource_file.product_version]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteMessageTable(
      self, message_resource_file, message_table_resource, language_identifier):
    """Writes a message table for a specific language identifier.

    Args:
      message_resource_file (MessageResourceFile): message resource file.
      message_table_resource (pywrc.message_table_resource): message table
          resource.
      language_identifier (int): language identifier (LCID).
    """
    number_of_messages = message_table_resource.get_number_of_messages()

    if number_of_messages > 0:
      message_file_key = self._GetMessageFileKey(message_resource_file)
      if message_file_key is None:
        logging.warning('Missing message file key for: {0:s}'.format(
            message_resource_file.windows_path))
      else:
        self._WriteMessageTableLanguage(message_file_key, language_identifier)

      table_name = 'message_table_0x{0:08x}'.format(language_identifier)
      if message_resource_file.file_version:
        table_name = '{0:s}_{1:s}'.format(
            table_name, message_resource_file.file_version)
        table_name = re.sub(r'\.', r'_', table_name)

      has_table = self._database_file.HasTable(table_name)
      if not has_table:
        column_definitions = [
            'message_identifier TEXT', 'message_string TEXT']
        self._database_file.CreateTable(table_name, column_definitions)

      for message_index in range(0, number_of_messages):
        self._WriteMessage(
            message_resource_file, message_table_resource, language_identifier,
            message_index, table_name, has_table)

  def _WriteMessageTableLanguage(self, message_file_key, language_identifier):
    """Writes a message table language.

    Args:
      message_file_key (int): message file key.
      language_identifier (int): language identifier (LCID).
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
      insert_values = number_of_values == 0

    if insert_values:
      language = definitions.LANGUAGES.get(language_identifier, ['', ''])[0]
      values = [
          '0x{0:08x}'.format(language_identifier), message_file_key, language]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteMessageTables(self):
    """Writes the message tables."""
    wrc_resource = self._message_resource_file.GetMessageTableResource()
    if wrc_resource and wrc_resource.number_of_items > 0:
      if wrc_resource.number_of_items != 1:
        logging.warning((
            'More than 1 message table resource item in message file: '
            '{0:s}.').format(self._message_resource_file.windows_path))

      wrc_resource_item = wrc_resource.items[0]
      for wrc_resource_sub_item in wrc_resource_item.sub_items:
        resource_data = wrc_resource_sub_item.read()

        message_table_resource = pywrc.message_table_resource()
        message_table_resource.copy_from_byte_stream(resource_data)

        self._WriteMessageTable(
            self._message_resource_file, message_table_resource,
            wrc_resource_sub_item.identifier)

  def _WriteString(
      self, message_resource_file, string_table_resource, language_identifier,
      string_index, table_name, has_table):
    """Writes a string to a specific string table.

    Args:
      message_resource_file (MessageResourceFile): message resource file.
      string_table_resource (pywrc.string_table_resource): string table
          resource.
      language_identifier (int): language identifier (LCID).
      string_index (int): string index.
      table_name (str): name of the table.
      has_table (bool): True if the table previously existed in the database.
    """
    column_names = ['string_identifier', 'string']

    string_identifier = string_table_resource.get_string_identifier(
        string_index)
    string_identifier = '0x{0:08x}'.format(string_identifier)

    string = string_table_resource.get_string(string_index)

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
              'String mismatch for LCID: 0x{0:08x}, '
              'file version: {1:s}, string identifier: {2:s}.\n'
              'Found: {3:s}\nStored: {4:s}\n').format(
                  language_identifier, message_resource_file.file_version,
                  string_identifier, string, values['string']))

      elif number_of_values != 0:
        logging.warning((
            'More than one string found for LCID: 0x{0:08x}, '
            'file version: {1:s}, string identifier: {2:s}.').format(
                language_identifier, message_resource_file.file_version,
                string_identifier))

      # TODO: warn if new string has been found.
      insert_values = False

    if insert_values:
      values = [string_identifier, string]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteStringTable(
      self, message_resource_file, string_table_resource, language_identifier):
    """Writes a string table for a specific language identifier.

    Args:
      message_resource_file (MessageResourceFile): message resource file.
      string_table_resource (pywrc.string_table_resource): string table
          resource.
      language_identifier (int): language identifier (LCID).
    """
    number_of_strings = string_table_resource.get_number_of_strings()

    if number_of_strings > 0:
      message_file_key = self._GetMessageFileKey(message_resource_file)
      if message_file_key is None:
        logging.warning('Missing message file key for: {0:s}'.format(
            message_resource_file.windows_path))

      self._WriteStringTableLanguage(message_file_key, language_identifier)

      table_name = 'message_table_0x{0:08x}'.format(language_identifier)
      if message_resource_file.file_version:
        table_name = '{0:s}_{1:s}'.format(
            table_name, message_resource_file.file_version)
        table_name = re.sub(r'\.', r'_', table_name)

      has_table = self._database_file.HasTable(table_name)
      if not has_table:
        column_definitions = ['string_identifier TEXT', 'string TEXT']
        self._database_file.CreateTable(table_name, column_definitions)

      for string_index in range(0, number_of_strings):
        self._WriteString(
            message_resource_file, string_table_resource, language_identifier,
            string_index, table_name, has_table)

  def _WriteStringTableLanguage(self, message_file_key, language_identifier):
    """Writes a string table language.

    Args:
      message_file_key (int): message file key.
      language_identifier (int): language identifier (LCID).
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
      insert_values = number_of_values == 0

    if insert_values:
      language = definitions.LANGUAGES.get(language_identifier, ['', ''])[0]
      values = [
          '0x{0:08x}'.format(language_identifier), message_file_key, language]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteStringTables(self):
    """Writes the string tables."""
    wrc_resource = self._message_resource_file.GetStringTableResource()
    if wrc_resource:
      for wrc_resource_item in wrc_resource.items:
        for wrc_resource_sub_item in wrc_resource_item.sub_items:
          resource_data = wrc_resource_sub_item.read()

          string_table_resource = pywrc.string_table_resource()
          string_table_resource.copy_from_byte_stream(
              resource_data, wrc_resource_item.identifier)

          self._WriteStringTable(
              self._message_resource_file, string_table_resource,
              wrc_resource_sub_item.identifier)

  def WriteResources(self):
    """Writes the resources."""
    self._WriteMessageFile(self._message_resource_file)
    self._WriteMessageTables()
    # TODO: only write the string resources of Event Log parameter files.
    # self._WriteStringTables()


class ResourcesSQLite3DatabaseReader(SQLite3DatabaseReader):
  """Event Log resources SQLite database reader."""

  def _GetEventLogProviderKey(self, log_source):
    """Retrieves the Event Log provider key.

    Args:
      log_source (str): Event Log source.

    Returns:
      int: an Event Log provider key or None if not available.

    Raises:
      IOError: if more than one value is found in the database.
      OSError: if more than one value is found in the database.
    """
    table_names = ['event_log_providers']
    column_names = ['event_log_provider_key']
    condition = 'log_source == "{0:s}"'.format(log_source)

    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return None

    if number_of_values == 1:
      values = values_list[0]
      return values['event_log_provider_key']

    raise IOError('More than one value found in database.')

  def _GetMessage(self, message_file_key, lcid, message_identifier):
    """Retrieves a specific message from a specific message table.

    Args:
      message_file_key (int): message file key.
      lcid (int): language code identifier (LCID).
      message_identifier (int): message identifier.

    Returns:
      str: the message string or None if not available.

    Raises:
      IOError: if more than one value is found in the database.
      OSError: if more than one value is found in the database.
    """
    table_name = 'message_table_{0:d}_0x{1:08x}'.format(message_file_key, lcid)

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      return None

    column_names = ['message_string']
    condition = 'message_identifier == "0x{0:08x}"'.format(message_identifier)

    values = list(self._database_file.GetValues(
        [table_name], column_names, condition))

    number_of_values = len(values)
    if number_of_values == 0:
      return None

    if number_of_values == 1:
      return values[0]['message_string']

    raise IOError('More than one value found in database.')

  def _GetMessageFileKeys(self, event_log_provider_key):
    """Retrieves the message file keys.

    Args:
      event_log_provider_key (int): the Event Log provider key.

    Yields:
      int: a message file key.
    """
    table_names = ['message_file_per_event_log_provider']
    column_names = ['message_file_key']
    condition = 'event_log_provider_key == {0:d}'.format(
        event_log_provider_key)

    generator = self._database_file.GetValues(
        table_names, column_names, condition)

    # pylint: disable=not-an-iterable
    for values in generator:
      yield values['message_file_key']

  def _GetMessageFilenames(self, log_source, message_file_type):
    """Retrieves the message filenames of a specific Event Log provider.

    Args:
      log_source (str): Event Log source.
      message_file_type (str): message file type.

    Returns:
      list[str]: message filenames.
    """
    table_names = [
        'event_log_providers', 'message_file_per_event_log_provider',
        'message_files']
    column_names = ['message_files.path']
    condition = (
        '{0:s}.log_source == "{3:s}" AND '
        '{1:s}.message_file_type == "{4:s}" AND '
        '{0:s}.event_log_provider_key == {1:s}.event_log_provider_key AND '
        '{1:s}.message_file_key == {2:s}.message_file_key').format(
            'event_log_providers', 'message_file_per_event_log_provider',
            'message_files', log_source, message_file_type)

    message_filenames = []
    for values in self._database_file.GetValues(
        table_names, column_names, condition):
      message_filename = values['message_files.path']
      message_filenames.append(message_filename)

    return message_filenames

  def _GetMessages(self, message_file_key, lcid):
    """Retrieves the messages of a specific message table.

    Args:
      message_file_key (int): message file key.
      lcid (int): language code identifier (LCID).

    Yields:
      tuple[int, str]: message identifier and message string.
    """
    table_name = 'message_table_{0:d}_0x{1:08x}'.format(message_file_key, lcid)

    has_table = self._database_file.HasTable(table_name)
    if has_table:
      column_names = ['message_identifier', 'message_string']
      condition = ''

      for values in self._database_file.GetValues(
          [table_name], column_names, condition):
        yield values['message_identifier'], values['message_string']

  def GetEventLogProviders(self):
    """Retrieves the Event Log providers.

    Yields:
      EventLogProvider: an Event Log provider.
    """
    table_names = ['event_log_providers']
    column_names = ['log_source', 'provider_guid']
    condition = ''

    event_log_providers = []
    for values in self._database_file.GetValues(
        table_names, column_names, condition):
      event_log_provider = resources.EventLogProvider()
      event_log_provider.identifier = values['provider_guid']

      event_log_provider.log_sources.append(values['log_source'])

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
      str: the message string or None if not available.
    """
    event_log_provider_key = self._GetEventLogProviderKey(log_source)
    if not event_log_provider_key:
      return None

    generator = self._GetMessageFileKeys(event_log_provider_key)
    if not generator:
      return None

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
      tuple[int, str]: message identifier and message string.
    """
    event_log_provider_key = self._GetEventLogProviderKey(log_source)
    if event_log_provider_key:
      for message_file_key in self._GetMessageFileKeys(event_log_provider_key):
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
      OSError: if more than one value is found in the database.
    """
    table_name = 'metadata'

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      return None

    column_names = ['value']
    condition = 'name == "{0:s}"'.format(attribute_name)

    values = list(self._database_file.GetValues(
        [table_name], column_names, condition))

    number_of_values = len(values)
    if number_of_values == 0:
      return None

    if number_of_values == 1:
      return values[0]['value']

    raise IOError('More than one value found in database.')


class ResourcesSQLite3DatabaseWriter(SQLite3DatabaseWriter):
  """Event Log resources SQLite database writer."""

  # Message string specifiers that are considered white space.
  _WHITE_SPACE_SPECIFIER_RE = re.compile(r'(%[0b]|[\r\n])')
  # Message string specifiers that expand to text.
  _TEXT_SPECIFIER_RE = re.compile(r'%([ .!%nrt])')
  # Curly brackets in a message string.
  _CURLY_BRACKETS = re.compile(r'([\{\}])')
  # Message string specifiers that expand to a variable place holder.
  _PLACE_HOLDER_SPECIFIER_RE = re.compile(r'%([1-9][0-9]?)[!]?[s]?[!]?')

  def __init__(self, string_format='wrc'):
    """Initializes the database writer.

    Args:
      string_format (Optional[str]): string format. The default is the Windows
          Resource (wrc) format.
    """
    super(ResourcesSQLite3DatabaseWriter, self).__init__()
    self._string_format = string_format

  def _GetEventLogProviderKey(self, event_log_provider):
    """Retrieves the key of an Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.

    Returns:
      int: the Event Log provider key or None if no such value.

    Raises:
      IOError: if more than one value is found in the database.
      OSError: if more than one value is found in the database.
    """
    table_names = ['event_log_providers']
    column_names = ['event_log_provider_key']
    condition = 'log_source = "{0:s}"'.format(
        event_log_provider.log_source)
    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return None

    if number_of_values == 1:
      values = values_list[0]
      return values['event_log_provider_key']

    raise IOError('More than one value found in database.')

  def _GetMessageFileKey(self, message_file):
    """Retrieves the key of a message file.

    Args:
      message_file (MessageFile): message file.

    Returns:
      int: the message file key or None if no such value.

    Raises:
      IOError: if more than one value is found in the database.
      OSError: if more than one value is found in the database.
    """
    table_names = ['message_files']
    column_names = ['message_file_key']
    condition = 'LOWER(path) = LOWER("{0:s}")'.format(
        message_file.windows_path)
    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return None

    if number_of_values == 1:
      values = values_list[0]
      return values['message_file_key']

    raise IOError('More than one value found in database.')

  def _GetMessageFileKeyByPath(self, message_filename):
    """Retrieves the key of a message file for a specific path.

    Args:
      message_filename (str): message filename.

    Returns:
      int: the message file key or None if no such value.

    Raises:
      IOError: if more than one value is found in the database.
      OSError: if more than one value is found in the database.
    """
    table_names = ['message_files']
    column_names = ['message_file_key']
    condition = 'LOWER(path) = LOWER("{0:s}")'.format(message_filename)
    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return None

    if number_of_values == 1:
      values = values_list[0]
      return values['message_file_key']

    raise IOError('More than one value found in database.')

  def _ReformatMessageString(self, message_string):
    """Reformats the message string.

    Args:
      message_string (str): message string.

    Returns:
      str: message string in Python format() (PEP 3103) style or None
          if not available.
    """
    def PlaceHolderSpecifierReplacer(match_object):
      """Replaces message string place holders into Python format() style."""
      expanded_groups = []
      for group in match_object.groups():
        try:
          place_holder_number = int(group, 10) - 1
          expanded_group = '{{{0:d}:s}}'.format(place_holder_number)
        except ValueError:
          expanded_group = group

        expanded_groups.append(expanded_group)

      return ''.join(expanded_groups)

    if not message_string:
      return None

    message_string = self._WHITE_SPACE_SPECIFIER_RE.sub(r'', message_string)
    message_string = self._TEXT_SPECIFIER_RE.sub(r'\\\1', message_string)
    message_string = self._CURLY_BRACKETS.sub(r'\1\1', message_string)
    return self._PLACE_HOLDER_SPECIFIER_RE.sub(
        PlaceHolderSpecifierReplacer, message_string)

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
              'Message string mismatch for LCID: {0:s}, '
              'file version: {1:s}, message identifier: {2:s}.\n'
              'Found: {3:s}\nStored: {4:s}\n').format(
                  language_identifier, message_file.file_version,
                  message_identifier, message_string,
                  values['message_string']))

      elif number_of_values != 0:
        logging.warning((
            'More than one message string found for LCID: {0:s}, '
            'file version: {1:s}, message identifier: {2:s}.').format(
                language_identifier, message_file.file_version,
                message_identifier))

      # TODO: warn if new message has been found.
      insert_values = False

    if insert_values:
      if self._string_format == 'pep3101':
        message_string = self._ReformatMessageString(message_string)

      values = [message_identifier, message_string]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteMessageFile(self, message_file):
    """Writes a message file.

    Args:
      message_file (MessageFile): message file.
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
      condition = 'LOWER(path) = LOWER("{0:s}")'.format(
          message_file.windows_path)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      insert_values = number_of_values == 0

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
        logging.warning('Missing message file key for: {0:s}'.format(
            message_file.windows_path))

      table_name = 'message_table_{0:d}_{1:s}'.format(
          message_file_key, message_table.lcid)

      has_table = self._database_file.HasTable(table_name)
      if not has_table:
        column_definitions = [
            'message_identifier TEXT', 'message_string TEXT']
        self._database_file.CreateTable(table_name, column_definitions)

      message_strings = message_table.message_strings
      for message_identifier, message_string in message_strings.items():
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
      insert_values = number_of_values == 0

    if insert_values:
      values = [language_identifier, message_file_key]
      self._database_file.InsertValues(table_name, column_names, values)

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
    """
    table_name = 'event_log_providers'
    column_names = ['log_source', 'provider_guid']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          'event_log_provider_key INTEGER PRIMARY KEY AUTOINCREMENT',
          'log_source TEXT', 'provider_guid TEXT']
      self._database_file.CreateTable(table_name, column_definitions)
      insert_values = True

    else:
      if event_log_provider.log_source:
        condition = 'log_source = "{0:s}"'.format(event_log_provider.log_source)
      if event_log_provider.identifier:
        condition = 'provider_guid = "{0:s}"'.format(
            event_log_provider.identifier)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      # TODO: check if more than 1 result.
      insert_values = number_of_values == 0

    if insert_values:
      values = [
          event_log_provider.log_source, event_log_provider.identifier]
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
      event_log_provider (EventLogProvider): Event Log provider.
      message_filename (str): message filename.
      message_file_type (str): message file type.
    """
    table_name = 'message_file_per_event_log_provider'
    column_names = [
        'message_file_key', 'message_file_type', 'event_log_provider_key']

    event_log_provider_key = self._GetEventLogProviderKey(event_log_provider)
    if event_log_provider_key is None:
      logging.warning('Missing Event Log provider key for: {0:s}'.format(
          event_log_provider.log_source))

    message_file_key = self._GetMessageFileKeyByPath(message_filename)
    if message_file_key is None:
      logging.warning('Missing message file key for: {0:s}'.format(
          message_filename))

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          'message_file_key INTEGER', 'message_file_type TEXT',
          'event_log_provider_key INTEGER']
      self._database_file.CreateTable(table_name, column_definitions)
      insert_values = True

    else:
      condition = (
          'message_file_key = {0:d} AND message_file_type = "{1:s}" AND '
          'event_log_provider_key = {2:d}').format(
              message_file_key, message_file_type, event_log_provider_key)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      # TODO: check if more than 1 result.
      insert_values = number_of_values == 0

    if insert_values:
      values = [message_file_key, message_file_type, event_log_provider_key]
      self._database_file.InsertValues(table_name, column_names, values)

  def WriteMetadataAttribute(self, attribute_name, attribute_value):
    """Writes a metadata attribute.

    Args:
      attribute_name (str): name of the metadata attribute.
      attribute_value (str): value of the metadata attribute.
    """
    table_name = 'metadata'
    column_names = ['name', 'value']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = ['name TEXT', 'value TEXT']
      self._database_file.CreateTable(table_name, column_definitions)
      insert_values = True

    else:
      condition = 'name = "{0:s}"'.format(attribute_name)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      # TODO: check if more than 1 result.
      insert_values = number_of_values == 0

    if insert_values:
      values = [attribute_name, attribute_value]
      self._database_file.InsertValues(table_name, column_names, values)

#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests to read from and write SQLite databases."""

import os
import unittest

from winevtrc import database
from winevtrc import errors
from winevtrc import resource_file
from winevtrc import resources

from tests import test_lib as shared_test_lib


class SQLite3DatabaseFileTest(shared_test_lib.BaseTestCase):
  """Tests for the SQLite database file."""

  @shared_test_lib.skipUnlessHasTestFile([u'winevt-rc.db'])
  def testOpenClose(self):
    """Tests the Open and Close functions."""
    database_file = database.SQLite3DatabaseFile()

    test_file_path = self._GetTestFilePath([u'winevt-rc.db'])
    database_file.Open(test_file_path, read_only=True)

    with self.assertRaises(IOError):
      database_file.Open(test_file_path, read_only=True)

    database_file.Close()

    # Test close after close.
    with self.assertRaises(IOError):
      database_file.Close()

  def testCreateTable(self):
    """Tests the CreateTable function."""
    database_file = database.SQLite3DatabaseFile()
    table_name = u'event_log_providers'
    column_names = [u'log_source', u'log_type', u'provider_guid']

    with shared_test_lib.TempDirectory() as temporary_directory:
      test_file_path = os.path.join(temporary_directory, u'winevt-rc.db')
      database_file.Open(test_file_path)

      database_file.CreateTable(table_name, column_names)

      database_file.Close()

    with self.assertRaises(IOError):
      database_file.CreateTable(table_name, column_names)

  def testCreateTableReadOnly(self):
    """Tests the CreateTable function read-only mode."""
    database_file = database.SQLite3DatabaseFile()
    table_name = u'event_log_providers'
    column_names = [u'log_source', u'log_type', u'provider_guid']

    with shared_test_lib.TempDirectory() as temporary_directory:
      test_file_path = os.path.join(temporary_directory, u'winevt-rc.db')
      database_file.Open(test_file_path, read_only=True)

      with self.assertRaises(IOError):
        database_file.CreateTable(table_name, column_names)

      database_file.Close()

  @shared_test_lib.skipUnlessHasTestFile([u'winevt-rc.db'])
  def testGetValues(self):
    """Tests the GetValues function."""
    database_file = database.SQLite3DatabaseFile()

    test_file_path = self._GetTestFilePath([u'winevt-rc.db'])
    database_file.Open(test_file_path, read_only=True)

    generator = database_file.GetValues(
        [u'metadata'], [u'name', u'value'], u'')
    values_dict = next(generator)
    self.assertIsNotNone(values_dict)

    generator = database_file.GetValues(
        [u'bogus'], [u'name', u'value'], u'')

    with self.assertRaises(errors.BackendError):
      next(generator)

    database_file.Close()

    with self.assertRaises(IOError):
      database_file.GetValues([u'metadata'], [u'name', u'value'], u'')

  @shared_test_lib.skipUnlessHasTestFile([u'winevt-rc.db'])
  def testHasTable(self):
    """Tests the HasTable function."""
    database_file = database.SQLite3DatabaseFile()

    test_file_path = self._GetTestFilePath([u'winevt-rc.db'])
    database_file.Open(test_file_path, read_only=True)

    result = database_file.HasTable(u'metadata')
    self.assertTrue(result)

    result = database_file.HasTable(u'bogus')
    self.assertFalse(result)

    database_file.Close()

    with self.assertRaises(IOError):
      database_file.HasTable(u'metadata')

  def testInsertValues(self):
    """Tests the InsertValues function."""
    database_file = database.SQLite3DatabaseFile()
    table_name = u'event_log_providers'
    column_names = [u'log_source', u'log_type', u'provider_guid']
    values = [
        u'LocationNotifications', u'Application',
        u'{5b93cdfa-5f51-45e0-9fde-296983129e6c}']

    with shared_test_lib.TempDirectory() as temporary_directory:
      test_file_path = os.path.join(temporary_directory, u'winevt-rc.db')
      database_file.Open(test_file_path)

      database_file.CreateTable(table_name, column_names)

      database_file.InsertValues(table_name, column_names, values)

      database_file.InsertValues(table_name, column_names, [1, 1.0, None])

      database_file.InsertValues(table_name, column_names, [])

      with self.assertRaises(IOError):
        database_file.InsertValues(
            table_name, column_names, [database_file, "", ""])

      database_file.Close()

    with self.assertRaises(IOError):
      database_file.InsertValues(table_name, column_names, values)

  def testInsertValuesReadOnly(self):
    """Tests the CreInsertValues function read-only mode."""
    database_file = database.SQLite3DatabaseFile()
    table_name = u'event_log_providers'
    column_names = [u'log_source', u'log_type', u'provider_guid']
    values = [
        u'LocationNotifications', u'Application',
        u'{5b93cdfa-5f51-45e0-9fde-296983129e6c}']

    with shared_test_lib.TempDirectory() as temporary_directory:
      test_file_path = os.path.join(temporary_directory, u'winevt-rc.db')
      database_file.Open(test_file_path, read_only=True)

      with self.assertRaises(IOError):
        database_file.InsertValues(table_name, column_names, values)

      database_file.Close()


class Sqlite3DatabaseReaderTest(shared_test_lib.BaseTestCase):
  """Tests for the SQLite database reader."""

  @shared_test_lib.skipUnlessHasTestFile([u'winevt-rc.db'])
  def testOpenClose(self):
    """Tests the Open and Close functions."""
    database_reader = database.Sqlite3DatabaseReader()

    test_file_path = self._GetTestFilePath([u'winevt-rc.db'])
    database_reader.Open(test_file_path)

    database_reader.Close()


class Sqlite3DatabaseWriterTest(shared_test_lib.BaseTestCase):
  """Tests for the SQLite database writer."""

  def testOpenClose(self):
    """Tests the Open and Close functions."""
    database_writer = database.Sqlite3DatabaseWriter()

    with shared_test_lib.TempDirectory() as temporary_directory:
      test_file_path = os.path.join(temporary_directory, u'winevt-rc.db')
      database_writer.Open(test_file_path)

      database_writer.Close()


class EventProvidersSqlite3DatabaseReaderTest(shared_test_lib.BaseTestCase):
  """Tests for the event providers SQLite database reader."""

  # pylint: disable=protected-access

  # TODO: add test for _GetMessageFilenames

  @shared_test_lib.skipUnlessHasTestFile([u'winevt-kb.db'])
  def testGetEventLogProviders(self):
    """Tests the GetEventLogProviders function."""
    database_reader = database.EventProvidersSqlite3DatabaseReader()

    test_file_path = self._GetTestFilePath([u'winevt-kb.db'])
    database_reader.Open(test_file_path)

    generator = database_reader.GetEventLogProviders()
    event_log_providers = list(generator)

    self.assertEqual(len(event_log_providers), 388)

    database_reader.Close()

  @shared_test_lib.skipUnlessHasTestFile([u'winevt-kb.db'])
  def testGetMessageFiles(self):
    """Tests the GetMessageFiles function."""
    database_reader = database.EventProvidersSqlite3DatabaseReader()

    test_file_path = self._GetTestFilePath([u'winevt-kb.db'])
    database_reader.Open(test_file_path)

    generator = database_reader.GetMessageFiles()
    message_files = list(generator)

    self.assertEqual(len(message_files), 187)

    database_reader.Close()


class EventProvidersSqlite3DatabaseWriterTest(shared_test_lib.BaseTestCase):
  """Tests for the event providers SQLite database writer."""

  # pylint: disable=protected-access

  # TODO: add test for _GetEventLogProviderKey
  # TODO: add test for _GetMessageFileKey

  def testWriteMessageFilesPerEventLogProvider(self):
    """Tests the WriteMessageFilesPerEventLogProvider function."""
    event_log_provider = resources.EventLogProvider(
        u'Application',
        u'Microsoft-Windows-RPC-Events',
        u'{f4aed7c7-a898-4627-b053-44a7caa12fcd}')

    database_writer = database.EventProvidersSqlite3DatabaseWriter()

    with shared_test_lib.TempDirectory() as temporary_directory:
      test_file_path = os.path.join(temporary_directory, u'winevt-kb.db')
      database_writer.Open(test_file_path)

      database_writer.WriteEventLogProvider(event_log_provider)

      database_writer.WriteMessageFile(
          u'%SystemRoot%\\system32\\rpcrt4.dll', u'rpcrt4.dll.db')

      database_writer.WriteMessageFilesPerEventLogProvider(
          event_log_provider, u'%SystemRoot%\\system32\\rpcrt4.dll', u'event')

      database_writer.WriteMessageFilesPerEventLogProvider(
          event_log_provider, u'%SystemRoot%\\system32\\rpcrt4.dll', u'event')

      database_writer.Close()

  def testWriteEventLogProvider(self):
    """Tests the WriteEventLogProvider function."""
    event_log_provider = resources.EventLogProvider(
        u'Application',
        u'Microsoft-Windows-RPC-Events',
        u'{f4aed7c7-a898-4627-b053-44a7caa12fcd}')

    database_writer = database.EventProvidersSqlite3DatabaseWriter()

    with shared_test_lib.TempDirectory() as temporary_directory:
      test_file_path = os.path.join(temporary_directory, u'winevt-kb.db')
      database_writer.Open(test_file_path)

      database_writer.WriteEventLogProvider(event_log_provider)

      database_writer.WriteEventLogProvider(event_log_provider)

      database_writer.Close()

  def testWriteMessageFile(self):
    """Tests the WriteMessageFile function."""
    database_writer = database.EventProvidersSqlite3DatabaseWriter()

    with shared_test_lib.TempDirectory() as temporary_directory:
      test_file_path = os.path.join(temporary_directory, u'winevt-kb.db')
      database_writer.Open(test_file_path)

      database_writer.WriteMessageFile(
          u'%SystemRoot%\\system32\\rpcrt4.dll', u'rpcrt4.dll.db')

      database_writer.WriteMessageFile(
          u'%SystemRoot%\\system32\\rpcrt4.dll', u'rpcrt4.dll.db')

      database_writer.Close()


class MessageFileSqlite3DatabaseReaderTest(shared_test_lib.BaseTestCase):
  """Tests for the message file SQLite database reader."""

  @shared_test_lib.skipUnlessHasTestFile([u'message_file.db'])
  def testGetMessageTables(self):
    """Tests the GetMessageTables function."""
    database_reader = database.MessageFileSqlite3DatabaseReader()

    test_file_path = self._GetTestFilePath([u'message_file.db'])
    database_reader.Open(test_file_path)

    generator = database_reader.GetMessageTables()
    message_tables = list(generator)

    self.assertEqual(len(message_tables), 1)

    database_reader.Close()

  @shared_test_lib.skipUnlessHasTestFile([u'message_file.db'])
  def testGetMessages(self):
    """Tests the GetMessages function."""
    database_reader = database.MessageFileSqlite3DatabaseReader()

    test_file_path = self._GetTestFilePath([u'message_file.db'])
    database_reader.Open(test_file_path)

    generator = database_reader.GetMessages(u'0x00000409', u'1.0.0.0')
    messages = list(generator)

    self.assertEqual(len(messages), 3)
    self.assertEqual(messages[0], (u'0x00000001', u'Category\r\n'))

    generator = database_reader.GetMessages(u'0x00000413', u'1.0.0.0')

    with self.assertRaises(errors.BackendError):
      list(generator)

    database_reader.Close()

  @shared_test_lib.skipUnlessHasTestFile([u'message_file.db'])
  def testGetStringTables(self):
    """Tests the GetStringTables function."""
    database_reader = database.MessageFileSqlite3DatabaseReader()

    test_file_path = self._GetTestFilePath([u'message_file.db'])
    database_reader.Open(test_file_path)

    generator = database_reader.GetStringTables()

    # TODO: string tables currently not written.
    with self.assertRaises(errors.BackendError):
      list(generator)

    database_reader.Close()

  @shared_test_lib.skipUnlessHasTestFile([u'message_file.db'])
  def testGetStrings(self):
    """Tests the GetStrings function."""
    database_reader = database.MessageFileSqlite3DatabaseReader()

    test_file_path = self._GetTestFilePath([u'message_file.db'])
    database_reader.Open(test_file_path)

    generator = database_reader.GetStrings(u'0x00000409', u'1.0.0.0')

    # TODO: string tables currently not written.
    with self.assertRaises(errors.BackendError):
      list(generator)

    database_reader.Close()


class MessageFileSqlite3DatabaseWriterTest(shared_test_lib.BaseTestCase):
  """Tests for the message file SQLite database writer."""

  # pylint: disable=protected-access

  @shared_test_lib.skipUnlessHasTestFile([u'wrc_test.dll'])
  def testGetMessageFileKey(self):
    """Tests the _GetMessageFileKey function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\wrc_test.dll')

    test_file_path = self._GetTestFilePath([u'wrc_test.dll'])
    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      database_writer = database.MessageFileSqlite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, u'message_file.db')
        database_writer.Open(test_file_path)

        database_writer._WriteMessageFile(message_resource_file)

        message_file_key = database_writer._GetMessageFileKey(
            message_resource_file)
        self.assertEqual(message_file_key, 1)

        database_writer.Close()

      message_resource_file.Close()

  @shared_test_lib.skipUnlessHasTestFile([u'wrc_test.dll'])
  def testWriteMessage(self):
    """Tests the _WriteMessage function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\wrc_test.dll')

    test_file_path = self._GetTestFilePath([u'wrc_test.dll'])
    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      message_table_resource = message_resource_file.GetMessageTableResource()

      database_writer = database.MessageFileSqlite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, u'message_file.db')
        database_writer.Open(test_file_path)

        # TODO: implement test.
        # database_writer._WriteMessage(
        #    message_resource_file, message_table_resource, 0x00000409, 0,
        #    u'message_table_0x00000409', False)
        _ = message_table_resource

        database_writer.Close()

      message_resource_file.Close()

  @shared_test_lib.skipUnlessHasTestFile([u'wrc_test.dll'])
  def testWriteMessageFile(self):
    """Tests the _WriteMessageFile function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\wrc_test.dll')

    test_file_path = self._GetTestFilePath([u'wrc_test.dll'])
    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      database_writer = database.MessageFileSqlite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, u'message_file.db')
        database_writer.Open(test_file_path)

        database_writer._WriteMessageFile(message_resource_file)

        database_writer.Close()

      message_resource_file.Close()

  @shared_test_lib.skipUnlessHasTestFile([u'wrc_test.dll'])
  def testWriteMessageTable(self):
    """Tests the _WriteMessageTable function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\wrc_test.dll')

    test_file_path = self._GetTestFilePath([u'wrc_test.dll'])
    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      message_table_resource = message_resource_file.GetMessageTableResource()

      database_writer = database.MessageFileSqlite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, u'message_file.db')
        database_writer.Open(test_file_path)

        database_writer._WriteMessageFile(message_resource_file)

        database_writer._WriteMessageTable(
            message_resource_file, message_table_resource, 0x00000409)

        database_writer._WriteMessageTable(
            message_resource_file, message_table_resource, 0x00000409)

        database_writer.Close()

      message_resource_file.Close()

  @shared_test_lib.skipUnlessHasTestFile([u'wrc_test.dll'])
  def testWriteMessageTableLanguage(self):
    """Tests the _WriteMessageTableLanguage function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\wrc_test.dll')

    test_file_path = self._GetTestFilePath([u'wrc_test.dll'])
    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      database_writer = database.MessageFileSqlite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, u'message_file.db')
        database_writer.Open(test_file_path)

        database_writer._WriteMessageFile(message_resource_file)

        message_file_key = database_writer._GetMessageFileKey(
            message_resource_file)

        database_writer._WriteMessageTableLanguage(
            message_file_key, 0x00000409)

        database_writer._WriteMessageTableLanguage(
            message_file_key, 0x00000409)

        database_writer.Close()

      message_resource_file.Close()

  @shared_test_lib.skipUnlessHasTestFile([u'wrc_test.dll'])
  def testWriteMessageTables(self):
    """Tests the _WriteMessageTables function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\wrc_test.dll')

    test_file_path = self._GetTestFilePath([u'wrc_test.dll'])
    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      database_writer = database.MessageFileSqlite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, u'message_file.db')
        database_writer.Open(test_file_path)

        database_writer._WriteMessageFile(message_resource_file)

        database_writer._WriteMessageTables()

        database_writer.Close()

      message_resource_file.Close()

  # TODO: add tests for _WriteString.

  @shared_test_lib.skipUnlessHasTestFile([u'wrc_test.dll'])
  def testWriteStringTable(self):
    """Tests the _WriteStringTable function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\wrc_test.dll')

    test_file_path = self._GetTestFilePath([u'wrc_test.dll'])
    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      string_resource = message_resource_file.GetStringResource()

      database_writer = database.MessageFileSqlite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, u'message_file.db')
        database_writer.Open(test_file_path)

        database_writer._WriteMessageFile(message_resource_file)

        database_writer._WriteStringTable(
            message_resource_file, string_resource, 0x00000409)

        database_writer.Close()

      message_resource_file.Close()

  @shared_test_lib.skipUnlessHasTestFile([u'wrc_test.dll'])
  def testWriteStringTableLanguage(self):
    """Tests the _WriteStringTableLanguage function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\wrc_test.dll')

    test_file_path = self._GetTestFilePath([u'wrc_test.dll'])
    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      database_writer = database.MessageFileSqlite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, u'message_file.db')
        database_writer.Open(test_file_path)

        database_writer._WriteMessageFile(message_resource_file)

        message_file_key = database_writer._GetMessageFileKey(
            message_resource_file)

        database_writer._WriteStringTableLanguage(
            message_file_key, 0x00000409)

        database_writer._WriteStringTableLanguage(
            message_file_key, 0x00000409)

        database_writer.Close()

      message_resource_file.Close()

  @shared_test_lib.skipUnlessHasTestFile([u'wrc_test.dll'])
  def testWriteStringTables(self):
    """Tests the _WriteStringTables function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\wrc_test.dll')

    test_file_path = self._GetTestFilePath([u'wrc_test.dll'])
    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      database_writer = database.MessageFileSqlite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, u'message_file.db')
        database_writer.Open(test_file_path)

        database_writer._WriteMessageFile(message_resource_file)

        database_writer._WriteStringTables()

        database_writer.Close()

      message_resource_file.Close()

  @shared_test_lib.skipUnlessHasTestFile([u'wrc_test.dll'])
  def testWriteResources(self):
    """Tests the WriteResources function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\wrc_test.dll')

    test_file_path = self._GetTestFilePath([u'wrc_test.dll'])
    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      database_writer = database.MessageFileSqlite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, u'message_file.db')
        database_writer.Open(test_file_path)

        database_writer.WriteResources()

        database_writer.Close()

      message_resource_file.Close()


class ResourcesSqlite3DatabaseReaderTest(shared_test_lib.BaseTestCase):
  """Tests for the resources SQLite database reader."""

  # pylint: disable=protected-access

  @shared_test_lib.skipUnlessHasTestFile([u'winevt-kb.db'])
  def testGetEventLogProviderKey(self):
    """Tests the _GetEventLogProviderKey function."""
    database_reader = database.ResourcesSqlite3DatabaseReader()

    test_file_path = self._GetTestFilePath([u'winevt-kb.db'])
    database_reader.Open(test_file_path)

    database_reader._GetEventLogProviderKey(u'Security')

    database_reader.Close()

  # TODO: add test for _GetMessage
  # TODO: add test for _GetMessageFileKeys
  # TODO: add test for _GetMessageFilenames
  # TODO: add test for _GetMessages

  @shared_test_lib.skipUnlessHasTestFile([u'winevt-kb.db'])
  def testGetEventLogProviders(self):
    """Tests the GetEventLogProviders function."""
    database_reader = database.ResourcesSqlite3DatabaseReader()

    test_file_path = self._GetTestFilePath([u'winevt-kb.db'])
    database_reader.Open(test_file_path)

    database_reader.GetEventLogProviders()

    database_reader.Close()

  # TODO: add test for GetMessage

  @shared_test_lib.skipUnlessHasTestFile([u'winevt-kb.db'])
  def testGetMessages(self):
    """Tests the GetMessages function."""
    database_reader = database.ResourcesSqlite3DatabaseReader()

    test_file_path = self._GetTestFilePath([u'winevt-kb.db'])
    database_reader.Open(test_file_path)

    database_reader.GetMessages(u'bogus', 0x00000409)

    database_reader.Close()

  @shared_test_lib.skipUnlessHasTestFile([u'winevt-kb.db'])
  def testGetMetadataAttribute(self):
    """Tests the GetMetadataAttribute function."""
    database_reader = database.ResourcesSqlite3DatabaseReader()

    test_file_path = self._GetTestFilePath([u'winevt-kb.db'])
    database_reader.Open(test_file_path)

    database_reader.GetMetadataAttribute(u'bogus')

    database_reader.Close()


class ResourcesSqlite3DatabaseWriterTest(shared_test_lib.BaseTestCase):
  """Tests for the resources SQLite database writer."""

  # pylint: disable=protected-access

  # TODO: add test for _GetEventLogProviderKey
  # TODO: add test for _GetMessageFileKey
  # TODO: add test for _GetMessageFileKeyByPath
  # TODO: add test for _ReformatMessageString
  # TODO: add test for _WriteMessage
  # TODO: add test for _WriteMessageFile
  # TODO: add test for _WriteMessageTable
  # TODO: add test for _WriteMessageTableLanguage
  # TODO: add test for WriteEventLogProvider
  # TODO: add test for WriteMessageFile
  # TODO: add test for WriteMessageFilesPerEventLogProvider
  # TODO: add test for WriteMetadataAttribute


if __name__ == '__main__':
  unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests to read from and write SQLite databases."""

import os
import unittest

import pywrc

from winevtrc import database
from winevtrc import errors
from winevtrc import resource_file
from winevtrc import resources

from tests import test_lib as shared_test_lib


class SQLite3DatabaseFileTest(shared_test_lib.BaseTestCase):
  """Tests for the SQLite database file."""

  def testOpenClose(self):
    """Tests the Open and Close functions."""
    test_file_path = self._GetTestFilePath(['winevt-rc.db'])
    self._SkipIfPathNotExists(test_file_path)

    database_file = database.SQLite3DatabaseFile()
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
    table_name = 'event_log_providers'
    column_names = ['log_source', 'log_type', 'provider_guid']

    with shared_test_lib.TempDirectory() as temporary_directory:
      test_file_path = os.path.join(temporary_directory, 'winevt-rc.db')
      database_file.Open(test_file_path)

      database_file.CreateTable(table_name, column_names)

      database_file.Close()

    with self.assertRaises(IOError):
      database_file.CreateTable(table_name, column_names)

  def testCreateTableReadOnly(self):
    """Tests the CreateTable function read-only mode."""
    database_file = database.SQLite3DatabaseFile()
    table_name = 'event_log_providers'
    column_names = ['log_source', 'log_type', 'provider_guid']

    with shared_test_lib.TempDirectory() as temporary_directory:
      test_file_path = os.path.join(temporary_directory, 'winevt-rc.db')
      database_file.Open(test_file_path, read_only=True)

      with self.assertRaises(IOError):
        database_file.CreateTable(table_name, column_names)

      database_file.Close()

  def testGetValues(self):
    """Tests the GetValues function."""
    test_file_path = self._GetTestFilePath(['winevt-rc.db'])
    self._SkipIfPathNotExists(test_file_path)

    database_file = database.SQLite3DatabaseFile()
    database_file.Open(test_file_path, read_only=True)

    generator = database_file.GetValues(
        ['metadata'], ['name', 'value'], '')
    values_dict = next(generator)
    self.assertIsNotNone(values_dict)

    generator = database_file.GetValues(
        ['bogus'], ['name', 'value'], '')

    with self.assertRaises(errors.BackendError):
      next(generator)

    database_file.Close()

    with self.assertRaises(IOError):
      database_file.GetValues(['metadata'], ['name', 'value'], '')

  def testHasTable(self):
    """Tests the HasTable function."""
    test_file_path = self._GetTestFilePath(['winevt-rc.db'])
    self._SkipIfPathNotExists(test_file_path)

    database_file = database.SQLite3DatabaseFile()
    database_file.Open(test_file_path, read_only=True)

    result = database_file.HasTable('metadata')
    self.assertTrue(result)

    result = database_file.HasTable('bogus')
    self.assertFalse(result)

    database_file.Close()

    with self.assertRaises(IOError):
      database_file.HasTable('metadata')

  def testInsertValues(self):
    """Tests the InsertValues function."""
    database_file = database.SQLite3DatabaseFile()
    table_name = 'event_log_providers'
    column_names = ['log_source', 'log_type', 'provider_guid']
    values = [
        'LocationNotifications', 'Application',
        '{5b93cdfa-5f51-45e0-9fde-296983129e6c}']

    with shared_test_lib.TempDirectory() as temporary_directory:
      test_file_path = os.path.join(temporary_directory, 'winevt-rc.db')
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
    table_name = 'event_log_providers'
    column_names = ['log_source', 'log_type', 'provider_guid']
    values = [
        'LocationNotifications', 'Application',
        '{5b93cdfa-5f51-45e0-9fde-296983129e6c}']

    with shared_test_lib.TempDirectory() as temporary_directory:
      test_file_path = os.path.join(temporary_directory, 'winevt-rc.db')
      database_file.Open(test_file_path, read_only=True)

      with self.assertRaises(IOError):
        database_file.InsertValues(table_name, column_names, values)

      database_file.Close()


class SQLite3DatabaseReaderTest(shared_test_lib.BaseTestCase):
  """Tests for the SQLite database reader."""

  def testOpenClose(self):
    """Tests the Open and Close functions."""
    test_file_path = self._GetTestFilePath(['winevt-rc.db'])
    self._SkipIfPathNotExists(test_file_path)

    database_reader = database.SQLite3DatabaseReader()
    database_reader.Open(test_file_path)

    database_reader.Close()


class SQLite3DatabaseWriterTest(shared_test_lib.BaseTestCase):
  """Tests for the SQLite database writer."""

  def testOpenClose(self):
    """Tests the Open and Close functions."""
    database_writer = database.SQLite3DatabaseWriter()

    with shared_test_lib.TempDirectory() as temporary_directory:
      test_file_path = os.path.join(temporary_directory, 'winevt-rc.db')
      database_writer.Open(test_file_path)

      database_writer.Close()


class EventProvidersSQLite3DatabaseReaderTest(shared_test_lib.BaseTestCase):
  """Tests for the event providers SQLite database reader."""

  # pylint: disable=protected-access

  # TODO: add test for _GetMessageFilenames

  def testGetEventLogProviders(self):
    """Tests the GetEventLogProviders function."""
    test_file_path = self._GetTestFilePath(['winevt-kb.db'])
    self._SkipIfPathNotExists(test_file_path)

    database_reader = database.EventProvidersSQLite3DatabaseReader()
    database_reader.Open(test_file_path)

    generator = database_reader.GetEventLogProviders()
    event_log_providers = list(generator)

    self.assertEqual(len(event_log_providers), 1122)

    database_reader.Close()

  def testGetMessageFiles(self):
    """Tests the GetMessageFiles function."""
    test_file_path = self._GetTestFilePath(['winevt-kb.db'])
    self._SkipIfPathNotExists(test_file_path)

    database_reader = database.EventProvidersSQLite3DatabaseReader()
    database_reader.Open(test_file_path)

    generator = database_reader.GetMessageFiles()
    message_files = list(generator)

    self.assertEqual(len(message_files), 788)

    database_reader.Close()


class EventProvidersSQLite3DatabaseWriterTest(shared_test_lib.BaseTestCase):
  """Tests for the event providers SQLite database writer."""

  # pylint: disable=protected-access

  # TODO: add test for _GetEventLogProviderKey
  # TODO: add test for _GetMessageFileKey

  def testWriteMessageFilesPerEventLogProvider(self):
    """Tests the WriteMessageFilesPerEventLogProvider function."""
    event_log_provider = resources.EventLogProvider()
    event_log_provider.identifier = '{f4aed7c7-a898-4627-b053-44a7caa12fcd}'
    event_log_provider.log_sources.append('Microsoft-Windows-RPC-Events')
    event_log_provider.log_types = ['Application']

    database_writer = database.EventProvidersSQLite3DatabaseWriter()

    with shared_test_lib.TempDirectory() as temporary_directory:
      test_file_path = os.path.join(temporary_directory, 'winevt-kb.db')
      database_writer.Open(test_file_path)

      database_writer.WriteEventLogProvider(event_log_provider)

      database_writer.WriteMessageFile(
          '%SystemRoot%\\system32\\rpcrt4.dll', 'rpcrt4.dll.db')

      database_writer.WriteMessageFilesPerEventLogProvider(
          event_log_provider, '%SystemRoot%\\system32\\rpcrt4.dll', 'event')

      database_writer.WriteMessageFilesPerEventLogProvider(
          event_log_provider, '%SystemRoot%\\system32\\rpcrt4.dll', 'event')

      database_writer.Close()

  def testWriteEventLogProvider(self):
    """Tests the WriteEventLogProvider function."""
    event_log_provider = resources.EventLogProvider()
    event_log_provider.identifier = '{f4aed7c7-a898-4627-b053-44a7caa12fcd}'
    event_log_provider.log_sources.append('Microsoft-Windows-RPC-Events')
    event_log_provider.log_types = ['Application']

    database_writer = database.EventProvidersSQLite3DatabaseWriter()

    with shared_test_lib.TempDirectory() as temporary_directory:
      test_file_path = os.path.join(temporary_directory, 'winevt-kb.db')
      database_writer.Open(test_file_path)

      database_writer.WriteEventLogProvider(event_log_provider)

      database_writer.WriteEventLogProvider(event_log_provider)

      database_writer.Close()

  def testWriteMessageFile(self):
    """Tests the WriteMessageFile function."""
    database_writer = database.EventProvidersSQLite3DatabaseWriter()

    with shared_test_lib.TempDirectory() as temporary_directory:
      test_file_path = os.path.join(temporary_directory, 'winevt-kb.db')
      database_writer.Open(test_file_path)

      database_writer.WriteMessageFile(
          '%SystemRoot%\\system32\\rpcrt4.dll', 'rpcrt4.dll.db')

      database_writer.WriteMessageFile(
          '%SystemRoot%\\system32\\rpcrt4.dll', 'rpcrt4.dll.db')

      database_writer.Close()


class MessageFileSQLite3DatabaseReaderTest(shared_test_lib.BaseTestCase):
  """Tests for the message file SQLite database reader."""

  def testGetMessageTables(self):
    """Tests the GetMessageTables function."""
    test_file_path = self._GetTestFilePath(['message_file.db'])
    self._SkipIfPathNotExists(test_file_path)

    database_reader = database.MessageFileSQLite3DatabaseReader()
    database_reader.Open(test_file_path)

    generator = database_reader.GetMessageTables()
    message_tables = list(generator)

    self.assertEqual(len(message_tables), 1)

    database_reader.Close()

  def testGetMessages(self):
    """Tests the GetMessages function."""
    test_file_path = self._GetTestFilePath(['message_file.db'])
    self._SkipIfPathNotExists(test_file_path)

    database_reader = database.MessageFileSQLite3DatabaseReader()
    database_reader.Open(test_file_path)

    generator = database_reader.GetMessages('0x00000409', '1.0.0.0')
    messages = list(generator)

    self.assertEqual(len(messages), 3)
    self.assertEqual(messages[0], ('0x00000001', 'Category\r\n'))

    generator = database_reader.GetMessages('0x00000413', '1.0.0.0')

    with self.assertRaises(errors.BackendError):
      list(generator)

    database_reader.Close()

  def testGetStringTables(self):
    """Tests the GetStringTables function."""
    test_file_path = self._GetTestFilePath(['message_file.db'])
    self._SkipIfPathNotExists(test_file_path)

    database_reader = database.MessageFileSQLite3DatabaseReader()
    database_reader.Open(test_file_path)

    generator = database_reader.GetStringTables()

    # TODO: string tables currently not written.
    with self.assertRaises(errors.BackendError):
      list(generator)

    database_reader.Close()

  def testGetStrings(self):
    """Tests the GetStrings function."""
    test_file_path = self._GetTestFilePath(['message_file.db'])
    self._SkipIfPathNotExists(test_file_path)

    database_reader = database.MessageFileSQLite3DatabaseReader()
    database_reader.Open(test_file_path)

    generator = database_reader.GetStrings('0x00000409', '1.0.0.0')

    # TODO: string tables currently not written.
    with self.assertRaises(errors.BackendError):
      list(generator)

    database_reader.Close()


class MessageResourceFileSQLite3DatabaseWriterTest(
    shared_test_lib.BaseTestCase):
  """Tests for the Event Log message resource file SQLite database writer."""

  # pylint: disable=protected-access

  def testGetMessageFileKey(self):
    """Tests the _GetMessageFileKey function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\wrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      database_writer = database.MessageResourceFileSQLite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, 'message_file.db')
        database_writer.Open(test_file_path)

        database_writer._WriteMessageFile(message_resource_file)

        message_file_key = database_writer._GetMessageFileKey(
            message_resource_file)
        self.assertEqual(message_file_key, 1)

        database_writer.Close()

      message_resource_file.Close()

  def testWriteMessage(self):
    """Tests the _WriteMessage function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\wrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      message_table_resource = message_resource_file.GetMessageTableResource()

      database_writer = database.MessageResourceFileSQLite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, 'message_file.db')
        database_writer.Open(test_file_path)

        # TODO: implement test.
        # database_writer._WriteMessage(
        #    message_resource_file, message_table_resource, 0x00000409, 0,
        #    'message_table_0x00000409', False)
        _ = message_table_resource

        database_writer.Close()

      message_resource_file.Close()

  def testWriteMessageFile(self):
    """Tests the _WriteMessageFile function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\wrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      database_writer = database.MessageResourceFileSQLite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, 'message_file.db')
        database_writer.Open(test_file_path)

        database_writer._WriteMessageFile(message_resource_file)

        database_writer.Close()

      message_resource_file.Close()

  def testWriteMessageTable(self):
    """Tests the _WriteMessageTable function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\wrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      wrc_resource = message_resource_file.GetMessageTableResource()
      resource_data = wrc_resource.items[0].sub_items[0].read()

      message_table_resource = pywrc.message_table_resource()
      message_table_resource.copy_from_byte_stream(resource_data)

      database_writer = database.MessageResourceFileSQLite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, 'message_file.db')
        database_writer.Open(test_file_path)

        database_writer._WriteMessageFile(message_resource_file)

        database_writer._WriteMessageTable(
            message_resource_file, message_table_resource, 0x00000409)

        database_writer._WriteMessageTable(
            message_resource_file, message_table_resource, 0x00000409)

        database_writer.Close()

      message_resource_file.Close()

  def testWriteMessageTableLanguage(self):
    """Tests the _WriteMessageTableLanguage function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\wrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      database_writer = database.MessageResourceFileSQLite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, 'message_file.db')
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

  def testWriteMessageTables(self):
    """Tests the _WriteMessageTables function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\wrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      database_writer = database.MessageResourceFileSQLite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, 'message_file.db')
        database_writer.Open(test_file_path)

        database_writer._WriteMessageFile(message_resource_file)

        database_writer._WriteMessageTables()

        database_writer.Close()

      message_resource_file.Close()

  # TODO: add tests for _WriteString.

  def testWriteStringTable(self):
    """Tests the _WriteStringTable function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\wrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      wrc_resource = message_resource_file.GetStringTableResource()
      wrc_resource_item = wrc_resource.items[0]
      resource_data = wrc_resource_item.sub_items[0].read()

      string_table_resource = pywrc.string_table_resource()
      string_table_resource.copy_from_byte_stream(
          resource_data, wrc_resource_item.identifier)

      database_writer = database.MessageResourceFileSQLite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, 'message_file.db')
        database_writer.Open(test_file_path)

        database_writer._WriteMessageFile(message_resource_file)

        database_writer._WriteStringTable(
            message_resource_file, string_table_resource, 0x00000409)

        database_writer.Close()

      message_resource_file.Close()

  def testWriteStringTableLanguage(self):
    """Tests the _WriteStringTableLanguage function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\wrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      database_writer = database.MessageResourceFileSQLite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, 'message_file.db')
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

  def testWriteStringTables(self):
    """Tests the _WriteStringTables function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\wrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      database_writer = database.MessageResourceFileSQLite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, 'message_file.db')
        database_writer.Open(test_file_path)

        database_writer._WriteMessageFile(message_resource_file)

        database_writer._WriteStringTables()

        database_writer.Close()

      message_resource_file.Close()

  def testWriteResources(self):
    """Tests the WriteResources function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\wrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      database_writer = database.MessageResourceFileSQLite3DatabaseWriter(
          message_resource_file)

      with shared_test_lib.TempDirectory() as temporary_directory:
        test_file_path = os.path.join(temporary_directory, 'message_file.db')
        database_writer.Open(test_file_path)

        database_writer.WriteResources()

        database_writer.Close()

      message_resource_file.Close()


class ResourcesSQLite3DatabaseReaderTest(shared_test_lib.BaseTestCase):
  """Tests for the resources SQLite database reader."""

  # pylint: disable=protected-access

  def testGetEventLogProviderKey(self):
    """Tests the _GetEventLogProviderKey function."""
    test_file_path = self._GetTestFilePath(['winevt-rc.db'])
    self._SkipIfPathNotExists(test_file_path)

    database_reader = database.ResourcesSQLite3DatabaseReader()
    database_reader.Open(test_file_path)

    database_reader._GetEventLogProviderKey('Security')

    database_reader.Close()

  # TODO: add test for _GetMessage
  # TODO: add test for _GetMessageFileKeys
  # TODO: add test for _GetMessageFilenames
  # TODO: add test for _GetMessages

  def testGetEventLogProviders(self):
    """Tests the GetEventLogProviders function."""
    test_file_path = self._GetTestFilePath(['winevt-rc.db'])
    self._SkipIfPathNotExists(test_file_path)

    database_reader = database.ResourcesSQLite3DatabaseReader()
    database_reader.Open(test_file_path)

    database_reader.GetEventLogProviders()

    database_reader.Close()

  # TODO: add test for GetMessage

  def testGetMessages(self):
    """Tests the GetMessages function."""
    test_file_path = self._GetTestFilePath(['winevt-rc.db'])
    self._SkipIfPathNotExists(test_file_path)

    database_reader = database.ResourcesSQLite3DatabaseReader()
    database_reader.Open(test_file_path)

    database_reader.GetMessages('bogus', 0x00000409)

    database_reader.Close()

  def testGetMetadataAttribute(self):
    """Tests the GetMetadataAttribute function."""
    test_file_path = self._GetTestFilePath(['winevt-rc.db'])
    self._SkipIfPathNotExists(test_file_path)

    database_reader = database.ResourcesSQLite3DatabaseReader()
    database_reader.Open(test_file_path)

    database_reader.GetMetadataAttribute('bogus')

    database_reader.Close()


class ResourcesSQLite3DatabaseWriterTest(shared_test_lib.BaseTestCase):
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

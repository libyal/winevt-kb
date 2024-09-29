#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests to read from and write SQLite databases."""

import os
import unittest

from winevtrc import database
from winevtrc import errors

from tests import test_lib


class SQLite3DatabaseFileTest(test_lib.BaseTestCase):
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

    with test_lib.TempDirectory() as temporary_directory:
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

    with test_lib.TempDirectory() as temporary_directory:
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

    with test_lib.TempDirectory() as temporary_directory:
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

    with test_lib.TempDirectory() as temporary_directory:
      test_file_path = os.path.join(temporary_directory, 'winevt-rc.db')
      database_file.Open(test_file_path, read_only=True)

      with self.assertRaises(IOError):
        database_file.InsertValues(table_name, column_names, values)

      database_file.Close()


class ResourcesSQLite3DatabaseReaderTest(test_lib.BaseTestCase):
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


class ResourcesSQLite3DatabaseWriterTest(test_lib.BaseTestCase):
  """Tests for the resources SQLite database writer."""

  # pylint: disable=protected-access

  # TODO: add test for _GetEventLogProviderKey
  # TODO: add test for _GetMessageFileKey
  # TODO: add test for _GetMessageFileKeyByPath
  # TODO: add test for _ReformatMessageString
  # TODO: add test for _WriteMessage
  # TODO: add test for _WriteMessageTableLanguage
  # TODO: add test for _WriteMetadataAttribute
  # TODO: add test for WriteEventLogProvider
  # TODO: add test for WriteMessageFile
  # TODO: add test for WriteMessageFilesPerEventLogProvider
  # TODO: add test for WriteMessageTable
  # TODO: add test for WriteMetadata


if __name__ == '__main__':
  unittest.main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests to read from and write SQLite databases."""

import os
import unittest

import sqlite3

from winevtrc import database

from tests import test_lib as shared_test_lib


class Sqlite3DatabaseFileTest(shared_test_lib.BaseTestCase):
  """Tests for the SQLite database file."""

  @shared_test_lib.skipUnlessHasTestFile([u'winevt-rc.db'])
  def testOpenClose(self):
    """Tests the Open and Close functions."""
    database_file = database.Sqlite3DatabaseFile()

    test_file_path = self._GetTestFilePath([u'winevt-rc.db'])
    database_file.Open(test_file_path, read_only=True)

    database_file.Close()

  def testCreateTable(self):
    """Tests the CreateTable function."""
    database_file = database.Sqlite3DatabaseFile()
    table_name = u'event_log_providers'
    column_names = [u'log_source', u'log_type', u'provider_guid']

    with shared_test_lib.TempDirectory() as temporary_directory:
      test_file_path = os.path.join(temporary_directory, u'winevt-rc.db')
      database_file.Open(test_file_path)

      database_file.CreateTable(table_name, column_names)

      database_file.Close()

    with self.assertRaises(RuntimeError):
      database_file.CreateTable(table_name, column_names)

  @shared_test_lib.skipUnlessHasTestFile([u'winevt-rc.db'])
  def testGetValues(self):
    """Tests the GetValues function."""
    database_file = database.Sqlite3DatabaseFile()

    test_file_path = self._GetTestFilePath([u'winevt-rc.db'])
    database_file.Open(test_file_path, read_only=True)

    generator = database_file.GetValues(
        [u'metadata'], [u'name', u'value'], u'')
    values_dict = next(generator)
    self.assertIsNotNone(values_dict)

    generator = database_file.GetValues(
        [u'bogus'], [u'name', u'value'], u'')

    with self.assertRaises(sqlite3.OperationalError):
      values_dict = next(generator)

    database_file.Close()

    # TODO: change to IOError.
    # TODO: determine why this not raises.
    # with self.assertRaises(RuntimeError):
    #   database_file.GetValues([u'metadata'], [u'name', u'value'], u'')

  @shared_test_lib.skipUnlessHasTestFile([u'winevt-rc.db'])
  def testHasTable(self):
    """Tests the HasTable function."""
    database_file = database.Sqlite3DatabaseFile()

    test_file_path = self._GetTestFilePath([u'winevt-rc.db'])
    database_file.Open(test_file_path, read_only=True)

    result = database_file.HasTable(u'metadata')
    self.assertTrue(result)

    result = database_file.HasTable(u'bogus')
    self.assertFalse(result)

    database_file.Close()

    # TODO: change to IOError.
    with self.assertRaises(RuntimeError):
      database_file.HasTable(u'metadata')

  def testInsertValues(self):
    """Tests the InsertValues function."""
    database_file = database.Sqlite3DatabaseFile()
    table_name = u'event_log_providers'
    column_names = [u'log_source', u'log_type', u'provider_guid']

    with shared_test_lib.TempDirectory() as temporary_directory:
      test_file_path = os.path.join(temporary_directory, u'winevt-rc.db')
      database_file.Open(test_file_path)

      database_file.CreateTable(table_name, column_names)

      # TODO: add call to InsertValues

      database_file.Close()

    # TODO: add call to InsertValues
    # with self.assertRaises(RuntimeError):
    #   database_file.InsertValues()


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

  # TODO: add tests.


class EventProvidersSqlite3DatabaseReaderTest(shared_test_lib.BaseTestCase):
  """Tests for the event providers SQLite database reader."""

  # TODO: add tests.


class EventProvidersSqlite3DatabaseWriter(shared_test_lib.BaseTestCase):
  """Tests for the event providers SQLite database writer."""

  # TODO: add tests.


class MessageFileSqlite3DatabaseReaderTest(shared_test_lib.BaseTestCase):
  """Tests for the message file SQLite database reader."""

  # TODO: add tests.


class MessageFileSqlite3DatabaseWriter(shared_test_lib.BaseTestCase):
  """Tests for the message file SQLite database writer."""

  # TODO: add tests.


class ResourcesSqlite3DatabaseReaderTest(shared_test_lib.BaseTestCase):
  """Tests for the resources SQLite database reader."""

  # TODO: add tests.


class ResourcesSqlite3DatabaseWriter(shared_test_lib.BaseTestCase):
  """Tests for the resources SQLite database writer."""

  # TODO: add tests.


if __name__ == '__main__':
  unittest.main()

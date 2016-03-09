#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for the fake Windows Registry back-end."""

import os
import unittest

from winevtrc import resource_file


class MessageResourceFileTest(unittest.TestCase):
  """Tests for the Windows Message Resource file object."""

  # Show full diff results, part of TestCase so does not follow our naming
  # conventions.
  maxDiff = None

  def testOpenFileObjectAndClose(self):
    """Tests the OpenFileObject and Close functions."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\sqlite3.dll')

    test_file = os.path.join(u'test_data', u'sqlite3.dll')
    file_object = open(test_file, 'rb')
    try:
      message_resource_file.OpenFileObject(file_object)

      with self.assertRaises(IOError):
        message_resource_file.OpenFileObject(file_object)

      message_resource_file.Close()
    finally:
      file_object.close()

    # TODO: add test on non PE/COFF file.
    # TODO: add test on PE/COFF file without resource section.

  def testGetVersionInformation(self):
    """Tests the GetVersionInformation function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\sqlite3.dll')

    test_file = os.path.join(u'test_data', u'sqlite3.dll')
    file_object = open(test_file, 'rb')
    try:
      message_resource_file.OpenFileObject(file_object)

      message_resource_file._GetVersionInformation()

      expected_file_version = u'3.11.1.0'
      self.assertEqual(
          message_resource_file.file_version, expected_file_version)

      expected_product_version = u'3.11.1.0'
      self.assertEqual(
          message_resource_file.product_version, expected_product_version)

    finally:
      message_resource_file.Close()
      file_object.close()

  def testGetMessageTableResource(self):
    """Tests the GetMessageTableResource function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\sqlite3.dll')

    test_file = os.path.join(u'test_data', u'sqlite3.dll')
    file_object = open(test_file, 'rb')
    try:
      message_resource_file.OpenFileObject(file_object)

      message_table_resource = message_resource_file.GetMessageTableResource()
      self.assertIsNone(message_table_resource)

    finally:
      message_resource_file.Close()
      file_object.close()

  def testGetStringResource(self):
    """Tests the GetStringResource function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\sqlite3.dll')

    test_file = os.path.join(u'test_data', u'sqlite3.dll')
    file_object = open(test_file, 'rb')
    try:
      message_resource_file.OpenFileObject(file_object)

      string_resource = message_resource_file.GetStringResource()
      self.assertIsNone(string_resource)

    finally:
      message_resource_file.Close()
      file_object.close()


if __name__ == '__main__':
  unittest.main()

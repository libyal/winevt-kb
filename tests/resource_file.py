#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for the Windows Message Resource file class."""

import os
import unittest

from winevtrc import resource_file

from tests import test_lib as shared_test_lib


class MessageResourceFileTest(shared_test_lib.BaseTestCase):
  """Tests for the Windows Message Resource file object."""

  # pylint: disable=protected-access

  @shared_test_lib.skipUnlessHasTestFile([u'wrc_test.dll'])
  def testOpenFileObjectAndClose(self):
    """Tests the OpenFileObject and Close functions."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\wrc_test.dll')

    test_path = self._GetTestFilePath([u'wrc_test.dll'])
    file_object = open(test_path, 'rb')
    try:
      message_resource_file.OpenFileObject(file_object)

      with self.assertRaises(IOError):
        message_resource_file.OpenFileObject(file_object)

      message_resource_file.Close()
    finally:
      file_object.close()

    # TODO: add test on non PE/COFF file.
    # TODO: add test on PE/COFF file without resource section.

  @shared_test_lib.skipUnlessHasTestFile([u'wrc_test.dll'])
  def testGetVersionInformation(self):
    """Tests the GetVersionInformation function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\wrc_test.dll')

    test_path = self._GetTestFilePath([u'wrc_test.dll'])
    file_object = open(test_path, 'rb')
    try:
      message_resource_file.OpenFileObject(file_object)

      message_resource_file._GetVersionInformation()

      expected_file_version = u'1.0.0.0'
      self.assertEqual(
          message_resource_file.file_version, expected_file_version)

      expected_product_version = u'1.0.0.0'
      self.assertEqual(
          message_resource_file.product_version, expected_product_version)

    finally:
      message_resource_file.Close()
      file_object.close()

  @shared_test_lib.skipUnlessHasTestFile([u'wrc_test.dll'])
  def testGetMessageTableResource(self):
    """Tests the GetMessageTableResource function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\wrc_test.dll')

    test_path = self._GetTestFilePath([u'wrc_test.dll'])
    file_object = open(test_path, 'rb')
    try:
      message_resource_file.OpenFileObject(file_object)

      message_table_resource = message_resource_file.GetMessageTableResource()
      self.assertIsNone(message_table_resource)

    finally:
      message_resource_file.Close()
      file_object.close()

  # TODO: add test for GetMUILanguage

  @shared_test_lib.skipUnlessHasTestFile([u'wrc_test.dll'])
  def testGetStringResource(self):
    """Tests the GetStringResource function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\wrc_test.dll')

    test_path = self._GetTestFilePath([u'wrc_test.dll'])
    file_object = open(test_path, 'rb')
    try:
      message_resource_file.OpenFileObject(file_object)

      string_resource = message_resource_file.GetStringResource()
      self.assertIsNone(string_resource)

    finally:
      message_resource_file.Close()
      file_object.close()


if __name__ == '__main__':
  unittest.main()

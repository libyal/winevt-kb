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

  # TODO: add open/close test on non PE/COFF file.

  @shared_test_lib.skipUnlessHasTestFile([u'nowrc_test.dll'])
  def testOpenFileObjectAndCloseNoWrc(self):
    """Tests the OpenFileObject and Close functions."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\nowrc_test.dll')

    test_file = self._GetTestFilePath([u'nowrc_test.dll'])
    with open(test_file, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      with self.assertRaises(IOError):
        message_resource_file.Close()

  @shared_test_lib.skipUnlessHasTestFile([u'wrc_test.dll'])
  def testOpenFileObjectAndCloseWrc(self):
    """Tests the OpenFileObject and Close functions."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\wrc_test.dll')

    test_file = self._GetTestFilePath([u'wrc_test.dll'])
    with open(test_file, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      with self.assertRaises(IOError):
        message_resource_file.OpenFileObject(file_object)

      message_resource_file.Close()

  @shared_test_lib.skipUnlessHasTestFile([u'nowrc_test.dll'])
  def testGetVersionInformationNoWrc(self):
    """Tests the GetVersionInformation function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\nowrc_test.dll')

    test_file = self._GetTestFilePath([u'nowrc_test.dll'])
    with open(test_file, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      with self.assertRaises(IOError):
        message_resource_file._GetVersionInformation()

  @shared_test_lib.skipUnlessHasTestFile([u'wrc_test.dll'])
  def testGetVersionInformationWrc(self):
    """Tests the GetVersionInformation function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\wrc_test.dll')

    test_file = self._GetTestFilePath([u'wrc_test.dll'])
    with open(test_file, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      message_resource_file._GetVersionInformation()

      expected_file_version = u'1.0.0.0'
      self.assertEqual(
          message_resource_file.file_version, expected_file_version)

      expected_product_version = u'1.0.0.0'
      self.assertEqual(
          message_resource_file.product_version, expected_product_version)

      message_resource_file.Close()

  @shared_test_lib.skipUnlessHasTestFile([u'nowrc_test.dll'])
  def testGetMessageTableResourceNoWrc(self):
    """Tests the GetMessageTableResource function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\nowrc_test.dll')

    test_file = self._GetTestFilePath([u'nowrc_test.dll'])
    with open(test_file, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      with self.assertRaises(IOError):
        message_resource_file.GetMessageTableResource()

  @shared_test_lib.skipUnlessHasTestFile([u'wrc_test.dll'])
  def testGetMessageTableResourceWrc(self):
    """Tests the GetMessageTableResource function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\wrc_test.dll')

    test_file = self._GetTestFilePath([u'wrc_test.dll'])
    with open(test_file, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      message_table_resource = message_resource_file.GetMessageTableResource()
      self.assertIsNotNone(message_table_resource)

      message_resource_file.Close()

  # TODO: add test for GetMUILanguage

  @shared_test_lib.skipUnlessHasTestFile([u'nowrc_test.dll'])
  def testGetStringResourceNoWrc(self):
    """Tests the GetStringResource function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\nowrc_test.dll')

    test_file = self._GetTestFilePath([u'nowrc_test.dll'])
    with open(test_file, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      with self.assertRaises(IOError):
        message_resource_file.GetStringResource()

  @shared_test_lib.skipUnlessHasTestFile([u'wrc_test.dll'])
  def testGetStringResourceWrc(self):
    """Tests the GetStringResource function."""
    message_resource_file = resource_file.MessageResourceFile(
        u'C:\\Windows\\System32\\wrc_test.dll')

    test_file = self._GetTestFilePath([u'wrc_test.dll'])
    with open(test_file, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      string_resource = message_resource_file.GetStringResource()
      self.assertIsNotNone(string_resource)

      message_resource_file.Close()


if __name__ == '__main__':
  unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the Windows Message Resource file class."""

import unittest

from winevtrc import resource_file

from tests import test_lib as shared_test_lib


class TestVersionResource(object):
  """Windows Resource Compiler (WRC) version resource for testing.

  Attributes:
    language_identifiers (list[int]): language identifiers.
    versions (dict[int, int]): versions per language identifier.
  """

  def __init__(self):
    """Initializes a version resource."""
    super(TestVersionResource, self).__init__()
    self.file_versions = {0x0409: 0}
    self.language_identifiers = [0x0409]
    self.product_versions = {0x0409: 2 << 48}

  # pylint: disable=invalid-name

  def get_file_version(self, language_identifier):
    """Retrieves the file version.

    Args:
      language_identifier (int): language identifier.

    Returns:
      int: file version.
    """
    return self.file_versions.get(language_identifier, 0)

  def get_product_version(self, language_identifier):
    """Retrieves the product version.

    Args:
      language_identifier (int): language identifier.

    Returns:
      int: product version.
    """
    return self.product_versions.get(language_identifier, 0)


class TestWrcStream(object):
  """Windows Resource Compiler (WRC) stream for testing.

  Attributes:
    resources (dict[int|str, object]): resources per identifier.
  """

  def __init__(self):
    """Initializes a version resource."""
    super(TestWrcStream, self).__init__()
    self.resources = {}

  # pylint: disable=invalid-name

  def get_resource_by_identifier(self, identifier):
    """Retrieves a specific resource by identifier.

    Args:
      identifier (int): identifier.

    Returns:
      object: resource or None.
    """
    return self.resources.get(identifier, None)

  def get_resource_by_name(self, name):
    """Retrieves a specific resource by name.

    Args:
      name (str): name.

    Returns:
      object: resource or None.
    """
    return self.resources.get(name, None)


class MessageResourceFileTest(shared_test_lib.BaseTestCase):
  """Tests for the Windows Message Resource file object."""

  # pylint: disable=protected-access

  def testGetVersionInformationNoWrc(self):
    """Tests the _GetVersionInformation function."""
    test_file_path = self._GetTestFilePath(['nowrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\nowrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      with self.assertRaises(IOError):
        message_resource_file._GetVersionInformation()

  def testGetVersionInformationWrc(self):
    """Tests the _GetVersionInformation function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\wrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      message_resource_file._GetVersionInformation()

      self.assertEqual(message_resource_file.file_version, '1.0.0.0')
      self.assertEqual(message_resource_file.product_version, '1.0.0.0')

      message_resource_file.Close()

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\test.dll')

    # Test with an empty WRC stream.
    wrc_stream = TestWrcStream()

    message_resource_file._wrc_stream = wrc_stream

    message_resource_file._GetVersionInformation()
    self.assertIsNone(message_resource_file.file_version)
    self.assertIsNone(message_resource_file.product_version)

    # Test with empty version information.
    wrc_stream.resources[0x10] = TestVersionResource()

    message_resource_file._wrc_stream = wrc_stream

    message_resource_file._GetVersionInformation()
    self.assertEqual(message_resource_file.file_version, '0.0.0.0')
    self.assertEqual(message_resource_file.product_version, '2.0.0.0')

  def testFileVersionProperty(self):
    """Tests the file_version property."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\wrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      self.assertEqual(message_resource_file.file_version, '1.0.0.0')

      message_resource_file.Close()

  def testProductVersionProperty(self):
    """Tests the product_version property."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\wrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      self.assertEqual(message_resource_file.product_version, '1.0.0.0')

      message_resource_file.Close()

  # TODO: add open/close test on non PE/COFF file.

  def testOpenFileObjectAndCloseNoWrc(self):
    """Tests the OpenFileObject and Close functions."""
    test_file_path = self._GetTestFilePath(['nowrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\nowrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      with self.assertRaises(IOError):
        message_resource_file.Close()

  def testOpenFileObjectAndCloseWrc(self):
    """Tests the OpenFileObject and Close functions."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\wrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      with self.assertRaises(IOError):
        message_resource_file.OpenFileObject(file_object)

      message_resource_file.Close()

  def testGetMessageTableResourceNoWrc(self):
    """Tests the GetMessageTableResource function."""
    test_file_path = self._GetTestFilePath(['nowrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\nowrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      with self.assertRaises(IOError):
        message_resource_file.GetMessageTableResource()

  def testGetMessageTableResourceWrc(self):
    """Tests the GetMessageTableResource function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\wrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      message_table_resource = message_resource_file.GetMessageTableResource()
      self.assertIsNotNone(message_table_resource)

      message_resource_file.Close()

  def testGetMUILanguage(self):
    """Tests the GetMUILanguage function."""
    test_file_path = self._GetTestFilePath(['wrc_test.mui.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      mui_language = message_resource_file.GetMUILanguage()
      self.assertEqual(mui_language, 'en-US')

      message_resource_file.Close()

    # Test with an empty WRC stream.
    wrc_stream = TestWrcStream()

    message_resource_file._wrc_stream = wrc_stream

    mui_language = message_resource_file.GetMUILanguage()
    self.assertIsNone(mui_language)

  def testGetStringResourceNoWrc(self):
    """Tests the GetStringResource function."""
    test_file_path = self._GetTestFilePath(['nowrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\nowrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      with self.assertRaises(IOError):
        message_resource_file.GetStringResource()

  def testGetStringResourceWrc(self):
    """Tests the GetStringResource function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    message_resource_file = resource_file.MessageResourceFile(
        'C:\\Windows\\System32\\wrc_test.dll')

    with open(test_file_path, 'rb') as file_object:
      message_resource_file.OpenFileObject(file_object)

      string_resource = message_resource_file.GetStringResource()
      self.assertIsNotNone(string_resource)

      message_resource_file.Close()


if __name__ == '__main__':
  unittest.main()

# -*- coding: utf-8 -*-
"""Tests for the file system helper."""

import pathlib
import platform
import unittest

from winevtrc import file_system

from tests import test_lib


class NativeFileSystemHelperTest(test_lib.BaseTestCase):
  """Python native system helper tests."""

  def testBasenamePath(self):
    """Tests the BasenamePath function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    test_helper = file_system.NativeFileSystemHelper()

    basename = test_helper.BasenamePath(test_file_path)
    self.assertEqual(basename, 'wrc_test.dll')

  def testCheckFileExistsByPath(self):
    """Tests the CheckFileExistsByPath function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    test_helper = file_system.NativeFileSystemHelper()

    result = test_helper.CheckFileExistsByPath(test_file_path)
    self.assertTrue(result)

  def testDirnamePath(self):
    """Tests the DirnamePath function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    test_helper = file_system.NativeFileSystemHelper()

    dirname = test_helper.DirnamePath(test_file_path)
    self.assertEqual(dirname, test_lib.TEST_DATA_PATH)

  def testGetFileSizeByPath(self):
    """Tests the GetFileSizeByPath function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    test_helper = file_system.NativeFileSystemHelper()

    file_size = test_helper.GetFileSizeByPath(test_file_path)
    self.assertEqual(file_size, 9728)

  def testJoinPath(self):
    """Tests the JoinPath function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    test_helper = file_system.NativeFileSystemHelper()

    path_segments = list(pathlib.Path(test_file_path).parts)
    path_segments.pop(0)

    if platform.system() == 'Windows':
      expected_path = test_file_path[2:]
    else:
      expected_path = test_file_path

    path = test_helper.JoinPath(path_segments)
    self.assertEqual(path, expected_path)

  def testListDirectory(self):
    """Tests the ListDirectory function."""
    test_file_path = self._GetTestFilePath([''])
    self._SkipIfPathNotExists(test_file_path)

    test_helper = file_system.NativeFileSystemHelper()

    expected_directory_entries = [
        'SOFTWARE',
        'SYSTEM',
        'defragsvc.dll.db',
        'message_file.db',
        'nowrc_test.dll',
        'winevt-kb.db',
        'winevt-rc.db',
        'wrc_test.dll',
        'wrc_test.mui.dll']

    directory_entries = sorted(test_helper.ListDirectory(test_file_path))
    self.assertEqual(directory_entries, expected_directory_entries)

  def testOpenFileByPath(self):
    """Tests the OpenFileByPath function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    test_helper = file_system.NativeFileSystemHelper()

    file_object = test_helper.OpenFileByPath(test_file_path)
    self.assertIsNotNone(file_object)

    file_object.close()

  def testSplitPath(self):
    """Tests the SplitPath function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    test_helper = file_system.NativeFileSystemHelper()

    expected_path_segments = list(pathlib.Path(test_file_path).parts)
    expected_path_segments.pop(0)

    path_segments = test_helper.SplitPath(test_file_path)
    if platform.system() == 'Windows':
      path_segments.pop(0)

    self.assertEqual(path_segments, expected_path_segments)


if __name__ == '__main__':
  unittest.main()

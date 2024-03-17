# -*- coding: utf-8 -*-
"""Tests for the dfVFS helpers."""

import pathlib
import os
import unittest

from dfvfs.lib import definitions as dfvfs_definitions
from dfvfs.path import factory as path_spec_factory

from winevtrc import dfvfs_helpers

from tests import test_lib


class DFVFSFileSystemHelperTest(test_lib.BaseTestCase):
  """dfVFS file system helper tests."""

  def testBasenamePath(self):
    """Tests the BasenamePath function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    test_helper = dfvfs_helpers.DFVFSFileSystemHelper(None)

    path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_OS, location=test_file_path)
    test_helper.OpenFileSystem(path_spec)

    basename = test_helper.BasenamePath(test_file_path)
    self.assertEqual(basename, 'wrc_test.dll')

  def testCheckFileExistsByPath(self):
    """Tests the CheckFileExistsByPath function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    test_helper = dfvfs_helpers.DFVFSFileSystemHelper(None)

    path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_OS, location=test_file_path)
    test_helper.OpenFileSystem(path_spec)

    result = test_helper.CheckFileExistsByPath(test_file_path)
    self.assertTrue(result)

  def testDirnamePath(self):
    """Tests the DirnamePath function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    test_helper = dfvfs_helpers.DFVFSFileSystemHelper(None)

    path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_OS, location=test_file_path)
    test_helper.OpenFileSystem(path_spec)

    dirname = test_helper.DirnamePath(test_file_path)
    self.assertEqual(dirname, test_lib.TEST_DATA_PATH)

  def testGetFileSizeByPath(self):
    """Tests the GetFileSizeByPath function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    test_helper = dfvfs_helpers.DFVFSFileSystemHelper(None)

    path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_OS, location=test_file_path)
    test_helper.OpenFileSystem(path_spec)

    file_size = test_helper.GetFileSizeByPath(test_file_path)
    self.assertEqual(file_size, 9728)

  def testJoinPath(self):
    """Tests the JoinPath function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    test_helper = dfvfs_helpers.DFVFSFileSystemHelper(None)

    path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_OS, location=test_file_path)
    test_helper.OpenFileSystem(path_spec)

    path_segments = os.path.split(test_file_path)

    path = test_helper.JoinPath(path_segments)
    self.assertEqual(path, test_file_path)

  def testListDirectory(self):
    """Tests the ListDirectory function."""
    test_file_path = self._GetTestFilePath([''])
    self._SkipIfPathNotExists(test_file_path)

    test_helper = dfvfs_helpers.DFVFSFileSystemHelper(None)

    path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_OS, location=test_file_path)
    test_helper.OpenFileSystem(path_spec)

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

    test_helper = dfvfs_helpers.DFVFSFileSystemHelper(None)

    path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_OS, location=test_file_path)
    test_helper.OpenFileSystem(path_spec)

    file_object = test_helper.OpenFileByPath(test_file_path)
    self.assertIsNotNone(file_object)

    file_object.close()

  def testSplitPath(self):
    """Tests the SplitPath function."""
    test_file_path = self._GetTestFilePath(['wrc_test.dll'])
    self._SkipIfPathNotExists(test_file_path)

    test_helper = dfvfs_helpers.DFVFSFileSystemHelper(None)

    path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_OS, location=test_file_path)
    test_helper.OpenFileSystem(path_spec)

    expected_path_segments = list(pathlib.Path(test_file_path).parts)
    expected_path_segments.pop(0)

    path_segments = test_helper.SplitPath(test_file_path)
    self.assertEqual(path_segments, expected_path_segments)


# TODO: add test for SetDFVFSBackEnd
# TODO: add test for AddDFVFSCLIArguments
# TODO: add test for ParseDFVFSCLIArguments


if __name__ == '__main__':
  unittest.main()

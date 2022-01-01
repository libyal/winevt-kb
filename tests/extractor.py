#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the Windows Event Log message resource extractor class."""

import unittest

from dfvfs.helpers import fake_file_system_builder
from dfvfs.helpers import windows_path_resolver
from dfvfs.lib import definitions as dfvfs_definitions
from dfvfs.path import factory as path_spec_factory

from winevtrc import extractor
from winevtrc import resources

from tests import test_lib as shared_test_lib


class EventMessageStringRegistryFileReaderTest(shared_test_lib.BaseTestCase):
  """Tests for the Windows Registry file reader."""

  def testOpen(self):
    """Tests the Open function."""
    volume_scanner = extractor.EventMessageStringExtractor()

    file_reader = extractor.EventMessageStringRegistryFileReader(
        volume_scanner)

    test_file_path = self._GetTestFilePath(['SOFTWARE'])
    self._SkipIfPathNotExists(test_file_path)

    # TODO: implement tests.
    # file_reader.Open(test_file_path)

    # file_reader.Open('bogus')
    _ = file_reader
    _ = test_file_path


class EventMessageStringExtractorTest(shared_test_lib.BaseTestCase):
  """Tests for the Windows Event Log message resource extractor."""

  # pylint: disable=protected-access

  def _CreateTestEventMessageStringExtractor(self):
    """Creates an event message string extractor for testing.

    Returns:
      EventMessageStringExtractor: an event message string extractor.
    """
    file_system_builder = fake_file_system_builder.FakeFileSystemBuilder()

    test_file_path = self._GetTestFilePath(['SOFTWARE'])
    self._SkipIfPathNotExists(test_file_path)
    file_system_builder.AddFileReadData(
        '/Windows/System32/config/SOFTWARE', test_file_path)

    test_file_path = self._GetTestFilePath(['SYSTEM'])
    self._SkipIfPathNotExists(test_file_path)
    file_system_builder.AddFileReadData(
        '/Windows/System32/config/SYSTEM', test_file_path)

    mount_point = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_FAKE, location='/')

    extractor_object = extractor.EventMessageStringExtractor()

    extractor_object._file_system = file_system_builder.file_system
    extractor_object._path_resolver = (
        windows_path_resolver.WindowsPathResolver(
            file_system_builder.file_system, mount_point))
    extractor_object._windows_directory = 'C:\\Windows'

    extractor_object._path_resolver.SetEnvironmentVariable(
        'SystemRoot', extractor_object._windows_directory)
    extractor_object._path_resolver.SetEnvironmentVariable(
        'WinDir', extractor_object._windows_directory)

    return extractor_object

  def testWindowsVersionProperty(self):
    """Tests the windows_version property."""
    extractor_object = self._CreateTestEventMessageStringExtractor()

    windows_version = extractor_object.windows_version
    # TODO: improve test.
    self.assertIsNone(windows_version)

  def testGetSystemRoot(self):
    """Tests the _GetSystemRoot function."""
    extractor_object = self._CreateTestEventMessageStringExtractor()

    system_root = extractor_object._GetSystemRoot()
    self.assertEqual(system_root, 'C:\\Windows')

  def testGetWindowsVersion(self):
    """Tests the _GetWindowsVersion function."""
    extractor_object = self._CreateTestEventMessageStringExtractor()

    windows_version = extractor_object._GetWindowsVersion()
    # TODO: improve test.
    self.assertIsNone(windows_version)

  def testOpenMessageResourceFile(self):
    """Tests the _OpenMessageResourceFile function."""
    extractor_object = self._CreateTestEventMessageStringExtractor()

    # TODO: improve test.

    message_resource_file = extractor_object._OpenMessageResourceFile(
        'C:\\Windows\\System32\\wrc_test.dll')
    self.assertIsNone(message_resource_file)

  # TODO: test _OpenMessageResourceFileByPathSpec

  def testCollectEventLogProviders(self):
    """Tests the CollectEventLogProviders function."""
    extractor_object = self._CreateTestEventMessageStringExtractor()

    event_log_providers = list(extractor_object.CollectEventLogProviders())

    self.assertEqual(len(event_log_providers), 974)

  def testGetMessageResourceFile(self):
    """Tests the GetMessageResourceFile function."""
    extractor_object = self._CreateTestEventMessageStringExtractor()

    # TODO: improve test.
    event_log_provider = resources.EventLogProvider(
        'log_type', 'log_source', 'provider_guid')
    message_filename = 'bogus'

    message_resource_file = extractor_object.GetMessageResourceFile(
        event_log_provider, message_filename)

    self.assertIsNone(message_resource_file)


if __name__ == '__main__':
  unittest.main()

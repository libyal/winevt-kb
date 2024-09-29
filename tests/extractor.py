#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the Windows Event Log message resource extractor class."""

import unittest

from dfimagetools import windows_registry

from dfvfs.helpers import fake_file_system_builder
from dfvfs.helpers import windows_path_resolver
from dfvfs.lib import definitions as dfvfs_definitions
from dfvfs.path import factory as path_spec_factory

from dfwinreg import registry as dfwinreg_registry

from winevtrc import extractor
from winevtrc import resources

from tests import test_lib


class EventMessageStringExtractorTest(test_lib.BaseTestCase):
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
    extractor_object._windows_directory = 'C:\\Windows'

    extractor_object._path_resolver = (
        windows_path_resolver.WindowsPathResolver(
            file_system_builder.file_system, mount_point))
    extractor_object._path_resolver.SetEnvironmentVariable(
        'SystemRoot', extractor_object._windows_directory)
    extractor_object._path_resolver.SetEnvironmentVariable(
        'WinDir', extractor_object._windows_directory)

    registry_file_reader = (
        windows_registry.StorageMediaImageWindowsRegistryFileReader(
            file_system_builder.file_system, extractor_object._path_resolver))
    extractor_object._registry = dfwinreg_registry.WinRegistry(
        registry_file_reader=registry_file_reader)

    return extractor_object

  def testWindowsVersionProperty(self):
    """Tests the windows_version property."""
    extractor_object = self._CreateTestEventMessageStringExtractor()

    windows_version = extractor_object.windows_version
    # TODO: improve test.
    self.assertIsNone(windows_version)

  # TODO: add tests for _GetMUIMessageResourceFile

  def testGetNormalizedPath(self):
    """Tests the _GetNormalizedPath function."""
    extractor_object = self._CreateTestEventMessageStringExtractor()

    normalized_path = extractor_object._GetNormalizedPath(
        '%SystemDrive%\\Windows\\System32\\IoLogMsg.dll')
    self.assertEqual(normalized_path, '%SystemRoot%\\System32\\IoLogMsg.dll')

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

  def testOpenWindowsResourceFile(self):
    """Tests the _OpenWindowsResourceFile function."""
    extractor_object = self._CreateTestEventMessageStringExtractor()

    # TODO: improve test.

    message_resource_file = extractor_object._OpenWindowsResourceFile(
        'C:\\Windows\\System32\\wrc_test.dll')
    self.assertIsNone(message_resource_file)

  # TODO: test _OpenWindowsResourceFileByPathSpec

  def testCollectEventLogProviders(self):
    """Tests the CollectEventLogProviders function."""
    extractor_object = self._CreateTestEventMessageStringExtractor()

    event_log_providers = list(extractor_object.CollectEventLogProviders())

    self.assertEqual(len(event_log_providers), 974)

  # TODO: test CollectSystemEnvironmentVariables

  def testGetMessageResourceFile(self):
    """Tests the GetMessageResourceFile function."""
    extractor_object = self._CreateTestEventMessageStringExtractor()

    # TODO: improve test.
    event_log_provider = resources.EventLogProvider()
    event_log_provider.identifier = 'provider_guid'
    event_log_provider.log_sources.append('log_source')
    event_log_provider.log_types = ['log_type']

    message_filename = 'bogus'
    message_resource_file = extractor_object.GetMessageResourceFile(
        event_log_provider, message_filename)

    self.assertIsNone(message_resource_file)

  def testGetNormalizedResourceFilePath(self):
    """Tests the GetNormalizedResourceFilePath function."""
    extractor_object = self._CreateTestEventMessageStringExtractor()

    normalized_path = extractor_object.GetNormalizedResourceFilePath(
        '%SystemRoot%\\System32\\IoLogMsg.dll')
    self.assertEqual(normalized_path, '%SystemRoot%\\System32\\IoLogMsg.dll')

    normalized_path = extractor_object.GetNormalizedResourceFilePath(
        '%windir%\\System32\\lsasrv.dll')
    self.assertEqual(normalized_path, '%SystemRoot%\\System32\\lsasrv.dll')

    normalized_path = extractor_object.GetNormalizedResourceFilePath(
        'C:\\Windows\\System32\\mscoree.dll')
    self.assertEqual(normalized_path, '%SystemRoot%\\System32\\mscoree.dll')

    normalized_path = extractor_object.GetNormalizedResourceFilePath(
        'werfault.exe')
    self.assertEqual(normalized_path, '%SystemRoot%\\System32\\werfault.exe')

    normalized_path = extractor_object.GetNormalizedResourceFilePath(
        'system32\\drivers\\WdFilter.sys')
    self.assertEqual(normalized_path, (
        '%SystemRoot%\\System32\\drivers\\WdFilter.sys'))

    normalized_path = extractor_object.GetNormalizedResourceFilePath(
        'C:\\Program Files\\Windows Defender\\MpClient.dll')
    self.assertEqual(normalized_path, (
        '%ProgramFiles%\\Windows Defender\\MpClient.dll'))

    normalized_path = extractor_object.GetNormalizedResourceFilePath(
        '%PROGRAMFILES%\\Windows Defender\\MpClient.dll')
    self.assertEqual(normalized_path, (
        '%ProgramFiles%\\Windows Defender\\MpClient.dll'))

    normalized_path = extractor_object.GetNormalizedResourceFilePath(
        'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\84.0.522.52\\'
        'eventlog_provider.dll')
    self.assertEqual(normalized_path, (
        '%ProgramFiles(x86)%\\Microsoft\\Edge\\Application\\84.0.522.52\\'
        'eventlog_provider.dll'))

    normalized_path = extractor_object.GetNormalizedResourceFilePath(
        '%PROGRAMFILES(X86)%\\Microsoft\\Edge\\Application\\84.0.522.52\\'
        'eventlog_provider.dll')
    self.assertEqual(normalized_path, (
        '%ProgramFiles(x86)%\\Microsoft\\Edge\\Application\\84.0.522.52\\'
        'eventlog_provider.dll'))

    normalized_path = extractor_object.GetNormalizedResourceFilePath(
        '%programdata%\\Microsoft\\Windows Defender\\Definition Updates\\'
        'Default\\MpEngine.dll')
    self.assertEqual(normalized_path, (
        '%programdata%\\Microsoft\\Windows Defender\\Definition Updates\\'
        'Default\\MpEngine.dll'))

    normalized_path = extractor_object.GetNormalizedResourceFilePath(
        '$(runtime.system32)\\WinML.dll')
    self.assertEqual(normalized_path, '%SystemRoot%\\System32\\WinML.dll')

    normalized_path = extractor_object.GetNormalizedResourceFilePath(
        '$(runtime.windows)\\immersivecontrolpanel\\systemsettings.exe')
    self.assertEqual(normalized_path, (
        '%SystemRoot%\\immersivecontrolpanel\\systemsettings.exe'))

  # TODO: test GetTemplateResourceFile

  # TODO: test ScanForWindowsVolume


if __name__ == '__main__':
  unittest.main()

#!/usr/bin/python
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


class TestOutputWriter(object):
  """Class that defines a test output writer.

  Attributes:
    event_log_providers (list[EventLogProvider]): event log providers.
    message_files (list[MessageFile]): message files.
  """

  def __init__(self):
    """Initializes the test output writer."""
    super(TestOutputWriter, self).__init__()
    self.event_log_providers = []
    self.message_files = []

  def Close(self):
    """Closes the output writer."""
    pass

  def Open(self):
    """Opens the output writer.

    Returns:
      bool: True if successful or False if not.
    """
    return True

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider (EventLogProvider): event log provider.
    """
    self.event_log_providers.append(event_log_provider)

  def WriteMessageFile(
      self, unused_event_log_provider, message_file, unused_message_filename,
      unused_message_type):
    """Writes the Windows Message Resource file.

    Args:
      event_log_provider (EventLogProvider): event log provider.
      message_file (MessageResourceFile): message resource file.
      message_filename (str): message filename.
      message_file_type (str): message file type.
    """
    self.message_files.append(message_file)


class EventMessageStringRegistryFileReaderTest(shared_test_lib.BaseTestCase):
  """Tests for the Windows Registry file reader."""

  def testOpen(self):
    """Tests the Open function."""
    volume_scanner = extractor.EventMessageStringExtractor()

    file_reader = extractor.EventMessageStringRegistryFileReader(
        volume_scanner)

    test_file_path = self._GetTestFilePath([u'SOFTWARE'])

    # TODO: implement tests.
    # file_reader.Open(test_file_path)

    # file_reader.Open(u'bogus')
    _ = file_reader
    _ = test_file_path


@shared_test_lib.skipUnlessHasTestFile([u'SOFTWARE'])
@shared_test_lib.skipUnlessHasTestFile([u'SYSTEM'])
class EventMessageStringExtractorTest(shared_test_lib.BaseTestCase):
  """Tests for the Windows Event Log message resource extractor."""

  # pylint: disable=protected-access

  def _CreateTestEventMessageStringExtractor(self):
    """Creates an event message string extractor for testing.

    Returns:
      EventMessageStringExtractor: an event message string extractor.
    """
    file_system_builder = fake_file_system_builder.FakeFileSystemBuilder()

    test_file_path = self._GetTestFilePath([u'SOFTWARE'])
    file_system_builder.AddFileReadData(
        u'/Windows/System32/config/SOFTWARE', test_file_path)

    test_file_path = self._GetTestFilePath([u'SYSTEM'])
    file_system_builder.AddFileReadData(
        u'/Windows/System32/config/SYSTEM', test_file_path)

    mount_point = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_FAKE, location=u'/')

    extractor_object = extractor.EventMessageStringExtractor()

    extractor_object._file_system = file_system_builder.file_system
    extractor_object._path_resolver = (
        windows_path_resolver.WindowsPathResolver(
            file_system_builder.file_system, mount_point))
    extractor_object._windows_directory = u'C:\\Windows'

    extractor_object._path_resolver.SetEnvironmentVariable(
        u'SystemRoot', extractor_object._windows_directory)
    extractor_object._path_resolver.SetEnvironmentVariable(
        u'WinDir', extractor_object._windows_directory)

    return extractor_object

  def testWindowsVersionProperty(self):
    """Tests the windows_version property."""
    extractor_object = self._CreateTestEventMessageStringExtractor()

    windows_version = extractor_object.windows_version
    # TODO: improve test.
    self.assertIsNone(windows_version)

  def testCollectEventLogTypes(self):
    """Tests the _CollectEventLogTypes function."""
    extractor_object = self._CreateTestEventMessageStringExtractor()

    event_log_types = extractor_object._CollectEventLogTypes()
    self.assertEqual(len(event_log_types), 3)
    self.assertEqual(len(event_log_types[u'Application']), 65)
    self.assertEqual(len(event_log_types[u'Security']), 7)
    self.assertEqual(len(event_log_types[u'System']), 186)

    # TODO: hide duplication warnings.
    event_log_types = extractor_object._CollectEventLogTypes(
        all_control_sets=True)
    self.assertEqual(len(event_log_types), 3)
    self.assertEqual(len(event_log_types[u'Application']), 65)
    self.assertEqual(len(event_log_types[u'Security']), 7)
    self.assertEqual(len(event_log_types[u'System']), 186)

  def testCollectEventLogProvidersFromKey(self):
    """Tests the _CollectEventLogProvidersFromKey function."""
    extractor_object = self._CreateTestEventMessageStringExtractor()

    generator = extractor_object._CollectEventLogProvidersFromKey(None)
    # TODO: fix generator method.
    self.assertIsNotNone(generator)

  def testExtractMessageFile(self):
    """Tests the _ExtractMessageFile function."""
    extractor_object = self._CreateTestEventMessageStringExtractor()

    # TODO: improve test.
    output_writer = TestOutputWriter()
    processed_message_filenames = []
    event_log_provider = resources.EventLogProvider(
        u'log_type', u'log_source', u'provider_guid')
    message_filename = u''
    message_file_type = u''

    extractor_object._ExtractMessageFile(
        output_writer, processed_message_filenames, event_log_provider,
        message_filename, message_file_type)

    self.assertEqual(len(output_writer.event_log_providers), 0)
    self.assertEqual(len(output_writer.message_files), 0)

  def testGetEventLogProviders(self):
    """Tests the _GetEventLogProviders function."""
    extractor_object = self._CreateTestEventMessageStringExtractor()

    event_log_providers = list(extractor_object._GetEventLogProviders())
    self.assertEqual(len(event_log_providers), 258)

    event_log_providers = list(
        extractor_object._GetEventLogProviders(all_control_sets=True))
    self.assertEqual(len(event_log_providers), 516)

  def testGetSystemRoot(self):
    """Tests the _GetSystemRoot function."""
    extractor_object = self._CreateTestEventMessageStringExtractor()

    system_root = extractor_object._GetSystemRoot()
    self.assertEqual(system_root, u'C:\\WINDOWS')

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
        u'C:\\Windows\\System32\\wrc_test.dll')
    self.assertIsNone(message_resource_file)

  # TODO: test _OpenMessageResourceFileByPathSpec

  def testExtractEventLogMessageStrings(self):
    """Tests the ExtractEventLogMessageStrings function."""
    extractor_object = self._CreateTestEventMessageStringExtractor()

    output_writer = TestOutputWriter()

    extractor_object.ExtractEventLogMessageStrings(output_writer)

    self.assertEqual(len(output_writer.event_log_providers), 258)
    self.assertEqual(len(output_writer.message_files), 0)


if __name__ == '__main__':
  unittest.main()

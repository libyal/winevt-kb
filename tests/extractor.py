#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for the Windows Event Log message resource extractor class."""

import unittest

from dfvfs.helpers import fake_file_system_builder
from dfvfs.helpers import windows_path_resolver
from dfvfs.lib import definitions as dfvfs_definitions
from dfvfs.path import factory as path_spec_factory

from winevtrc import extractor

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


class EventMessageStringExtractorTest(shared_test_lib.BaseTestCase):
  """Tests for the Windows Event Log message resource extractor."""

  # pylint: disable=protected-access

  @shared_test_lib.skipUnlessHasTestFile([u'SOFTWARE'])
  @shared_test_lib.skipUnlessHasTestFile([u'SYSTEM'])
  def testExtractEventLogMessageStrings(self):
    """Tests the ExtractEventLogMessageStrings function."""
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

    system_root = extractor_object._GetSystemRoot()
    self.assertEqual(system_root, u'C:\\WINDOWS')

    event_log_providers = list(extractor_object._GetEventLogProviders())
    self.assertEqual(len(event_log_providers), 258)

    event_log_providers = list(
        extractor_object._GetEventLogProviders(all_control_sets=True))
    self.assertEqual(len(event_log_providers), 516)

    output_writer = TestOutputWriter()

    extractor_object.ExtractEventLogMessageStrings(output_writer)

    self.assertEqual(len(output_writer.event_log_providers), 258)
    self.assertEqual(len(output_writer.message_files), 0)


if __name__ == '__main__':
  unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the Windows Event Log resources."""

import unittest

from winevtrc import resources

from tests import test_lib


class WinevtResourcesEventLogProviderTest(test_lib.BaseTestCase):
  """Tests for the Windows Event Log provider."""

  def testSetCategoryMessageFilenames(self):
    """Tests the SetCategoryMessageFilenames function."""
    event_log_provider = resources.WinevtResourcesEventLogProvider()
    event_log_provider.identifier = 'provider_guid'
    event_log_provider.log_sources.append('log_source')
    event_log_provider.log_types = ['log_type']

    expected_category_message_files = set(['test1', 'test2', 'test3'])

    event_log_provider.SetCategoryMessageFilenames(
        expected_category_message_files)
    self.assertEqual(
        event_log_provider.category_message_files,
        expected_category_message_files)

    event_log_provider.SetCategoryMessageFilenames('test1;test2;test3')
    self.assertEqual(
        event_log_provider.category_message_files,
        expected_category_message_files)

  def testSetEventMessageFilenames(self):
    """Tests the SetEventMessageFilenames function."""
    event_log_provider = resources.WinevtResourcesEventLogProvider()
    event_log_provider.identifier = 'provider_guid'
    event_log_provider.log_sources.append('log_source')
    event_log_provider.log_types = ['log_type']

    expected_event_message_files = set(['test1', 'test2', 'test3'])

    event_log_provider.SetEventMessageFilenames(
        expected_event_message_files)
    self.assertEqual(
        event_log_provider.event_message_files,
        expected_event_message_files)

    event_log_provider.SetEventMessageFilenames('test1;test2;test3')
    self.assertEqual(
        event_log_provider.event_message_files,
        expected_event_message_files)

  def testSetParameterMessageFilenames(self):
    """Tests the SetParameterMessageFilenames function."""
    event_log_provider = resources.WinevtResourcesEventLogProvider()
    event_log_provider.identifier = 'provider_guid'
    event_log_provider.log_sources.append('log_source')
    event_log_provider.log_types = ['log_type']

    expected_parameter_message_files = set(['test1', 'test2', 'test3'])

    event_log_provider.SetParameterMessageFilenames(
        expected_parameter_message_files)
    self.assertEqual(
        event_log_provider.parameter_message_files,
        expected_parameter_message_files)

    event_log_provider.SetParameterMessageFilenames('test1;test2;test3')
    self.assertEqual(
        event_log_provider.parameter_message_files,
        expected_parameter_message_files)


if __name__ == '__main__':
  unittest.main()

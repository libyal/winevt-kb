#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the Windows Event Log message resource exporter."""

import unittest

from winevtrc import exporter

from tests import test_lib


class ExporterTest(test_lib.BaseTestCase):
  """Tests for the Windows Event Log message resource exporter."""

  # pylint: disable=protected-access

  # TODO: add tests for _ExportEventLogProviders
  # TODO: add tests for _ExportMessageFile
  # TODO: add tests for _ExportMessageFiles
  # TODO: add tests for _ExportMessageFilesPerEventLogProvider
  # TODO: add tests for _ExportMessageStrings

  def testGetNormalizedPath(self):
    """Tests the _GetNormalizedPath function."""
    exporter_object = exporter.Exporter()

    normalized_path = exporter_object._GetNormalizedPath(
        '%SystemDrive%\\Windows\\System32\\IoLogMsg.dll')
    self.assertEqual(normalized_path, '%SystemRoot%\\System32\\IoLogMsg.dll')

  # TODO: add tests for Export


if __name__ == '__main__':
  unittest.main()

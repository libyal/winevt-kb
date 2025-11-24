#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for the Windows Event Log message resource exporter."""

import unittest

# from winevtrc import exporter

from tests import test_lib


class ExporterTest(test_lib.BaseTestCase):
  """Tests for the Windows Event Log message resource exporter."""

  # pylint: disable=protected-access

  # TODO: add tests for _ExportEventLogProviders
  # TODO: add tests for _ExportMessageFile
  # TODO: add tests for _ExportMessageFiles
  # TODO: add tests for _ExportMessageFilesPerEventLogProvider
  # TODO: add tests for _ExportMessageStrings
  # TODO: add tests for Export


if __name__ == '__main__':
  unittest.main()

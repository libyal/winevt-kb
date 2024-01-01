#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for the Windows language tags."""

import unittest

from winevtrc import language_tags

from tests import test_lib


class WindowsLanguageTagsTest(test_lib.BaseTestCase):
  """Tests for the Windows language tags."""

  def testGetLanguageTagForLCID(self):
    """Tests the GetLanguageTagForLCID function."""
    language_tag = language_tags.WindowsLanguageTags.GetLanguageTagForLCID(
        0x040f)
    self.assertEqual(language_tag, 'is-IS')

    language_tag = language_tags.WindowsLanguageTags.GetLanguageTagForLCID(
        0xffff)
    self.assertIsNone(language_tag)

  def testGetLCIDForLanguageTag(self):
    """Tests the GetLCIDForLanguageTag function."""
    lcid = language_tags.WindowsLanguageTags.GetLCIDForLanguageTag('is-IS')
    self.assertEqual(lcid, 0x040f)

    lcid = language_tags.WindowsLanguageTags.GetLCIDForLanguageTag('bogus')
    self.assertIsNone(lcid)


if __name__ == '__main__':
  unittest.main()

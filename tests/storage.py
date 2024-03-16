#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the Attribute container store."""

import unittest

from winevtrc import storage

from tests import test_lib


class JSONStringsListAttributeSerializerTest(test_lib.BaseTestCase):
  """Tests for the JSON strings list attribute serializer."""

  def testDeserializeValue(self):
    """Tests the DeserializeValue function."""
    serializer = storage.JSONStringsListAttributeSerializer()

    value = serializer.DeserializeValue([1, 2, 3])
    self.assertIsInstance(value, list)
    self.assertEqual(value, [1, 2, 3])

  def testSerializeValue(self):
    """Tests the SerializeValue function."""
    serializer = storage.JSONStringsListAttributeSerializer()

    value = serializer.SerializeValue([1, 2, 3])
    self.assertIsInstance(value, list)
    self.assertEqual(value, [1, 2, 3])


if __name__ == '__main__':
  unittest.main()

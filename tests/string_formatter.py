#!/usr/bin/env python3
"""Tests for the message string formatter."""

import unittest

from winevtrc import string_formatter

from tests import test_lib


class MessageStringFormatterTest(test_lib.BaseTestCase):
    """Tests for the message string formatter."""

    def testReformatMessageString(self):
        """Tests the ReformatMessageString function."""
        test_formatter = string_formatter.MessageStringFormatter()

        original_message_string = (
            "Sync info for %1%nServer copy exists, client copy replaced then "
            "deleted.%n%10\\%nSee details for more information."
        )
        message_string = test_formatter.FormatMessageStringInPEP3101(
            original_message_string
        )
        expected_message_string = (
            "Sync info for {0:s}\\nServer copy exists, client copy replaced then "
            "deleted.\\n{9:s}\\\\nSee details for more information."
        )
        self.assertEqual(message_string, expected_message_string)

        original_message_string = "User %1 logged in from host %2%0 at %3."
        message_string = test_formatter.FormatMessageStringInPEP3101(
            original_message_string
        )
        expected_message_string = "User {0:s} logged in from host {1:s}"
        self.assertEqual(message_string, expected_message_string)


if __name__ == "__main__":
    unittest.main()

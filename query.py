#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Script to query a winevt-kb SQLite database."""

# pylint: disable=superfluous-parens

import argparse
import logging
import sys

import database


def Main():
  """The main program function.

  Returns:
    A boolean containing True if successful or False if not.
  """
  args_parser = argparse.ArgumentParser(description=(
      'Export strings extracted from message files.'))

  args_parser.add_argument(
      'event_provider', nargs='?', action='store', metavar='EVENT_PROVIDER',
      default=None, help='The event provider.')

  args_parser.add_argument(
      'message_identifier', nargs='?', action='store',
      metavar='MESSAGE_IDENTIFIER', default=None,
      help='The message identifier.')

  args_parser.add_argument(
      '--db', dest='database', action='store', metavar='winevt-rc.db',
      default=None, help='filename of the sqlite3 database to read from.')

  # TODO: allow to set preferred language.
  lcid = 0x00000409

  options = args_parser.parse_args()

  if not options.event_provider or not options.message_identifier:
    print(u'Event provider or message identifier value is missing.')
    print(u'')
    args_parser.print_help()
    print(u'')
    return False

  logging.basicConfig(
      level=logging.INFO, format=u'[%(levelname)s] %(message)s')

  database_reader = database.Sqlite3ResourcesDatabaseReader()
  database_reader.Open(options.database)

  message_string = database_reader.GetMessage(
      options.event_provider, lcid, options.message_identifier)

  database_reader.Close()

  if message_string:
    print(u'Message string:')
    print(message_string)

  return True


if __name__ == '__main__':
  if not Main():
    sys.exit(1)
  else:
    sys.exit(0)

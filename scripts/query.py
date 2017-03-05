#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Script to query a winevt-kb SQLite database."""

from __future__ import print_function
import argparse
import logging
import sys

from winevtrc import database


def Main():
  """The main program function.

  Returns:
    A boolean containing True if successful or False if not.
  """
  argument_parser = argparse.ArgumentParser(description=(
      u'Export strings extracted from message files.'))

  argument_parser.add_argument(
      u'database', nargs=u'?', action=u'store', metavar=u'DATABASE',
      default=None, help=u'filename of the sqlite3 database to read from.')

  argument_parser.add_argument(
      u'event_provider', nargs=u'?', action=u'store', metavar=u'EVENT_PROVIDER',
      default=None, help=u'specific event provider to query.')

  argument_parser.add_argument(
      u'message_identifier', nargs=u'?', action=u'store',
      metavar=u'MESSAGE_IDENTIFIER', default=None,
      help=u'specific message identifier to query.')

  argument_parser.add_argument(
      u'--lcid', dest=u'lcid', action=u'store', metavar=u'LCID',
      default=0x00000409, help=u'the preferred LCID.')

  options = argument_parser.parse_args()

  if not options.database:
    print(u'Database value is missing.')
    print(u'')
    argument_parser.print_help()
    print(u'')
    return False

  logging.basicConfig(
      level=logging.INFO, format=u'[%(levelname)s] %(message)s')

  database_reader = database.ResourcesSqlite3DatabaseReader()
  database_reader.Open(options.database)

  message_identifier = None
  if getattr(options, u'message_identifier', None):
    try:
      message_identifier = int(options.message_identifier, 10)
    except ValueError:
      pass

    if message_identifier is None:
      try:
        message_identifier = int(options.message_identifier, 16)
      except ValueError:
        pass

    if message_identifier is None:
      print(u'Unsupported message identifier: {0:s}'.format(
          options.message_identifier))
      return False

  if not getattr(options, u'event_provider', None):
    print(u'Event Log providers:')
    for event_log_provider in database_reader.GetEventLogProviders():
      print(event_log_provider.log_source)

  elif message_identifier is None:
    print(u'Message strings:')
    for message_identifier, message_string in database_reader.GetMessages(
        options.event_provider, options.lcid):
      print(u'{0:s}:\t{1:s}'.format(message_identifier, message_string))

  else:
    message_string = database_reader.GetMessage(
        options.event_provider, options.lcid, message_identifier)

    print(u'Message string:')
    if message_string:
      print(u'0x{0:08x}:\t{1:s}'.format(message_identifier, message_string))

  database_reader.Close()

  return True


if __name__ == '__main__':
  if not Main():
    sys.exit(1)
  else:
    sys.exit(0)

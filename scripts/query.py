#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script to query a winevt-kb SQLite database."""

import argparse
import logging
import sys

from winevtrc import database


def Main():
  """The main program function.

  Returns:
    bool: True if successful or False if not.
  """
  argument_parser = argparse.ArgumentParser(description=(
      'Export strings extracted from message files.'))

  argument_parser.add_argument(
      'database', nargs='?', action='store', metavar='DATABASE',
      default=None, help='filename of the sqlite3 database to read from.')

  argument_parser.add_argument(
      'event_provider', nargs='?', action='store', metavar='EVENT_PROVIDER',
      default=None, help='specific event provider to query.')

  argument_parser.add_argument(
      'message_identifier', nargs='?', action='store',
      metavar='MESSAGE_IDENTIFIER', default=None,
      help='specific message identifier to query.')

  argument_parser.add_argument(
      '--lcid', dest='lcid', action='store', metavar='LCID', type=int,
      default=0x00000409, help='the preferred LCID.')

  options = argument_parser.parse_args()

  if not options.database:
    print('Database value is missing.')
    print('')
    argument_parser.print_help()
    print('')
    return False

  logging.basicConfig(
      level=logging.INFO, format='[%(levelname)s] %(message)s')

  database_reader = database.ResourcesSQLite3DatabaseReader()
  database_reader.Open(options.database)

  message_identifier = None
  if getattr(options, 'message_identifier', None):
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
      print('Unsupported message identifier: {0:s}'.format(
          options.message_identifier))
      return False

  if not getattr(options, 'event_provider', None):
    print('Event Log providers:')
    for event_log_provider in database_reader.GetEventLogProviders():
      print(event_log_provider.log_source)

  elif message_identifier is None:
    print('Message strings:')
    for message_identifier, message_string in database_reader.GetMessages(
        options.event_provider, options.lcid):
      print('{0:s}:\t{1:s}'.format(message_identifier, message_string))

  else:
    message_string = database_reader.GetMessage(
        options.event_provider, options.lcid, message_identifier)

    print('Message string:')
    if message_string:
      print('0x{0:08x}:\t{1:s}'.format(message_identifier, message_string))

  database_reader.Close()

  return True


if __name__ == '__main__':
  if not Main():
    sys.exit(1)
  else:
    sys.exit(0)

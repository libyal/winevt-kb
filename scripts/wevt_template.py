#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script to parse WEVT_TEMPLATE from PE/COFF resource files."""

import argparse
import logging
import sys

import pyexe
import pyfwevt
import pywrc


def Main():
  """The main program function.

  Returns:
    bool: True if successful or False if not.
  """
  argument_parser = argparse.ArgumentParser(description=(
      'Extracts WEVT_TEMPLATE information from a PE/COFF resource file.'))

  argument_parser.add_argument(
      '-d', '--debug', dest='debug', action='store_true', default=False,
      help='enable debug output.')

  argument_parser.add_argument(
      'source', nargs='?', action='store', metavar='PATH', default=None, help=(
          'path of the PE/COFF resource file.'))

  options = argument_parser.parse_args()

  if not options.source:
    print('Source file missing.')
    print('')
    argument_parser.print_help()
    print('')
    return False

  logging.basicConfig(
      level=logging.INFO, format='[%(levelname)s] %(message)s')

  exe_file = pyexe.file()
  exe_file.open(options.source)

  exe_section = exe_file.get_section_by_name('.rsrc')
  if exe_section:
    wrc_stream = pywrc.stream()
    wrc_stream.set_virtual_address(exe_section.virtual_address)
    wrc_stream.open_file_object(exe_section)

    wrc_resource = wrc_stream.get_resource_by_name('WEVT_TEMPLATE')
    if wrc_resource:
      for wrc_resource_item in wrc_resource.items:
        for wrc_resource_sub_item in wrc_resource_item.sub_items:
          resource_data = wrc_resource_sub_item.read()

          wevt_manifest = pyfwevt.manifest()
          wevt_manifest.copy_from_byte_stream(resource_data)

          for wevt_provider in iter(wevt_manifest.providers):
            print('Event provider:')
            print(f'\tIdentifier\t\t\t: {{{wevt_provider.identifier:s}}}')
            print((f'\tLanguage identifier\t\t: '
                   f'0x{wrc_resource_sub_item.identifier:04x}'))
            print(f'\tNumber of events\t\t: {wevt_provider.number_of_events:d}')
            print('')

            for index, wevt_event in enumerate(wevt_provider.events):
              version = wevt_event.version or 0
              print(f'\tEvent {index:d}:')
              print(f'\t\tIdentifier\t\t: {wevt_event.identifier:d}')
              print(f'\t\tVersion\t\t\t: {version:d}')
              print((f'\t\tMessage identifier\t: '
                     f'0x{wevt_event.message_identifier:08x}'))
              print('')

    wrc_stream.close()

  exe_file.close()

  return True


if __name__ == '__main__':
  if not Main():
    sys.exit(1)
  else:
    sys.exit(0)

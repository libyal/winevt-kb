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
      print('\n'.join([
          '<?xml version="1.0" encoding="UTF-8"?>',
          '<instrumentationManifest',
          ('    xsi:schemaLocation="http://schemas.microsoft.com/win/2004/08/'
           'events eventman.xsd"'),
          '    xmlns="http://schemas.microsoft.com/win/2004/08/events"',
          ('    xmlns:win="http://manifests.microsoft.com/win/2004/08/windows/'
           'events"'),
          '    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
          '    xmlns:xs="http://www.w3.org/2001/XMLSchema"',
          ('    xmlns:trace="http://schemas.microsoft.com/win/2004/08/events/'
           'trace">'),
          '    <instrumentation>']))

      for wrc_resource_item in wrc_resource.items:
        for wrc_resource_sub_item in wrc_resource_item.sub_items:
          resource_data = wrc_resource_sub_item.read()

          wevt_manifest = pyfwevt.manifest()
          wevt_manifest.copy_from_byte_stream(resource_data)

          if wevt_manifest.number_of_providers > 0:
            print('        <events>')

            for wevt_provider in iter(wevt_manifest.providers):
              provider_identifier = wevt_provider.identifier.upper()

              print('\n'.join([
                  '            <provider',
                  f'                guid="{{{provider_identifier:s}}}">']))

              # TODO: implement support for other known values if possible
              # name
              # symbol
              # resourceFileName
              # messageFileName

              if wevt_provider.number_of_events > 0:
                print('                <events>')

                for wevt_event in wevt_provider.events:
                  event_version = wevt_event.version or 0

                  print('\n'.join([
                      '                    <event',
                      (f'                        value='
                       f'"{wevt_event.identifier:d}"'),
                      f'                        version="{event_version:d}"',
                      (f'                        message='
                       f'"$(string.MessageTable.'
                       f'0x{wevt_event.message_identifier:08x})">'),
                      '                    </event>']))

                # TODO: implement support for other known values if possible
                # symbol
                # channel
                # template
                # keywords
                # message

                print('                </events>')

              if wevt_provider.number_of_channels > 0:
                print('                <channels>')

                for wevt_channel in wevt_provider.channels:
                  channel_name = wevt_channel.name
                  channel_identifier = wevt_channel.identifier

                  print('\n'.join([
                      '                    <channel',
                      f'                        name="{channel_name:s}"',
                      f'                        chid="{channel_identifier:d}">',
                      '                    </channel>']))

                  # TODO: implement support for other known values if possible
                  # symbol
                  # type
                  # enabled
                  # message

                print('                </channels>')

              if wevt_provider.number_of_keywords > 0:
                print('                <keywords>')
                print('                </keywords>')

              if wevt_provider.number_of_templates > 0:
                print('                <templates>')

                for wevt_template in wevt_provider.templates:
                  template_identifier = wevt_template.identifier.upper()
                  print((f'                    <template tid='
                         f'"{{{template_identifier:s}}}">'))

                  # TODO: implement support for instance values

                  print('\n'.join([
                      '                        <data',
                      '                            name="name"',
                      '                            inType="win:UnicodeString"',
                      '                            outType="xs:string">',
                      '                        </data>']))
                  print('                    <template/>')

                print('                </templates>')

              print('            </provider>')

            print('        </events>')

      print('    </instrumentation>')

      wrc_resource = wrc_stream.get_resource_by_identifier(0x0b)
      if wrc_resource:
        print('    <localization>')

        wrc_resource_item = wrc_resource.items[0]
        for wrc_resource_sub_item in wrc_resource_item.sub_items:
          language_identifier = wrc_resource_sub_item.identifier

          # TODO: get language tag from LCID and support non en-US languages.
          if language_identifier != 0x0409:
            continue

          resource_data = wrc_resource_sub_item.read()

          message_table_resource = pywrc.message_table_resource()
          message_table_resource.copy_from_byte_stream(resource_data)

          print('\n'.join([
              '        <resources culture="en-US">',
              '            <stringTable>']))

          number_of_messages = message_table_resource.get_number_of_messages()
          for message_index in range(number_of_messages):
            message_identifier = message_table_resource.get_message_identifier(
                message_index)
            message_string = message_table_resource.get_string(
                message_index).rstrip()

            print('\n'.join([
                '                <string',
                (f'                    id='
                 f'"MessageTable.0x{message_identifier:08x}"'),
                f'                    value="{message_string:s}">',
                '                </string>']))

          print('\n'.join([
              '            </stringTable>',
              '        </resources>']))

        print('    </localization>')

      print('</instrumentationManifest>')

    wrc_stream.close()

  exe_file.close()

  return True


if __name__ == '__main__':
  if not Main():
    sys.exit(1)
  else:
    sys.exit(0)

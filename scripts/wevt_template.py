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

  input_data_types = {
      0x01: 'win:UnicodeString',
      0x02: 'win:AnsiString',
      0x03: 'win:Int8',
      0x04: 'win:UInt8',
      0x05: 'win:Int16',
      0x06: 'win:UInt16',
      0x07: 'win:Int32',
      0x08: 'win:UInt32',
      0x09: 'win:Int64',
      0x0a: 'win:UInt64',
      0x0b: 'win:Float',
      0x0c: 'win:Double',
      0x0d: 'win:Boolean',
      0x0e: 'win:Binary',
      0x0f: 'win:GUID',
      0x10: 'win:Pointer',
      0x11: 'win:FILETIME',
      0x12: 'win:SYSTEMTIME',
      0x13: 'win:SID',
      0x14: 'win:HexInt32',
      0x15: 'win:HexInt64'}

  output_data_types = {
      0x01: 'xs:string',
      0x02: 'xs:dateTime',
      0x03: 'xs:byte',
      0x04: 'xs:unsignedByte',
      0x05: 'xs:short',
      0x06: 'xs:unsignedShort',
      0x07: 'xs:int',
      0x08: 'xs:unsignedInt',
      0x09: 'xs:long',
      0x0a: 'xs:unsignedLong',
      0x0b: 'xs:float',
      0x0c: 'xs:double',
      0x0d: 'xs:boolean',
      0x0e: 'xs:GUID',
      0x0f: 'xs:hexBinary',
      0x10: 'win:HexInt8',
      0x11: 'win:HexInt16',
      0x12: 'win:HexInt32',
      0x13: 'win:HexInt64',
      0x14: 'win:PID',
      0x15: 'win:TID',
      0x16: 'win:Port',
      0x17: 'win:IPv4',
      0x18: 'win:IPv6',
      0x19: 'win:SocketAddress',
      0x1a: 'win:CIMDateTime',
      0x1b: 'win:ETWTIME',
      0x1c: 'win:Xml',
      0x1d: 'win:ErrorCode',
      0x1e: 'win:Win32Error',
      0x1f: 'win:NTSTATUS',
      0x20: 'win:HResult',
      0x21: 'win:DateTimeCultureInsensitive',
      0x22: 'win:Json',
      0x23: 'win:Utf8',
      0x24: 'win:Pkcs7WithTypeInfo'}

  exe_file = pyexe.file()
  exe_file.open(options.source)

  exe_section = exe_file.get_section_by_name('.rsrc')
  if exe_section:
    wrc_stream = pywrc.stream()
    wrc_stream.set_virtual_address(exe_section.virtual_address)
    wrc_stream.open_file_object(exe_section)

    wrc_resource = wrc_stream.get_resource_by_name('WEVT_TEMPLATE')
    if wrc_resource:
      # Note that symbols do not appear to be stored in the binary format.

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
                      f'                        version="{event_version:d}"']))

                  # TODO: implement support for other known values if possible
                  # channel
                  # keywords

                  if wevt_event.template_offset > 0:
                    wevt_template = wevt_provider.get_template_by_offset(
                        wevt_event.template_offset)
                    if wevt_template:
                      template_identifier = wevt_template.identifier.upper()
                      print((f'                        template='
                             f'"{{{template_identifier:s}}}"'))

                  print('\n'.join([
                      (f'                        message='
                       f'"$(string.MessageTable.'
                       f'0x{wevt_event.message_identifier:08x})">'),
                      '                    </event>']))

                print('                </events>')

              if wevt_provider.number_of_channels > 0:
                print('                <channels>')

                for wevt_channel in wevt_provider.channels:
                  print('\n'.join([
                      '                    <channel',
                      f'                        name="{wevt_channel.name:s}"',
                      (f'                        chid='
                       f'"{wevt_channel.identifier:d}">'),
                      '                    </channel>']))

                  # TODO: implement support for other known values if possible
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

                  # TODO: add support for template name, get from BinXML
                  # TODO: add support for UserData

                  for wevt_template_item in wevt_template.items:
                    input_type = input_data_types.get(
                        wevt_template_item.input_data_type, None)
                    output_type = output_data_types.get(
                        wevt_template_item.output_data_type, None)

                    print('\n'.join([
                        '                        <data',
                        (f'                            name='
                         f'"{wevt_template_item.name:s}"'),
                        (f'                            inType='
                         f'"{input_type:s}"')]))

                    if wevt_template_item.number_of_values > 0:
                      print((f'                            count='
                             f'"{wevt_template_item.number_of_values:d}"'))

                    if wevt_template_item.value_data_size > 0:
                      print((f'                            length='
                             f'"{wevt_template_item.value_data_size:d}"'))

                    if output_type:
                      print((f'                            outType='
                             f'"{output_type:s}">'))

                    print('                        </data>')

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

#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Script to print the message strings for all known Event Log sources.
#
# Copyright (c) 2013, Joachim Metz <joachim.metz@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import os
import sys

import pyexe
import pyregf
import sqlite3


class OSDirectory(object):
  def __init__(self, path):
    self._path = path

  def GetEntries(self):
    for entry in os.listdir(self._path):
      yield entry

  def GetEntryByNameNoCase(self, entry_name):
    entry_found = None
    entry_name_lower = entry_name.lower()

    for entry in self.GetEntries():
      if entry == entry_name:
        return entry

      if entry.lower() == entry_name_lower:
        if not entry_found:
          entry_found = entry

    return entry_found

class WindowsPathHelper(object):
  PATH_SEPARATOR = '\\'

  def GetInSystemCase(self, path, root_path=None):
    if path[ 1 ] == ':':
      if path[ 2 ] != self.PATH_SEPARATOR:
        return None

      path = path[ 3: ]

    if not root_path:
      root_path = os.getcwd()

    system_path = root_path

    for path_segment in path.split(self.PATH_SEPARATOR):
      if path_segment not in ['.', '..']:
        directory = OSDirectory(system_path)

        path_segment = directory.GetEntryByNameNoCase(path_segment)

        if not path_segment:
          return None

      system_path = os.path.join(system_path, path_segment)

    return system_path

class StdoutWriter(object):
  def Open(self):
    return True

  def Close(self):
    return True

  def Write(self, log_type, category_message_files, event_message_files):
      print '{0:s}\t{1:s}\t{2:s}'.format(
          log_type, category_message_files, event_message_files)


def GetCurrentControlSet(regf_file):
  control_set = 0

  select_key = regf_file.get_key_by_path('Select')

  if select_key:
    current_value = select_key.get_value_by_name('Current')

    control_set = current_value.data_as_integer

  return control_set

def GeteventProviders(regf_file, writer):
  control_set = GetCurrentControlSet(regf_file)

  if control_set > 0 and control_set <= 999:
    eventlog_key_path = 'ControlSet{0:03d}\\Services\\EventLog'.format(
        control_set)

    eventlog_key = regf_file.get_key_by_path(eventlog_key_path)

    if eventlog_key:
      for logtype_key in eventlog_key.sub_keys:
        log_type = logtype_key.name

        for source_key in logtype_key.sub_keys:
          category_message_file_value = source_key.get_value_by_name(
              'CategoryMessageFile')

          if category_message_file_value:
            category_message_files = category_message_file_value.data_as_string
          else:
            category_message_files = None

          event_message_file_value = source_key.get_value_by_name(
              'EventMessageFile')

          if event_message_file_value:
            event_message_files = event_message_file_value.data_as_string
          else:
            event_message_files = None

          # The messages files can contain a list of message file paths
          # separated by ;
          writer.Write(log_type, category_message_files, event_message_files)

def Main():
  args_parser = argparse.ArgumentParser(description=(
      'Extract the message strings for the known Event Log sources.'))

  args_parser.add_argument(
      'windows_volume_path', nargs='?', action='store', metavar='/mnt/c/',
      default=None, help='path of the volume containing C:\\Windows.')

  args_parser.add_argument(
      '--db', dest='database', action='store', metavar='messages.db',
      default=None, help='path of the sqlite3 database to write to.')

  args_parser.add_argument(
      '--winver', dest='windows_version', action='store', metavar='xp',
      default=None, help=('string that identifies the Windows version '
                          'in the database.'))

  options = args_parser.parse_args()

  if not options.windows_volume_path:
    print 'Windows volume path missing.'
    print ''
    args_parser.print_help()
    print ''
    return False

  writer = StdoutWriter()

  writer.Open()

  path_helper = WindowsPathHelper()

  system_path = 'C:\\Windows\\System32\\config\\SYSTEM'
  system_path = path_helper.GetInSystemCase(
      system_path, root_path=options.windows_volume_path)

  regf_file = pyregf.file()
  regf_file.open(system_path)

  GeteventProviders(regf_file, writer)

  regf_file.close()

  writer.Close()

  return True

if __name__ == '__main__':
  if not Main():
    sys.exit(1)
  else:
    sys.exit(0)

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
import logging
import os
import re
import sys

import pyexe
import pyregf
import pywrc
import sqlite3


if pyexe.get_version() < '20131017':
  raise ImportWarning('message_strings.py requires at least pyexe 20131017.')

if pyregf.get_version() < '20130716':
  raise ImportWarning('message_strings.py requires at least pyregf 20130716.')

if pywrc.get_version() < '20131017':
  raise ImportWarning('message_strings.py requires at least pywrc 20131017.')


class OSDirectory(object):
  """Directory object using operating system (OS) specific functions."""
  def __init__(self, path):
    self._path = path

  def GetEntries(self):
    """Retrieves the entries within the directory.

    Yields:
      An entry.
    """
    for entry in os.listdir(self._path):
      yield entry

  def GetEntryByNameNoCase(self, entry_name):
    """Retrieves an entry by name using a caseless comparison.

    Args:
      entry_name: a string containing the name of the entry.

    Returns:
      An entry.
    """
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
  """Helper object for Windows paths."""
  PATH_SEPARATOR = '\\'

  _PATH_EXPANSION_VARIABLE = re.compile('^[%][^%]+[%]$')

  def __init__(self, root_path=None):
    """Initializes the Windows path helper.

    Args:
      root_path: optional string that contains the root path,
                 or None by default if no root path is defined.
                 The root path should be in system specific format.
    """
    self._environment_variables = {}
    self._root_path = root_path

  def SetEnvironmentVariable(self, name, value):
    """Sets an environment variable in the Windows path helper.

    Args:
      name: the name of the environment variable without enclosing
            %-characters, e.g. SystemRoot as in %SystemRoot%.
      value: the value of the environment variable.
    """
    system_path = self.GetInSystemCase(value, expand_variables=False)
    self._environment_variables[name] = system_path[len(self._root_path):]

  def GetInSystemCase(self, path, expand_variables=True):
    """Retrieves the path in system specific format.

    Args:
      path: the Windows path to retrieve.
      expand_variables: optional value to indicate path variables should be
                        expanded or not. The default is to expand (True).

    Returns:
      The path in system specific format.
    """
    if path[1] == ':':
      if path[2] != self.PATH_SEPARATOR:
        return None

      path = path[3:]

    if self._root_path:
      system_path = self._root_path
    else:
      system_path = os.getcwd()

    for path_segment in path.split(self.PATH_SEPARATOR):
      if path_segment not in ['.', '..']:
        if (expand_variables and
            self._PATH_EXPANSION_VARIABLE.match(path_segment)):
          path_segment = self._environment_variables.get(
              path_segment[1:-1], path_segment)

        directory = OSDirectory(system_path)
        path_segment = directory.GetEntryByNameNoCase(path_segment)

        if not path_segment:
          return None

      system_path = os.path.join(system_path, path_segment)

    return system_path


class EventLogProvider(object):
  """Object to represent a Windows Event Log provider."""

  def __init__(self, log_type, log_source, category_message_filenames,
               event_message_filenames):
    """Initializes the Windows Event Log provider.

    Args:
      log_type: the Event Log type.
      log_source: the Event Log source.
      category_message_filenames: the message filenames that contain
                                  the category strings.
      event_message_filenames: the message filenames that contain
                               the event messages.
    """
    self.log_type = log_type
    self.log_source = log_source

    # It not empty the messages filenames can contain a list
    # of message file paths separated by ;
    if category_message_filenames:
      self.category_message_files = category_message_filenames.split(';')
    else:
      self.category_message_files = category_message_filenames

    if event_message_filenames:
      self.event_message_files = event_message_filenames.split(';')
    else:
      self.event_message_files = event_message_filenames


class RegistryFile(object):
  """Object to represent a Windows Registry file."""

  def __init__(self):
    """Initializes the Windows Registry file."""
    self._regf_file = pyregf.file()

  def Open(self, filename):
    """Opens the Windows Registry file.

    Args:
      filename: the name of the Windows Registry file.

    Returns:
      A boolean containing True if successful or False if not.
    """
    # TODO: allow to set ASCII codepage.
    self._regf_file.open(filename)
    return True

  def Close(self):
    """Closes the Windows Registry file."""
    self._regf_file.close()

  def GetSystemRoot(self):
    """Retrieves the value of %SystemRoot%.

    Returns:
      A string containing value of %SystemRoot%
      or None if the value could not be retrieved.
    """
    system_root = None

    current_version_key = self._regf_file.get_key_by_path(
        'Microsoft\\Windows NT\\CurrentVersion')

    if current_version_key:
      system_root_value = current_version_key.get_value_by_name('SystemRoot')
      if system_root_value:
        system_root = system_root_value.data_as_string

    return system_root

  def GetCurrentControlSet(self):
    """Retrieves the current control set.

    Returns:
      An integer containing the number of the current control set
      or 0 if no current control set could be retrieved.
    """
    control_set = 0
  
    select_key = self._regf_file.get_key_by_path('Select')
  
    if select_key:
      current_value = select_key.get_value_by_name('Current')
      if current_value: 
        control_set = current_value.data_as_integer
  
    return control_set

  def GetEventLogProviders(self):
    """Retrieves the event log providers.

    Yields:
      An event log provider object (EventLogProvider).
    """
    control_set = self.GetCurrentControlSet()
  
    if control_set > 0 and control_set <= 999:
      eventlog_key_path = 'ControlSet{0:03d}\\Services\\EventLog'.format(
          control_set)
  
      eventlog_key = self._regf_file.get_key_by_path(eventlog_key_path)
  
      if eventlog_key:
        for log_type_key in eventlog_key.sub_keys:
          log_type = log_type_key.name
  
          for log_source_key in log_type_key.sub_keys:
            log_source = log_source_key.name

            category_message_file_value = log_source_key.get_value_by_name(
                'CategoryMessageFile')
  
            if category_message_file_value:
              category_message_files = category_message_file_value.data_as_string
            else:
              category_message_files = None
  
            event_message_file_value = log_source_key.get_value_by_name(
                'EventMessageFile')
  
            if event_message_file_value:
              event_message_files = event_message_file_value.data_as_string
            else:
              event_message_files = None

            yield EventLogProvider(
                log_type, log_source, category_message_files,
                event_message_files)


class MessageResourceFile(object):
  """Object to represent a Windows Message Resource file."""

  _MESSAGE_TABLE_RESOURCE_IDENTIFIER = 0x0b

  def __init__(self):
    """Initializes the Windows Message Resource file."""
    self._exe_file = pyexe.file()
    self._wrc_stream = pywrc.stream()

  def Open(self, filename):
    """Opens the Windows Message Resource file.

    Args:
      filename: the name of the Windows Message Resource file.

    Returns:
      A boolean containing True if successful or False if not.
    """
    # TODO: allow to set ASCII codepage.
    self._exe_file.open(filename)
    exe_section = self._exe_file.get_section_by_name('.rsrc')

    if not exe_section:
      self._exe_file.close()
      return False

    self._wrc_stream.set_virtual_address(exe_section.virtual_address)
    self._wrc_stream.open_file_object(exe_section)

    return True

  def Close(self):
    """Closes the Windows Message Resource file."""
    self._wrc_stream.close()
    self._exe_file.close()


class StdoutWriter(object):
  """Output writer object to write to stdout."""

  def Open(self):
    """Opens the output writer object.

    Returns:
      A boolean containing True if successful or False if not.
    """
    return True

  def Close(self):
    """Closes the output writer object."""
    pass

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider to the output.

    Args:
      event_log_provider: the Event Log provider.
    """
    print '{0:s}\t{1:s}\t{2:s}\t{3:s}'.format(
        event_log_provider.log_type,
        event_log_provider.log_source,
        event_log_provider.category_message_files,
        event_log_provider.event_message_files)


def Main():
  """The main program function.

  Returns:
    A boolean containing True if successful or False if not.
  """
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

  logging.basicConfig(
      level=logging.INFO, format='[%(levelname)s] %(message)s')

  writer = StdoutWriter()

  writer.Open()

  path_helper = WindowsPathHelper(options.windows_volume_path)

  # Determine the value of %SystemRoot%.
  registry_filename = 'C:\\Windows\\System32\\config\\SOFTWARE'
  registry_filename = path_helper.GetInSystemCase(registry_filename)

  registry_file = RegistryFile()
  registry_file.Open(registry_filename)

  system_root = registry_file.GetSystemRoot()

  registry_file.Close()

  path_helper.SetEnvironmentVariable('SystemRoot', system_root)

  # Determine the Event Log providers.
  registry_filename = 'C:\\Windows\\System32\\config\\SYSTEM'
  registry_filename = path_helper.GetInSystemCase(registry_filename)

  registry_file = RegistryFile()
  registry_file.Open(registry_filename)

  event_log_types = {}

  for event_log_provider in registry_file.GetEventLogProviders():
    if event_log_provider.log_type not in event_log_types:
      event_log_types[event_log_provider.log_type] = {}

    event_log_sources = event_log_types[event_log_provider.log_type]
    if event_log_provider.log_source in event_log_sources:
      logging.warning(('Found duplicate Event Log source: '
                       '{0:s} in type: {1:s}').format(
          event_log_provider.log_source, event_log_provider.log_type))

    event_log_sources[event_log_provider.log_source] = event_log_provider

    if event_log_provider.event_message_files:
      for message_filename in event_log_provider.event_message_files:
        message_filename = path_helper.GetInSystemCase(message_filename)

    writer.WriteEventLogProvider(event_log_provider)

  registry_file.Close()

  writer.Close()

  return True


if __name__ == '__main__':
  if not Main():
    sys.exit(1)
  else:
    sys.exit(0)

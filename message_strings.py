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
import stat
import sys

import dfvfs
import pyexe
import pyregf
import pywrc
import sqlite3

from dfvfs.analyzer import analyzer
from dfvfs.lib import definitions
from dfvfs.path import factory as path_spec_factory
from dfvfs.helpers import windows_path_resolver
from dfvfs.resolver import resolver
from dfvfs.vfs import os_file_system
from dfvfs.volume import tsk_volume_system


if dfvfs.__version__ < '20140127':
  raise ImportWarning('message_strings.py requires dfvfs 20140127 or later.')

if pyexe.get_version() < '20131229':
  raise ImportWarning('message_strings.py requires pyexe 20131229 or later.')

if pyregf.get_version() < '20130716':
  raise ImportWarning('message_strings.py requires pyregf 20130716 or later.')

if pywrc.get_version() < '20140128':
  raise ImportWarning('message_strings.py requires pywrc 20140128 or later.')


class CollectorError(Exception):
  """Class that defines collector errors."""


class WindowsVolumeCollector(object):
  """Class that defines a Windows volume collector."""

  _WINDOWS_DIRECTORIES = frozenset([
      u'C:\\Windows',
      u'C:\\WINNT',
      u'C:\\WTSRV',
      u'C:\\WINNT35',
  ])

  def __init__(self):
    """Initializes the Windows volume collector object."""
    super(WindowsVolumeCollector, self).__init__()
    self._file_system = None
    self._path_resolver = None

  def GetWindowsVolumePathSpec(self, source_path):
    """Determines the file system path specification of the Windows volume.

    Args:
      source_path: the source path.

    Returns:
      True if successful or False otherwise.

    Raises:
      CollectorError: if the source path does not exists, or if the source path
                      is not a file or directory, or if the format of or within
                      the source file is not supported.
    """
    if not os.path.exists(source_path):
      raise CollectorError(u'No such source: {0:s}.'.format(source_path))

    stat_info = os.stat(source_path)

    if (not stat.S_ISDIR(stat_info.st_mode) and
        not stat.S_ISREG(stat_info.st_mode)):
      raise CollectorError(
          u'Unsupported source: {0:s} not a file or directory.'.format(
              source_path))

    path_spec = path_spec_factory.Factory.NewPathSpec(
        definitions.TYPE_INDICATOR_OS, location=source_path)

    if stat.S_ISREG(stat_info.st_mode):
      type_indicators = analyzer.Analyzer.GetStorageMediaImageTypeIndicators(
          path_spec)

      if len(type_indicators) > 1:
        raise CollectorError((
            u'Unsupported source: {0:s} found more than one storage media '
            u'image types.').format(source_path))

      if len(type_indicators) == 1:
        path_spec = path_spec_factory.Factory.NewPathSpec(
            type_indicators[0], parent=path_spec)

      type_indicators = analyzer.Analyzer.GetVolumeSystemTypeIndicators(
          path_spec)

      if len(type_indicators) > 1:
        raise CollectorError((
            u'Unsupported source: {0:s} found more than one volume system '
            u'types.').format(source_path))

      if len(type_indicators) == 1:
        if type_indicators[0] == definitions.TYPE_INDICATOR_TSK_PARTITION:
          vs_path_spec = path_spec_factory.Factory.NewPathSpec(
              type_indicators[0], location='/', parent=path_spec)

          volume_system = tsk_volume_system.TSKVolumeSystem()
          volume_system.Open(vs_path_spec)

          result = False

          for volume in volume_system.volumes:
            if not hasattr(volume, 'identifier'):
              continue

            volume_location = u'/{0:s}'.format(volume.identifier)
            volume_path_spec = path_spec_factory.Factory.NewPathSpec(
                type_indicators[0], location=volume_location, parent=path_spec)

            fs_path_spec = path_spec_factory.Factory.NewPathSpec(
                definitions.TYPE_INDICATOR_TSK, location=u'/',
                parent=volume_path_spec)
            file_system = resolver.Resolver.OpenFileSystem(fs_path_spec)

            if file_system is None:
              continue

            path_resolver = windows_path_resolver.WindowsPathResolver(
                file_system, volume_path_spec)

            for windows_path in self._WINDOWS_DIRECTORIES:
              windows_path_spec = path_resolver.ResolvePath(windows_path)

              result = windows_path_spec is not None

              if result:
                path_spec = volume_path_spec
                break

            if result:
              break

          if not result:
            return False

        elif type_indicators[0] != definitions.TYPE_INDICATOR_VSHADOW:
          raise CollectorError((
              u'Unsupported source: {0:s} found unsupported volume system '
              u'type: {1:s}.').format(source_path, type_indicators[0]))

      type_indicators = analyzer.Analyzer.GetFileSystemTypeIndicators(
          path_spec)

      if len(type_indicators) == 0:
        return False

      if len(type_indicators) > 1:
        raise CollectorError((
            u'Unsupported source: {0:s} found more than one file system '
            u'types.').format(source_path))

      if type_indicators[0] != definitions.TYPE_INDICATOR_TSK:
        raise CollectorError((
            u'Unsupported source: {0:s} found unsupported file system '
            u'type: {1:s}.').format(source_path, type_indicators[0]))

      fs_path_spec = path_spec_factory.Factory.NewPathSpec(
          definitions.TYPE_INDICATOR_TSK, location=u'/',
          parent=path_spec)
      self._file_system = resolver.Resolver.OpenFileSystem(fs_path_spec)

    elif stat.S_ISDIR(stat_info.st_mode):
      self._file_system = os_file_system.OSFileSystem()

    self._path_resolver = windows_path_resolver.WindowsPathResolver(
        self._file_system, path_spec)

    return True

  def OpenFile(self, windows_path):
    """Opens the file specificed by the Windows path.

    Args:
      windows_path: the Windows path to the file.

    Returns:
      The file-like object (instance of dfvfs.FileIO) or None if
      the file does not exist.
    """
    path_spec = self._path_resolver.ResolvePath(windows_path)
    if path_spec is None:
      return None

    return resolver.Resolver.OpenFileObject(path_spec)


class EventLogProvider(object):
  """Class that defines a Windows Event Log provider."""

  def __init__(
      self, log_type, log_source, category_message_filenames,
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
    super(EventLogProvider, self).__init__()
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


class EventMessageStringCollector(WindowsVolumeCollector):
  """Class that defines an event message string collector."""

  _REGISTRY_FILENAME_SOFTWARE = u'C:\\Windows\\System32\\config\\SOFTWARE'
  _REGISTRY_FILENAME_SYSTEM = u'C:\\Windows\\System32\\config\\SYSTEM'

  def __init__(self):
    """Initializes the event message string collector object."""
    super(EventMessageStringCollector, self).__init__()
    self.ascii_codepage='cp1252'
    self.invalid_message_filenames = None
    self.missing_table_message_filenames = None
    self.preferred_language_identifier = 0x0409
    self.system_root = None

  def _CollectEventLogTypes(self):
    """Collects the Event Log types form the SYSTEM Registry file.

    Returns:
      A dictionary containing a dictionary of Event Log providers per event
      log type. E.g. { 'Application': { 'EventSystem': instance of 
                                        EventLogProvider, ... }, ... }
    """
    event_log_types = {}
    registry_file = self._OpenRegistryFile(self._REGISTRY_FILENAME_SYSTEM)

    for event_log_provider in registry_file.GetEventLogProviders():
      if event_log_provider.log_type not in event_log_types:
        event_log_types[event_log_provider.log_type] = {}

      event_log_sources = event_log_types[event_log_provider.log_type]
      if event_log_provider.log_source in event_log_sources:
        logging.warning((
            u'Found duplicate Event Log source: {0:s} in type: {1:s}.').format(
                event_log_provider.log_source, event_log_provider.log_type))

      event_log_sources[event_log_provider.log_source] = event_log_provider

    registry_file.Close()

    return event_log_types

  def _OpenMessageResourceFile(self, windows_path):
    """Opens the message resource file specificed by the Windows path.

    Args:
      windows_path: the Windows path containing the messagge resource filename.

    Returns:
      The message resource file (instance of MessageResourceFile) or None.
    """
    file_object = self.OpenFile(windows_path)
    if file_object is None:
      return None

    message_file = MessageResourceFile(
        ascii_codepage=self.ascii_codepage,
        preferred_language_identifier=self.preferred_language_identifier)
    if not message_file.Open(file_object):
      return None

    return message_file

  def _OpenRegistryFile(self, windows_path):
    """Opens the registry file specificed by the Windows path.

    Args:
      windows_path: the Windows path containing the Registry filename.

    Returns:
      The Registry file (instance of RegistryFile) or None.
    """
    file_object = self.OpenFile(windows_path)
    if file_object is None:
      return None

    registry_file = RegistryFile()
    registry_file.Open(file_object)
    return registry_file

  def CollectEventLogMessageStrings(self, output_writer):
    """Collects the Event Log message strings from the message files."""
    self.invalid_message_filenames = []
    self.missing_table_message_filenames = []
    processed_message_filenames = []
    event_log_types = self._CollectEventLogTypes()

    for event_log_type, event_log_sources in event_log_types.iteritems():
      output_writer.WriteEventLogType(event_log_type)

      for event_log_source, event_log_provider in event_log_sources.iteritems():
        output_writer.WriteEventLogProvider(event_log_provider)

        if event_log_provider.event_message_files:
          for message_filename in event_log_provider.event_message_files:

            if message_filename not in processed_message_filenames:
              message_file = self._OpenMessageResourceFile(message_filename)

              if not message_file:
                self.invalid_message_filenames.append(message_filename)
                continue

              message_file_version = message_file.GetVersion()
              if message_file_version:
                print u'Message file version: {0:s}'.format(message_file_version)

              message_table = message_file.GetMessageTableResource()
              if not message_table:
                # Windows Vista and later use a MUI resource to redirect to
                # a language specific message file.
                mui_language = message_file.GetMuiLanguage()

                if mui_language:
                  message_filename_path, _, message_filename_name = (
                      message_filename.rpartition(u'\\'))

                  mui_message_file_path = u'{0:s}\\{1:s}\\{2:s}.mui'.format(
                      message_filename_path, mui_language, message_filename_name)

                  mui_message_file = self._OpenMessageResourceFile(
                      mui_message_file_path)

                  if not mui_message_file:
                    mui_message_file_path = u'{0:s}\\{1:s}.mui'.format(
                      message_filename_path, message_filename_name)

                    mui_message_file = self._OpenMessageResourceFile(
                        mui_message_file_path)

                  if mui_message_file:
                    print u'MUI message file: {0:s}'.format(mui_message_file_path)
                    message_file.Close()
                    message_file = mui_message_file

                    message_table = message_file.GetMessageTableResource()

              if not message_table:
                self.missing_table_message_filenames.append(message_filename)
              else:
                output_writer.WriteMessageTable(message_table)

              message_file.Close()

              processed_message_filenames.append(message_filename)

  def GetSystemRootFromRegistry(self):
    """Determines the value of %SystemRoot% from the SOFTWARE Registry file.

       The Windows path resolver is updated to expand this environment variable.

    Returns:
      True if successful or False otherwise.
    """
    # TODO: use the determined Windows directory to find the Registry file.
    registry_file = self._OpenRegistryFile(self._REGISTRY_FILENAME_SOFTWARE)
    system_root = registry_file.GetSystemRoot()
    registry_file.Close()

    if system_root:
      self.system_root = system_root
    else:
      # TODO: use the determined Windows directory instead of harding coding
      # the fallback.
      self.system_root = u'C:\\Windows\\System32'

    self._path_resolver.SetEnvironmentVariable('SystemRoot', self.system_root)

    return self.system_root is not None


class MessageResourceFile(object):
  """Class that defines a Windows Message Resource file."""

  _RESOURCE_IDENTIFIER_MESSAGE_TABLE = 0x0b
  _RESOURCE_IDENTIFIER_VERSION = 0x10

  def __init__(
      self, ascii_codepage='cp1252', preferred_language_identifier=0x0409):
    """Initializes the Windows Message Resource file.

    Args:
      ascii_codepage: optional ASCII string codepage. The default is cp1252
                      (or windows-1252).
      preferred_language_identifier: optional preferred language identifier
                                     (LCID). The default is 0x0409 (en-US).
    """
    super(MessageResourceFile, self).__init__()
    self._ascii_codepage = ascii_codepage
    self._exe_file = pyexe.file()
    self._exe_file.set_ascii_codepage(self._ascii_codepage)
    self._is_open = False
    self._preferred_language_identifier = preferred_language_identifier
    self._wrc_stream = pywrc.stream()
    # TODO: wrc stream set codepage?

  def GetMessageTableResource(self):
    """Retrieves the message table resource."""
    return self._wrc_stream.get_resource_by_identifier(
        self._RESOURCE_IDENTIFIER_MESSAGE_TABLE)

  def GetMuiLanguage(self):
    """Retrieves the MUI language or None if not available."""
    mui_resource = self._wrc_stream.get_resource_by_name('MUI')
    if not mui_resource:
      return

    mui_language = None
    language_identifier = self._preferred_language_identifier
    if language_identifier in mui_resource.language_identifiers:
      mui_language = mui_resource.get_language(language_identifier)

    if not mui_language:
      for language_identifier in mui_resource.language_identifiers:
        mui_language = mui_resource.get_language(language_identifier)
        if mui_language:
          break

    return mui_language

  def GetVersion(self):
    """Retrieves the file (or product) version.

    Returns:
      A string containing the file (or product) version or None
      if not available.
    """
    version_resource = self._wrc_stream.get_resource_by_identifier(
        self._RESOURCE_IDENTIFIER_VERSION)
    if not version_resource:
      return

    file_version = None
    language_identifier = self._preferred_language_identifier
    if language_identifier in version_resource.language_identifiers:
      file_version = version_resource.get_file_version(language_identifier)
      product_version = version_resource.get_product_version(
          language_identifier)

    if not file_version:
      for language_identifier in version_resource.language_identifiers:
        file_version = version_resource.get_file_version(language_identifier)
        product_version = version_resource.get_product_version(
            language_identifier)

        if file_version:
          break

    file_version_string = u'{0:d}.{1:d}.{2:d}.{3:d}'.format(
        (file_version >> 48) & 0xffff, (file_version >> 32) & 0xffff,
        (file_version >> 16) & 0xffff, file_version & 0xffff)

    if file_version != product_version:
      product_version_string = u'{0:d}.{1:d}.{2:d}.{3:d}'.format(
          (product_version >> 48) & 0xffff, (product_version >> 32) & 0xffff,
          (product_version >> 16) & 0xffff, product_version & 0xffff)

      logging.warning((
          u'Mismatch in file version: {0:s} and product version: '
          u'{1:s}.').format(file_version_string, product_version_string))

    return file_version_string

  def Open(self, file_object):
    """Opens the Windows Message Resource file using a file-like object.

    Args:
      file_object: the file-like object.

    Returns:
      A boolean containing True if successful or False if not.

    Raises:
      IOError: if already open.
    """
    if self._is_open:
      raise IOError(u'Already open.')

    self._file_object = file_object
    self._exe_file.open_file_object(self._file_object)
    exe_section = self._exe_file.get_section_by_name('.rsrc')

    if not exe_section:
      self._exe_file.close()
      return False

    self._wrc_stream.set_virtual_address(exe_section.virtual_address)
    self._wrc_stream.open_file_object(exe_section)

    return True

  def Close(self):
    """Closes the Windows Message Resource file.

    Raises:
      IOError: if not open.
    """
    if self._is_open:
      raise IOError(u'Not opened.')

    self._wrc_stream.close()
    self._exe_file.close()
    self._file_object.close()
    self._file_object = None


class RegistryFile(object):
  """Class that defines a Windows Registry file."""

  def __init__(self, ascii_codepage='cp1252'):
    """Initializes the Windows Registry file.

    Args:
      ascii_codepage: optional ASCII string codepage. The default is cp1252
                      (or windows-1252).
    """
    super(RegistryFile, self).__init__()
    self._file_object = None
    self._regf_file = pyregf.file()
    self._regf_file.set_ascii_codepage(ascii_codepage)

  def Open(self, file_object):
    """Opens the Windows Registry file using a file-like object.

    Args:
      file_object: the file-like object.

    Returns:
      A boolean containing True if successful or False if not.
    """
    self._file_object = file_object
    self._regf_file.open_file_object(self._file_object)
    return True

  def Close(self):
    """Closes the Windows Registry file."""
    self._regf_file.close()
    self._file_object.close()
    self._file_object = None

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
    """Retrieves the Event Log providers.

    Yields:
      An Event Log provider object (EventLogProvider).
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
              category_message_files = (
                  category_message_file_value.data_as_string)
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


class Sqlite3Writer(object):
  """Class that defines a sqlite3 output writer."""

  _EVENT_SOURCES_CREATE_QUERY = (
      'CREATE TABLE event_sources ( name TEXT, windows_version TEXT, '
      'categories TEXT, messages TEXT )')

  _EVENT_SOURCES_INSERT_QUERY = (
      'INSERT INTO event_sources VALUES ( "{0:s}", "{1:s}", "{2:s}", "{3:s}" )')

  _EVENT_SOURCES_SELECT_QUERY = (
      'SELECT name FROM event_sources WHERE name = "{0:s}" AND '
      'windows_version = "{1:s}"')

  # TODO: create table of the resource files, have an id per resource file.
  # Use the in the resource table names e.g. message_table_00000001.

  _MESSAGE_TABLE_CREATE_QUERY = (
      'CREATE TABLE message_table_{0:s} ( message_identifier TEXT, '
      'windows_version TEXT, string TEXT )')

  _MESSAGE_TABLE_INSERT_QUERY = (
      'INSERT INTO message_table_{0:s} VALUES ( "{1:s}", "{2:s}", "{3:s}" )')

  _MESSAGE_TABLE_SELECT_QUERY = (
      'SELECT message_identifier, string FROM message_table_{0:s} '
      'WHERE message_identifier = "{1:s}" AND windows_version = "{2:s}"')

  def __init__(self, database_file, windows_version):
    """Initializes the output writer object.

    Args:
      database_file: the name of the database file.
      windows_version: the Windows version.
    """
    super(Sqlite3Writer, self).__init__()
    self._database_file = database_file
    self._windows_version = windows_version

  def Open(self):
    """Opens the output writer object.

    Returns:
      A boolean containing True if successful or False if not.
    """
    if os.path.exists(self._database_file):
      self._create_new_database = False
    else:
      self._create_new_database = True

    self._connection = sqlite3.connect(self._database_file)
    if not self._connection:
      return False

    self._cursor = self._connection.cursor()
    if not self._cursor:
      return False

    if self._create_new_database:
      self._cursor.execute(self._EVENT_SOURCES_CREATE_QUERY)

    return True

  def Close(self):
    """Closes the output writer object."""
    self._connection.close()

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider to stdout.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
    """
    # TODO: write message files in a separate table and use the key
    # instead of writing the list.
    if not self._create_new_database:
      sql_query = self._EVENT_SOURCES_SELECT_QUERY.format(
          event_log_provider.log_source, self._windows_version)

      self._cursor.execute(sql_query)

      if self._cursor.fetchone():
        have_entry = True
      else:
        have_entry = False
    else:
      have_entry = False

    if not have_entry:
      sql_query = self._EVENT_SOURCES_INSERT_QUERY.format(
          event_log_provider.log_source, self._windows_version,
          event_log_provider.category_message_files,
          event_log_provider.event_message_files)

      self._cursor.execute(sql_query)
      self._connection.commit()
    else:
      logging.info(u'Ignoring duplicate: {0:s}'.format(
          event_log_provider.log_source))

  def WriteEventLogType(self, event_log_type):
    """Writes the Event Log provider to stdout

    Args:
      event_log_type: string containing the Event Log type.
    """
    # TODO: implement.
    pass

  def WriteMessageTable(self, message_table):
    """Writes the Windows Message Resource file message table to stdout.

    Args:
      message_table: the message table (instance of pywrc.message_table).
    """
    # TODO: implement.
    pass


class StdoutWriter(object):
  """Class that defines a stdout output writer."""

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
    """Writes the Event Log provider to stdout.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
    """
    print u'Source\t\t: {0:s}'.format(
        event_log_provider.log_source)

    print u'Categories\t: {0:s}'.format(
        event_log_provider.category_message_files)

    print u'Messages\t: {0:s}'.format(
        event_log_provider.event_message_files)

    print ''

  def WriteEventLogType(self, event_log_type):
    """Writes the Event Log provider to stdout

    Args:
      event_log_type: string containing the Event Log type.
    """
    print u'Event Log type: {0:s}'.format(event_log_type)

  def WriteMessageTable(self, message_table):
    """Writes the Windows Message Resource file message table to stdout.

    Args:
      message_table: the message table (instance of pywrc.message_table).
    """
    if message_table.number_of_languages > 0:
      for language_identifier in message_table.language_identifiers:
        number_of_messages = message_table.get_number_of_messages(
            language_identifier)

        for message_index in range(0, number_of_messages):
          message_identifier = message_table.get_message_identifier(
              language_identifier, message_index)
          message_string = message_table.get_string(
              language_identifier, message_index)

          ouput_string = u'0x{0:08x}\t: {1:s}'.format(
              message_identifier, message_string)

          print ouput_string.encode('utf8')

      print ''


def Main():
  """The main program function.

  Returns:
    A boolean containing True if successful or False if not.
  """
  args_parser = argparse.ArgumentParser(description=(
      'Extract the message strings for the known Event Log sources.'))

  args_parser.add_argument(
      'source', nargs='?', action='store', metavar='/mnt/c/',
      default=None, help=('path of the volume containing C:\\Windows or the '
                          'filename of a storage media image containing the '
                          'C:\\Windows directory.'))

  args_parser.add_argument(
      '--db', dest='database', action='store', metavar='messages.db',
      default=None, help='path of the sqlite3 database to write to.')

  args_parser.add_argument(
      '--winver', dest='windows_version', action='store', metavar='xp',
      default=None, help=('string that identifies the Windows version '
                          'in the database.'))

  options = args_parser.parse_args()

  if not options.source:
    print u'Source value is missing.'
    print u''
    args_parser.print_help()
    print u''
    return False

  if options.database and not options.windows_version:
    print 'Windows version missing.'
    print ''
    args_parser.print_help()
    print ''
    return False

  logging.basicConfig(
      level=logging.INFO, format=u'[%(levelname)s] %(message)s')

  if not options.database:
    output_writer = StdoutWriter()
  else:
    output_writer = Sqlite3Writer(options.database, options.windows_version)

  if not output_writer.Open():
    print 'Unable to open output writer.'
    print ''
    return False

  collector = EventMessageStringCollector()

  if not collector.GetWindowsVolumePathSpec(options.source):
    print (
        u'Unable to retrieve the volume with the Windows directory from: '
        u'{0:s}.').format(options.source)
    print ''
    return False

  # Determine the value of %SystemRoot%.
  if not collector.GetSystemRootFromRegistry():
    print u'Unable to retrieve %SystemRoot%.'
    print u''
    return False

  collector.CollectEventLogMessageStrings(output_writer)
  output_writer.Close()

  if collector.invalid_message_filenames:
    print u'Message resource files not found or without resource section:'
    for message_filename in collector.invalid_message_filenames:
      print u'{0:s}'.format(message_filename)
    print u''

  if collector.missing_table_message_filenames:
    print u'Message resource files without a message table resource:'
    for message_filename in collector.missing_table_message_filenames:
      print u'{0:s}'.format(message_filename)
    print u''

  return True


if __name__ == '__main__':
  if not Main():
    sys.exit(1)
  else:
    sys.exit(0)

#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Script to print the message strings for all known Event Log sources.
#
# Copyright (c) 2013-2014, Joachim Metz <joachim.metz@gmail.com>
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

import abc
import argparse
import logging
import os
import re
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


if dfvfs.__version__ < '20140413':
  raise ImportWarning('message_strings.py requires dfvfs 20140413 or later.')

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
    self._windows_path = None

  def _ScanForWindowsDirectory(self, file_system, mount_point):
    """Scans a path specification for the Windows directory.

    Args:
      file_system: the file system object (instance of vfs.FileSystem).
      mount_point: the mount point path specification (instance of
                   dfvfs.PathSpec). The default is None.

    Returns:
      True if a Windows directory was found, False otherwise.
    """
    path_resolver = windows_path_resolver.WindowsPathResolver(
        file_system, mount_point)

    for windows_path in self._WINDOWS_DIRECTORIES:
      windows_path_spec = path_resolver.ResolvePath(windows_path)

      result = windows_path_spec is not None

      if result:
        self._windows_path = windows_path
        return True

    return False

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

    source_path_spec = path_spec_factory.Factory.NewPathSpec(
        definitions.TYPE_INDICATOR_OS, location=source_path)

    path_spec = source_path_spec

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

            result = self._ScanForWindowsDirectory(file_system, volume_path_spec)
            if result:
              path_spec = volume_path_spec
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
      self._file_system = resolver.Resolver.OpenFileSystem(source_path_spec)

      result = self._ScanForWindowsDirectory(
          self._file_system, source_path_spec)
      if not result:
        return False

      path_spec = source_path_spec

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

  def __init__(self):
    """Initializes the event message string collector object."""
    super(EventMessageStringCollector, self).__init__()
    self._system_root = None
    self._windows_version = None
    self.ascii_codepage='cp1252'
    self.invalid_message_filenames = None
    self.missing_table_message_filenames = None
    self.preferred_language_identifier = 0x0409

  def _CollectEventLogTypes(self):
    """Collects the Event Log types form the SYSTEM Registry file.

    Returns:
      A dictionary containing a dictionary of Event Log providers per event
      log type. E.g. { 'Application': { 'EventSystem': instance of 
                                        EventLogProvider, ... }, ... }
    """
    registry_filename = u'\\'.join([
        self._windows_path, u'System32', u'config', u'SYSTEM'])

    registry_file = self._OpenRegistryFile(registry_filename)
    event_log_types = {}

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

  def _GetSystemRoot(self):
    """Retrieves the value of %SystemRoot%.

    Returns:
      A string containing the system root.
    """
    if not self._system_root:
      self._system_root = self._GetSystemRootFromRegistry()

    if self._system_root:
      self._path_resolver.SetEnvironmentVariable(
          'SystemRoot', self._system_root)

    return self._system_root

  def _GetSystemRootFromRegistry(self):
    """Determines the value of %SystemRoot% from the SOFTWARE Registry file.

       The Windows path resolver is updated to expand this environment variable.

    Returns:
      A string containing the System Root or None otherwise.
    """
    registry_filename = u'\\'.join([
        self._windows_path, u'System32', u'config', u'SOFTWARE'])

    registry_file = self._OpenRegistryFile(registry_filename)
    system_root = registry_file.GetSystemRoot()
    registry_file.Close()

    if system_root:
      system_root = system_root
    else:
      system_root = self._windows_path

    return system_root

  def _GetWindowsVersion(self):
    """Determines the Windows version from kernel executable file.

    Returns:
      A string containing the Windows version or None otherwise.
    """
    system_root = self._GetSystemRoot()

    # Window NT variants.
    kernel_executable_path = u'\\'.join([
          system_root, u'System32', u'ntoskrnl.exe'])
    message_file = self._OpenMessageResourceFile(kernel_executable_path)

    if not message_file:
      # Window 9x variants.
      kernel_executable_path = u'\\'.join([
          system_root, u'System32', u'\kernel32.dll'])
      message_file = self._OpenMessageResourceFile(kernel_executable_path)

    if not message_file:
      return None

    return message_file.file_version

  def _OpenMessageResourceFile(self, windows_path):
    """Opens the message resource file specificed by the Windows path.

    Args:
      windows_path: the Windows path containing the messagge resource filename.

    Returns:
      The message resource file (instance of MessageResourceFile) or None.
    """
    path_spec = self._path_resolver.ResolvePath(windows_path)
    if path_spec is None:
      return None

    windows_path = self._path_resolver.GetWindowsPath(path_spec)
    if windows_path is None:
      logging.warning(u'Unable to retrieve Windows path.')

    file_object = resolver.Resolver.OpenFileObject(path_spec)
    if file_object is None:
      return None

    message_file = MessageResourceFile(
        windows_path, ascii_codepage=self.ascii_codepage,
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

  @property
  def windows_version(self):
    """The Windows version."""
    if self._windows_version is None:
      self._windows_version = self._GetWindowsVersion()
    return self._windows_version

  @windows_version.setter
  def windows_version(self, value):
    """The Windows version."""
    self._windows_version = value

  def CollectEventLogMessageStrings(self, output_writer):
    """Collects the Event Log message strings from the message files.

    Args:
      output_writer: the output writer (instance of OutputWriter).
    """
    self.invalid_message_filenames = []
    self.missing_table_message_filenames = []
    processed_message_filenames = []
    event_log_types = self._CollectEventLogTypes()

    for event_log_type, event_log_sources in event_log_types.iteritems():
      for event_log_source, event_log_provider in event_log_sources.iteritems():
        output_writer.WriteEventLogProvider(event_log_provider)

        if event_log_provider.event_message_files:
          for message_filename in event_log_provider.event_message_files:
            if message_filename in processed_message_filenames:
              continue

            message_file = self._OpenMessageResourceFile(message_filename)
            mui_message_filename = None

            if not message_file:
              if message_filename in self.invalid_message_filenames:
                self.invalid_message_filenames.append(message_filename)
              continue

            if message_file.windows_path in processed_message_filenames:
              message_file.Close()
              continue

            message_table = message_file.GetMessageTableResource()
            if not message_table:
              # Windows Vista and later use a MUI resource to redirect to
              # a language specific message file.
              mui_language = message_file.GetMuiLanguage()

              if mui_language:
                message_filename_path, _, message_filename_name = (
                    message_filename.rpartition(u'\\'))

                mui_message_filename = u'{0:s}\\{1:s}\\{2:s}.mui'.format(
                    message_filename_path, mui_language, message_filename_name)

                mui_message_file = self._OpenMessageResourceFile(
                    mui_message_filename)

                if not mui_message_file:
                  mui_message_filename = u'{0:s}\\{1:s}.mui'.format(
                    message_filename_path, message_filename_name)

                  mui_message_file = self._OpenMessageResourceFile(
                      mui_message_filename)

                if mui_message_file:
                  message_file.Close()
                  message_file = mui_message_file

                  message_table = message_file.GetMessageTableResource()

            if not message_table:
              if message_filename not in self.missing_table_message_filenames:
                self.missing_table_message_filenames.append(message_filename)
            else:
              normalized_message_filename = message_filename.lower()

              if normalized_message_filename.startswith(
                  self._windows_path.lower()):
                normalized_message_filename = u'%SystemRoot%{0:s}'.format(
                    message_filename[len(self._windows_path):])

              elif normalized_message_filename.startswith(
                  u'%SystemRoot%'.lower()):
                normalized_message_filename = u'%SystemRoot%{0:s}'.format(
                    message_filename[len(u'%SystemRoot%'):])

              else:
                normalized_message_filename = message_filename

              output_writer.WriteMessageFile(
                  event_log_provider, message_file, normalized_message_filename)

            if message_filename != message_file.windows_path:
              processed_message_filenames.append(message_file.windows_path)
            processed_message_filenames.append(message_filename)

            message_file.Close()


class MessageResourceFile(object):
  """Class that defines a Windows Message Resource file."""

  _RESOURCE_IDENTIFIER_STRING = 0x06
  _RESOURCE_IDENTIFIER_MESSAGE_TABLE = 0x0b
  _RESOURCE_IDENTIFIER_VERSION = 0x10

  def __init__(
      self, windows_path, ascii_codepage='cp1252',
      preferred_language_identifier=0x0409):
    """Initializes the Windows Message Resource file.

    Args:
      windows_path: normalized version of the Windows path.
      ascii_codepage: optional ASCII string codepage. The default is cp1252
                      (or windows-1252).
      preferred_language_identifier: optional preferred language identifier
                                     (LCID). The default is 0x0409 (en-US).
    """
    super(MessageResourceFile, self).__init__()
    self._ascii_codepage = ascii_codepage
    self._exe_file = pyexe.file()
    self._exe_file.set_ascii_codepage(self._ascii_codepage)
    self._file_version = None
    self._is_open = False
    self._preferred_language_identifier = preferred_language_identifier
    self._product_version = None
    self._wrc_stream = pywrc.stream()
    # TODO: wrc stream set codepage?
    self.windows_path = windows_path

  def _GetVersionInformation(self):
    """Retrieves the file and product version."""
    version_resource = self._wrc_stream.get_resource_by_identifier(
        self._RESOURCE_IDENTIFIER_VERSION)
    if not version_resource:
      return None, None

    file_version = None
    product_version = None
    language_identifier = self._preferred_language_identifier
    if language_identifier in version_resource.language_identifiers:
      file_version = version_resource.get_file_version(language_identifier)
      product_version = version_resource.get_product_version(
          language_identifier)

    if not file_version or not product_version:
      for language_identifier in version_resource.language_identifiers:
        file_version = version_resource.get_file_version(language_identifier)
        product_version = version_resource.get_product_version(
            language_identifier)

        if file_version and product_version:
          break

    self._file_version = u'{0:d}.{1:d}.{2:d}.{3:d}'.format(
        (file_version >> 48) & 0xffff, (file_version >> 32) & 0xffff,
        (file_version >> 16) & 0xffff, file_version & 0xffff)

    self._product_version = u'{0:d}.{1:d}.{2:d}.{3:d}'.format(
        (product_version >> 48) & 0xffff, (product_version >> 32) & 0xffff,
        (product_version >> 16) & 0xffff, product_version & 0xffff)

    if file_version != product_version:
      logging.warning((
          u'Mismatch between file version: {0:s} and product version: '
          u'{1:s} in message file: {2:s}.').format(
              self._file_version, self._product_version, self.windows_path))

  @property
  def file_version(self):
    """The file version."""
    if self._file_version is None:
      self._GetVersionInformation()
    return self._file_version

  @property
  def product_version(self):
    """The product version."""
    if self._product_version is None:
      self._GetVersionInformation()
    return self._product_version

  def GetMessageTableResource(self):
    """Retrieves the message table resource."""
    return self._wrc_stream.get_resource_by_identifier(
        self._RESOURCE_IDENTIFIER_MESSAGE_TABLE)

  def GetMuiLanguage(self):
    """Retrieves the MUI language or None if not available."""
    mui_resource = self._wrc_stream.get_resource_by_name('MUI')
    if not mui_resource:
      return None

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

  def GetStringResource(self):
    """Retrieves the string resource."""
    return self._wrc_stream.get_resource_by_identifier(
        self._RESOURCE_IDENTIFIER_STRING)

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


class Sqlite3DatabaseFile(object):
  """Class that defines a sqlite3 database file."""

  _HAS_TABLE_QUERY = (
      u'SELECT name FROM sqlite_master '
      u'WHERE type = "table" AND name = "{0:s}"')

  def __init__(self):
    """Initializes the database file object."""
    super(Sqlite3DatabaseFile, self).__init__()
    self._connection = None
    self._cursor = None
    self.filename = None

  def Close(self):
    """Closes the database file."""
    # We need to run commit or not all data is stored in the database.
    self._connection.commit()
    self._connection.close()

    self._connection = None
    self._cursor = None
    self.filename = None

  def CreateTable(self, table_name, column_definitions):
    """Creates a table.

    Args:
      table_name: the table name.
      column_definitions: list of strings containing column definitions.
    """
    sql_query = u'CREATE TABLE {0:s} ( {1:s} )'.format(
        table_name, u', '.join(column_definitions))

    self._cursor.execute(sql_query)

  def HasTable(self, table_name):
    """Determines if a specific table exists.

    Args:
      table_name: the table name.

    Returns:
      True if the table exists, false otheriwse.
    """
    sql_query = self._HAS_TABLE_QUERY.format(table_name)

    self._cursor.execute(sql_query)
    if self._cursor.fetchone():
      has_table = True
    else:
      has_table = False
    return has_table

  def GetValues(self, table_name, column_names, condition):
    """Retrieves values from a table.

    Args:
      table_name: the table name.
      column_names: list of column names.
      condition: string containing the condition.

    Yields:
      A row object (instance of sqlite3.row).
    """
    sql_query = u'SELECT {1:s} FROM {0:s} WHERE {2:s}'.format(
        table_name, u', '.join(column_names), condition)

    self._cursor.execute(sql_query)

    for row in self._cursor:
      values = {}
      for column_index in range(0, len(column_names)):
        column_name = column_names[column_index]
        values[column_name] = row[column_index]
      yield values

  def InsertValues(self, table_name, column_names, values):
    """Inserts values into a table.

    Args:
      table_name: the table name.
      column_names: list of column names.
      values: list of values formatted as a string.
    """
    if not values:
      return

    sql_values = []
    for value in values:
      # In sqlite3 the double quote is escaped with a second double quote.
      value = u'"{0:s}"'.format(re.sub('"', '""', value))
      sql_values.append(value)

    sql_query = u'INSERT INTO {0:s} ( {1:s} ) VALUES ( {2:s} )'.format(
        table_name, u', '.join(column_names), u', '.join(sql_values))

    self._cursor.execute(sql_query)

  def Open(self, filename):
    """Opens the database file.

    Args:
      filename: the filename of the database.

    Returns:
      A boolean containing True if successful or False if not.
    """
    self.filename = filename
    self._connection = sqlite3.connect(filename)
    if not self._connection:
      return False

    self._cursor = self._connection.cursor()
    if not self._cursor:
      return False

    return True


class MessageFileWriter(object):
  """Class to represent a message file writer."""

  def __init__(self, message_file):
    """Initializes the message file writer object.

    Args:
      message_file: the message file (instance of MessageResourceFile).
    """
    super(MessageFileWriter, self).__init__()
    self._message_file = message_file


class Sqlite3EventProvidersWriter(object):
  """Class to represent a sqlite3 Event Log providers writer."""

  def __init__(self):
    """Initializes the Event Log providers writer object."""
    super(Sqlite3EventProvidersWriter, self).__init__()
    self._database_file = Sqlite3DatabaseFile()

  def Close(self):
    """Closes the Event Log providers writer object."""
    self._database_file.Close()

  def GetEventLogProviderKey(self, event_log_provider):
    """Retrieves the key of an Event Log provider.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
    """
    table_name = 'event_log_providers'
    column_names = ['event_log_provider_key']
    condition = 'log_source = "{0:s}" AND log_type = "{1:s}"'.format(
        event_log_provider.log_source, event_log_provider.log_type)
    values_list = list(self._database_file.GetValues(
        table_name, column_names, condition))

    if len(values_list) == 1:
      values = values_list[0]
      return values['event_log_provider_key']

    # TODO print error

  def GetMessageFileKey(self, message_file, message_filename):
    """Retrieves the key of a message file.

    Args:
      message_file: the message file (instance of MessageResourceFile).
      message_filename: the message filename.
    """
    table_name = 'message_files'
    column_names = ['message_file_key']
    condition = 'message_filename = "{0:s}"'.format(message_filename)
    values_list = list(self._database_file.GetValues(
        table_name, column_names, condition))

    if len(values_list) == 1:
      values = values_list[0]
      return values['message_file_key']

    # TODO print error

  def Open(self, filename):
    """Opens the Event Log providers writer object.

    Args:
      filename: the filename of the database.

    Returns:
      A boolean containing True if successful or False if not.
    """
    self._database_file.Open(filename)

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
    """
    table_name = 'event_log_providers'
    column_names = ['log_source', 'log_type']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      # TODO: write message files in a separate table and use the key
      # instead of writing the list.
      column_definitions = [
          'event_log_provider_key INTEGER PRIMARY KEY AUTOINCREMENT',
          'log_source TEXT', 'log_type TEXT']
      self._database_file.CreateTable(table_name, column_definitions)
      insert_values = True

    else:
      condition = 'log_source = "{0:s}" AND log_type = "{1:s}"'.format(
          event_log_provider.log_source, event_log_provider.log_type)
      values_list = list(self._database_file.GetValues(
          table_name, column_names, condition))

      if len(values_list) == 0:
        insert_values = True
      else:
        # TODO: check if more than 1 result.
        insert_values = False

    if insert_values:
      values = [event_log_provider.log_source, event_log_provider.log_type]
      self._database_file.InsertValues(table_name, column_names, values)

  def WriteMessageFile(
      self, message_file, message_filename, database_filename):
    """Writes the Windows Message Resource file.

    Args:
      message_file: the message file (instance of MessageResourceFile).
      message_filename: the message filename.
      database_filename: the database filename.
    """
    table_name = 'message_files'
    column_names = ['message_filename', 'database_filename']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          'message_file_key INTEGER PRIMARY KEY AUTOINCREMENT',
          'message_filename TEXT', 'database_filename TEXT']
      self._database_file.CreateTable(table_name, column_definitions)
      insert_values = True

    else:
      condition = 'message_filename = "{0:s}"'.format(message_filename)
      values_list = list(self._database_file.GetValues(
          table_name, column_names, condition))

      if len(values_list) == 0:
        insert_values = True
      else:
        # TODO: check if more than 1 result.
        insert_values = False

    if insert_values:
      values = [message_filename, database_filename]
      self._database_file.InsertValues(table_name, column_names, values)


class Sqlite3MessageFileWriter(MessageFileWriter):
  """Class to represent a sqlite3 message file writer."""

  def __init__(self, message_file):
    """Initializes the message file writer object.

    Args:
      message_file: the message file (instance of MessageResourceFile).
    """
    super(Sqlite3MessageFileWriter, self).__init__(message_file)
    self._database_file = Sqlite3DatabaseFile()

  def _WriteMessage(
      self, message_table, language_identifier, message_index, table_name,
      has_table):
    """Writes a message to a specific message table.

    Args:
      message_table: the message table (instance of pywrc.message_table).
      language_identifier: the language identifier (LCID).
      message_index: the message index.
      table_name: the name of the table.
      has_table: boolean value to indicate the table previously existed in
                 the database.
    """
    column_names = ['message_identifier', 'message_string']

    message_identifier = message_table.get_message_identifier(
        language_identifier, message_index)
    message_identifier = '0x{0:08x}'.format(message_identifier)

    message_string = message_table.get_string(
        language_identifier, message_index)

    if not has_table:
      values = [message_identifier, message_string]
      self._database_file.InsertValues(table_name, column_names, values)

    else:
      condition = 'message_identifier = "{0:s}"'.format(message_identifier)
      values_list = list(self._database_file.GetValues(
          table_name, column_names, condition))

      if len(values_list) == 1:
        values = values_list[0]
        if message_string != values['message_string']:
          logging.warning((
              u'Message string mismatch for LCID: 0x{0:08x}, '
              u'file version: {1:s}, message identifier: {2:s}.\n'
              u'Found: {2:s}\nStored: {3:s}\n').format(
                  language_identifier, self._message_file.file_version,
                  message_identifier, message_string,
                  values['message_string']))

      elif len(values_list) != 0:
        logging.warning((
             u'More than one message string found for LCID: 0x{0:08x}, '
             u'file version: {1:s}, message identifier: {2:s}.').format(
                 language_identifier, self._message_file.file_version,
                 message_identifier))

  def _WriteMessageTable(self, message_table, language_identifier):
    """Writes a message table for a specific language identifier.

    Args:
      message_table: the message table (instance of pywrc.message_table).
      language_identifier: the language identifier (LCID).
    """
    number_of_messages = message_table.get_number_of_messages(
        language_identifier)

    if number_of_messages > 0:
      table_name = u'message_table_0x{0:08x}_{1:s}'.format(
          language_identifier, self._message_file.file_version)
      table_name = re.sub('\.', '_', table_name)

      has_table = self._database_file.HasTable(table_name)
      if not has_table:
        column_definitions = ['message_identifier TEXT', 'message_string TEXT']
        self._database_file.CreateTable(table_name, column_definitions)

      for message_index in range(0, number_of_messages):
        self._WriteMessage(
            message_table, language_identifier, message_index, table_name,
            has_table)

  def Close(self):
    """Closes the message file writer object."""
    self._database_file.Close()

  def Open(self, filename):
    """Opens the message file writer object.

    Args:
      filename: the filename of the database.

    Returns:
      A boolean containing True if successful or False if not.
    """
    self._database_file.Open(filename)

  def WriteMessageTables(self):
    """Writes the message tables."""
    message_table = self._message_file.GetMessageTableResource()

    if message_table.number_of_languages > 0:
      for language_identifier in message_table.language_identifiers:
        self._WriteMessageTable(message_table, language_identifier)


class Sqlite3Writer(object):
  """Class that defines a sqlite3 output writer."""

  def __init__(self, databases_path):
    """Initializes the output writer object.

    Args:
      databases_path: the path to the database files.
    """
    super(Sqlite3Writer, self).__init__()
    self._databases_path = databases_path

  def Open(self):
    """Opens the output writer object.

    Returns:
      A boolean containing True if successful or False if not.
    """
    if not os.path.isdir(self._databases_path):
      return False

    self._event_providers_writer = Sqlite3EventProvidersWriter()
    self._event_providers_writer.Open(
        os.path.join(self._databases_path, 'winevt-kb.db'))

    return True

  def Close(self):
    """Closes the output writer object."""
    self._event_providers_writer.Close()

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
    """
    self._event_providers_writer.WriteEventLogProvider(event_log_provider)

  def WriteMessageFile(
      self, event_log_provider, message_file, message_filename):
    """Writes the Windows Message Resource file.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
      message_file: the message file (instance of MessageResourceFile).
      message_filename: the message filename.
    """
    _, _, database_filename = message_file.windows_path.rpartition(u'\\')
    database_filename = u'{0:s}.db'.format(database_filename.lower())
    database_filename = re.sub('\.mui', '', database_filename)

    message_file_writer = Sqlite3MessageFileWriter(message_file)
    message_file_writer.Open(
        os.path.join(self._databases_path, database_filename))
    message_file_writer.WriteMessageTables()
    message_file_writer.Close()

    self._event_providers_writer.WriteMessageFile(
        message_file, message_filename, database_filename)

    event_log_provider_key = self._event_providers_writer.GetEventLogProviderKey(
        event_log_provider)
    message_file_key = self._event_providers_writer.GetMessageFileKey(
        message_file, message_filename)

    # TODO: write the relationship between the event log provider and
    # the message file and the Windows version?


class StdoutWriter(object):
  """Class that defines a stdout output writer."""

  def _WriteMessageTable(self, message_table):
    """Writes the Windows Message Resource file message table.

    Args:
      message_table: the message table (instance of pywrc.message_table).
    """
    if message_table.number_of_languages > 0:
      for language_identifier in message_table.language_identifiers:
        number_of_messages = message_table.get_number_of_messages(
            language_identifier)

        if number_of_messages > 0:
          print u'Message table:'
          print u'LCID\t\t: 0x{0:08x}'.format(language_identifier)
          for message_index in range(0, number_of_messages):
            message_identifier = message_table.get_message_identifier(
                language_identifier, message_index)
            message_string = message_table.get_string(
                language_identifier, message_index)

            ouput_string = u'0x{0:08x}\t: {1:s}'.format(
                message_identifier, message_string)

            print ouput_string.encode('utf8')

          print ''

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
    """Writes the Event Log provider.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
    """
    print u'Source\t\t: {0:s}'.format(
        event_log_provider.log_source)

    print u'Event Log type\t: {0:s}'.format(
        event_log_provider.log_type)

    print u'Categories\t: {0:s}'.format(
        event_log_provider.category_message_files)

    print u'Messages\t: {0:s}'.format(
        event_log_provider.event_message_files)

    print ''

  def WriteMessageFile(
      self, event_log_provider, message_file, message_filename):
    """Writes the Windows Message Resource file.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
      message_file: the message file (instance of MessageResourceFile).
      message_filename: the message filename.
    """
    file_version = getattr(message_file, 'file_version', '')
    product_version = getattr(message_file, 'product_version', '')

    print u'Message file:'
    print u'Path\t\t: {0:s}'.format(message_file.windows_path)
    print u'File version\t: {0:s}'.format(file_version)
    print u'Product version\t: {0:s}'.format(product_version)

    message_table = message_file.GetMessageTableResource()
    self._WriteMessageTable(message_table)


class WikiMessageFileWriter(object):
  """Class to represent a Google Code wiki message file writer."""
  # TODO: aparantly the filename should only contain 1 dot and end with .wiki

  def Open(self, filename):
    """Opens the file.

    Args:
      filename: the filename.
    """
    # Using binary mode to make sure to write Unix end of lines.
    self._file = open(filename, 'wb')

  def Close(self):
    """Closes the file."""
    self._file.close()

  def WriteLine(self, line):
    """Writes a line."""
    self._file.write('{0:s}\r\n'.format(line))

  def WriteLines(self, lines):
    """Writes lines."""
    for line in lines:
      self.WriteLine(line)


class WikiWriter(object):
  """Class that defines a Google Code wiki output writer."""

  def __init__(self, wiki_path):
    """Initializes the Windows volume collector object.

    Args:
      wiki_path: the path to the directory containing the wiki files.
    """
    super(WikiWriter, self).__init__()
    self._wiki_path = wiki_path

  def _WriteMessageTable(self, message_table):
    """Writes the Windows Message Resource file message table.

    Args:
      message_table: the message table (instance of pywrc.message_table).
    """
    if message_table.number_of_languages > 0:
      for language_identifier in message_table.language_identifiers:
        number_of_messages = message_table.get_number_of_messages(
            language_identifier)

        if number_of_messages > 0:
          print '== LCID: 0x{0:08x} =='.format(language_identifier)
          print '|| *Message identifier* || *Message string* ||'

          for message_index in range(0, number_of_messages):
            message_identifier = message_table.get_message_identifier(
                language_identifier, message_index)
            message_string = message_table.get_string(
                language_identifier, message_index)

            message_string = re.sub(r'\n', '\\\\n', message_string)
            message_string = re.sub(r'\r', '\\\\r', message_string)
            message_string = re.sub(r'\t', '\\\\t', message_string)

            ouput_string = u'|| 0x{0:08x} || {{{{{{ {1:s} }}}}}} ||'.format(
                message_identifier, message_string)

            print ouput_string.encode('utf8')

          print ''

  def Close(self):
    """Closes the output writer object."""
    pass

  def Open(self):
    """Opens the output writer object.

    Returns:
      A boolean containing True if successful or False if not.
    """
    if not os.path.isdir(self._wiki_path):
      return False
    return True

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
    """
    # TODO: implement.
    return

  def WriteMessageFile(
      self, event_log_provider, message_file, message_filename):
    """Writes the Windows Message Resource file.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
      message_file: the message file (instance of MessageResourceFile).
      message_filename: the message filename.
    """
    # TODO: create file.

    file_version = getattr(message_file, 'file_version', '')
    product_version = getattr(message_file, 'product_version', '')

    print u'= Message file ='
    print u'|| *Path:* || {0:s} ||'.format(message_file.windows_path)
    print u'|| *File version:* || {0:s} ||'.format(file_version)
    print u'|| *Product version:* || {0:s} ||'.format(product_version)
    print ''

    message_table = message_file.GetMessageTableResource()
    self.WriteMessageTable(message_table)


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
      '--db', dest='database', action='store', metavar='./winevt-db/',
      default=None, help='path to write the sqlite3 databases to.')

  args_parser.add_argument(
      '--wiki', dest='wiki', action='store', metavar='./winevt-kb.wiki/',
      default=None, help='path to write the wiki pages to.')

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

  logging.basicConfig(
      level=logging.INFO, format=u'[%(levelname)s] %(message)s')

  if options.database:
    output_writer = Sqlite3Writer(options.database)
  elif options.wiki:
    output_writer = WikiWriter(options.wiki)
  else:
    output_writer = StdoutWriter()

  if not output_writer.Open():
    print u'Unable to open output writer.'
    print u''
    return False

  collector = EventMessageStringCollector()

  if not collector.GetWindowsVolumePathSpec(options.source):
    print (
        u'Unable to retrieve the volume with the Windows directory from: '
        u'{0:s}.').format(options.source)
    print ''
    return False

  if not collector.windows_version:
    if not options.windows_version:
      print u'Unable to determine Windows version.'

      if options.database:
        print u'Database output requires a Windows version, specify one with --winver.'
        print u''
        return False

    collector.windows_version = options.windows_version

  print u'Windows version: {0:s}.'.format(collector.windows_version)
  print u''

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

#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Script to extract the strings from Event Log message resource files."""

import argparse
import logging
import os
import re
import sys

import dfvfs
import pyexe
import pyregf
import pywrc

from dfvfs.lib import definitions as dfvfs_definitions
from dfvfs.lib import errors as dfvfs_errors
from dfvfs.helpers import source_scanner
from dfvfs.helpers import windows_path_resolver
from dfvfs.resolver import resolver
from dfvfs.volume import tsk_volume_system

import database
import resources


if dfvfs.__version__ < u'20140727':
  raise ImportWarning(u'extract.py requires dfvfs 20140727 or later.')

if pyexe.get_version() < u'20131229':
  raise ImportWarning(u'extract.py requires pyexe 20131229 or later.')

if pyregf.get_version() < u'20130716':
  raise ImportWarning(u'extract.py requires pyregf 20130716 or later.')

if pywrc.get_version() < u'20140128':
  raise ImportWarning(u'extract.py requires pywrc 20140128 or later.')


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
    self._scanner = source_scanner.SourceScanner()
    self._windows_directory = None

  def _ScanFileSystem(self, path_resolver):
    """Scans a file system for the Windows volume.

    Args:
      path_resolver: the path resolver (instance of dfvfs.WindowsPathResolver).

    Returns:
      True if the Windows directory was found, false otherwise.

    """
    result = False

    for windows_path in self._WINDOWS_DIRECTORIES:
      windows_path_spec = path_resolver.ResolvePath(windows_path)

      result = windows_path_spec is not None
      if result:
        self._windows_directory = windows_path
        break

    return result

  def _ScanTSKPartionVolumeSystemPathSpec(self, scan_context):
    """Scans a path specification for the Windows volume.

    Args:
      scan_context: the scan context (instance of dfvfs.ScanContext).

    Returns:
      The volume scan node (instance of dfvfs.SourceScanNode) of the volume
      that contains the Windows directory or None.

    Raises:
      CollectorError: if the scan context is invalid.
    """
    if (not scan_context or not scan_context.last_scan_node or
        not scan_context.last_scan_node.path_spec):
      raise CollectorError(u'Invalid scan context.')

    volume_system = tsk_volume_system.TSKVolumeSystem()
    volume_system.Open(scan_context.last_scan_node.path_spec)

    volume_identifiers = self._scanner.GetVolumeIdentifiers(volume_system)
    if not volume_identifiers:
      return

    volume_scan_node = None
    result = False

    for volume_identifier in volume_identifiers:
      volume_location = u'/{0:s}'.format(volume_identifier)
      volume_scan_node = scan_context.last_scan_node.GetSubNodeByLocation(
          volume_location)
      volume_path_spec = getattr(volume_scan_node, u'path_spec', None)

      # The leaf scan node shoudl contain the actual file system.
      file_system_scan_node = volume_scan_node.GetSubNodeByLocation(u'/')
      if not file_system_scan_node:
        continue

      while file_system_scan_node.sub_nodes:
        file_system_scan_node = file_system_scan_node.GetSubNodeByLocation(u'/')

      file_system_path_spec = getattr(file_system_scan_node, u'path_spec', None)
      file_system = resolver.Resolver.OpenFileSystem(file_system_path_spec)

      if file_system is None:
        continue

      path_resolver = windows_path_resolver.WindowsPathResolver(
          file_system, volume_path_spec)

      result = self._ScanFileSystem(path_resolver)
      if result:
        break

    if not result:
      return

    return volume_scan_node

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
    # Note that os.path.exists() does not support Windows device paths.
    if (not source_path.startswith(u'\\\\.\\') and
        not os.path.exists(source_path)):
      raise CollectorError(
          u'No such device, file or directory: {0:s}.'.format(source_path))

    scan_context = source_scanner.SourceScannerContext()
    scan_path_spec = None

    scan_context.OpenSourcePath(source_path)

    while True:
      last_scan_node = scan_context.last_scan_node
      try:
        scan_context = self._scanner.Scan(
            scan_context, scan_path_spec=scan_path_spec)
      except dfvfs_errors.BackEndError as exception:
        raise CollectorError(
            u'Unable to scan source, with error: {0:s}'.format(exception))

      # The source is a directory or file.
      if scan_context.source_type in [
          scan_context.SOURCE_TYPE_DIRECTORY, scan_context.SOURCE_TYPE_FILE]:
        break

      if (not scan_context.last_scan_node or
          scan_context.last_scan_node == last_scan_node):
        raise CollectorError(
            u'No supported file system found in source: {0:s}.'.format(
                self._source_path))

      # The source scanner found a file system.
      if scan_context.last_scan_node.type_indicator in [
          dfvfs_definitions.TYPE_INDICATOR_TSK]:
        break

      # The source scanner found a BitLocker encrypted volume and we need
      # a credential to unlock the volume.
      if scan_context.last_scan_node.type_indicator in [
          dfvfs_definitions.TYPE_INDICATOR_BDE]:
        # TODO: ask for password.
        raise CollectorError(
            u'BitLocker encrypted volume not yet supported.')

      # The source scanner found a partition table and we need to determine
      # which partition contains the Windows directory.
      elif scan_context.last_scan_node.type_indicator in [
          dfvfs_definitions.TYPE_INDICATOR_TSK_PARTITION]:
        scan_node = self._ScanTSKPartionVolumeSystemPathSpec(scan_context)
        if not scan_node:
          return False
        scan_context.last_scan_node = scan_node

      # The source scanner found Volume Shadow Snapshot which is ignored.
      elif scan_context.last_scan_node.type_indicator in [
          dfvfs_definitions.TYPE_INDICATOR_VSHADOW]:
        # Get the scan node of the current volume.
        scan_node = scan_context.last_scan_node.GetSubNodeByLocation(u'/')
        scan_context.last_scan_node = scan_node
        break

      else:
        raise CollectorError(
            u'Unsupported volume system found in source: {0:s}.'.format(
                self._source_path))

    # TODO: add single file support.
    if scan_context.source_type == scan_context.SOURCE_TYPE_FILE:
      raise CollectorError(
          u'Unsupported source: {0:s}.'.format(source_path))

    if scan_context.source_type != scan_context.SOURCE_TYPE_DIRECTORY:
      if not scan_context.last_scan_node.type_indicator in [
          dfvfs_definitions.TYPE_INDICATOR_TSK]:
        raise CollectorError(
            u'Unsupported source: {0:s} found unsupported file system.'.format(
                source_path))

    file_system_path_spec = getattr(
        scan_context.last_scan_node, u'path_spec', None)
    self._file_system = resolver.Resolver.OpenFileSystem(
        file_system_path_spec)

    if file_system_path_spec.type_indicator in [
        dfvfs_definitions.TYPE_INDICATOR_OS]:
      mount_point = file_system_path_spec
    else:
      mount_point = file_system_path_spec.parent

    self._path_resolver = windows_path_resolver.WindowsPathResolver(
        self._file_system, mount_point)

    # The source is a directory or single volume storage media image.
    if not self._windows_directory:
      if not self._ScanFileSystem(self._path_resolver):
        return False

    if not self._windows_directory:
      return False

    self._path_resolver.SetEnvironmentVariable(
        u'WinDir', self._windows_directory)

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


class EventMessageStringExtractor(WindowsVolumeCollector):
  """Class that defines an event message string extractor."""

  def __init__(self):
    """Initializes the event message string extractor object."""
    super(EventMessageStringExtractor, self).__init__()
    self._system_root = None
    self._windows_version = None
    self.ascii_codepage = u'cp1252'
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
        self._windows_directory, u'System32', u'config', u'SYSTEM'])

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
          u'SystemRoot', self._system_root)

    return self._system_root

  def _GetSystemRootFromRegistry(self):
    """Determines the value of %SystemRoot% from the SOFTWARE Registry file.

       The Windows path resolver is updated to expand this environment variable.

    Returns:
      A string containing the System Root or None otherwise.
    """
    registry_filename = u'\\'.join([
        self._windows_directory, u'System32', u'config', u'SOFTWARE'])

    registry_file = self._OpenRegistryFile(registry_filename)
    system_root = registry_file.GetSystemRoot()
    registry_file.Close()

    if system_root:
      system_root = system_root
    else:
      system_root = self._windows_directory

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
          system_root, u'System32', u'\\kernel32.dll'])
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

    return self._OpenMessageResourceFileByPathSpec(path_spec)

  def _OpenMessageResourceFileByPathSpec(self, path_spec):
    """Opens the message resource file specificed by the path specification.

    Args:
      path_spec: the path specification (instance of dfvfs.PathSpec).

    Returns:
      The message resource file (instance of MessageResourceFile) or None.
    """
    windows_path = self._path_resolver.GetWindowsPath(path_spec)
    if windows_path is None:
      logging.warning(u'Unable to retrieve Windows path.')

    try:
      file_object = resolver.Resolver.OpenFileObject(path_spec)
    except IOError as exception:
      logging.warning(u'Unable to open: {0:s} with error: {1:s}'.format(
          path_spec.comparable, exception))
      file_object = None

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

  def _ExtractMessageFile(
      self, output_writer, processed_message_filenames, event_log_provider,
      message_filename, message_file_type):
    """Extracts the Event Log message strings from a message file.

    Args:
      output_writer: the output writer (instance of OutputWriter).
      processed_message_filenames: a list of the processed message filenames.
      event_log_provider: the Event Log provider (instance of EventLogProvider).
      message_filename: string containing the message filename.
      message_file_type: string containing the message file type.
    """
    if message_filename in processed_message_filenames:
      return

    path_spec = self._path_resolver.ResolvePath(message_filename)
    if path_spec is not None:
      file_entry = self._file_system.GetFileEntryByPathSpec(path_spec)

      # If message_filename points to a directory try appending the Event Log
      # provider log source as the file name.
      if file_entry.IsDirectory():
        message_filename = u'\\'.join([
            message_filename, event_log_provider.log_source])
        path_spec = self._path_resolver.ResolvePath(message_filename)

    if path_spec is not None:
      message_file = self._OpenMessageResourceFileByPathSpec(path_spec)
    else:
      message_file = None

    mui_message_filename = None

    if not message_file:
      if message_filename in self.invalid_message_filenames:
        self.invalid_message_filenames.append(message_filename)
      return

    if message_file.windows_path in processed_message_filenames:
      message_file.Close()
      return

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
          self._windows_directory.lower()):
        normalized_message_filename = u'%SystemRoot%{0:s}'.format(
            message_filename[len(self._windows_directory):])

      elif normalized_message_filename.startswith(
          u'%SystemRoot%'.lower()):
        normalized_message_filename = u'%SystemRoot%{0:s}'.format(
            message_filename[len(u'%SystemRoot%'):])

      else:
        normalized_message_filename = message_filename

      logging.info(u'Processing: {0:s}'.format(normalized_message_filename))

      message_file.windows_path = normalized_message_filename

      output_writer.WriteMessageFile(
          event_log_provider, message_file, normalized_message_filename,
          message_file_type)

    if message_filename != message_file.windows_path:
      processed_message_filenames.append(message_file.windows_path)
    processed_message_filenames.append(message_filename)

    message_file.Close()

  def ExtractEventLogMessageStrings(self, output_writer):
    """Extracts the Event Log message strings from the message files.

    Args:
      output_writer: the output writer (instance of OutputWriter).
    """
    self.invalid_message_filenames = []
    self.missing_table_message_filenames = []
    processed_message_filenames = []
    event_log_types = self._CollectEventLogTypes()

    for _, event_log_sources in event_log_types.iteritems():
      for _, event_log_provider in event_log_sources.iteritems():
        output_writer.WriteEventLogProvider(event_log_provider)

        if event_log_provider.event_message_files:
          for message_filename in event_log_provider.event_message_files:
            self._ExtractMessageFile(
                output_writer, processed_message_filenames, event_log_provider,
                message_filename, database.MESSAGE_FILE_TYPE_EVENT)

        if event_log_provider.category_message_files:
          for message_filename in event_log_provider.category_message_files:
            self._ExtractMessageFile(
                output_writer, processed_message_filenames, event_log_provider,
                message_filename, database.MESSAGE_FILE_TYPE_CATEGORY)

        if event_log_provider.parameter_message_files:
          for message_filename in event_log_provider.parameter_message_files:
            self._ExtractMessageFile(
                output_writer, processed_message_filenames, event_log_provider,
                message_filename, database.MESSAGE_FILE_TYPE_PARAMETER)


class MessageResourceFile(object):
  """Class that defines a Windows Message Resource file."""

  _RESOURCE_IDENTIFIER_STRING = 0x06
  _RESOURCE_IDENTIFIER_MESSAGE_TABLE = 0x0b
  _RESOURCE_IDENTIFIER_VERSION = 0x10

  def __init__(
      self, windows_path, ascii_codepage=u'cp1252',
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
    self._file_object = None
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
    mui_resource = self._wrc_stream.get_resource_by_name(u'MUI')
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
    exe_section = self._exe_file.get_section_by_name(u'.rsrc')

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

  def __init__(self, ascii_codepage=u'cp1252'):
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
        u'Microsoft\\Windows NT\\CurrentVersion')

    if current_version_key:
      system_root_value = current_version_key.get_value_by_name(u'SystemRoot')
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

    select_key = self._regf_file.get_key_by_path(u'Select')

    if select_key:
      current_value = select_key.get_value_by_name(u'Current')
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
      eventlog_key_path = u'ControlSet{0:03d}\\Services\\EventLog'.format(
          control_set)

      eventlog_key = self._regf_file.get_key_by_path(eventlog_key_path)

      if eventlog_key:
        for log_type_key in eventlog_key.sub_keys:
          log_type = log_type_key.name

          for log_source_key in log_type_key.sub_keys:
            log_source = log_source_key.name

            provider_guid_value = log_source_key.get_value_by_name(
                u'ProviderGuid')

            if provider_guid_value:
              provider_guid = provider_guid_value.data_as_string
            else:
              provider_guid = None

            event_log_provider = resources.EventLogProvider(
                log_type, log_source, provider_guid)

            category_message_file_value = log_source_key.get_value_by_name(
                u'CategoryMessageFile')

            if category_message_file_value:
              event_log_provider.SetCategoryMessageFilenames(
                  category_message_file_value.data_as_string)

            event_message_file_value = log_source_key.get_value_by_name(
                u'EventMessageFile')

            if event_message_file_value:
              event_log_provider.SetEventMessageFilenames(
                  event_message_file_value.data_as_string)

            parameter_message_file_value = log_source_key.get_value_by_name(
                u'ParameterMessageFile')

            if parameter_message_file_value:
              event_log_provider.SetParameterMessageFilenames(
                  parameter_message_file_value.data_as_string)

            yield event_log_provider


class Sqlite3OutputWriter(object):
  """Class that defines a sqlite3 output writer."""

  EVENT_PROVIDERS_DATABASE_FILENAME = u'winevt-kb.db'

  def __init__(self, databases_path):
    """Initializes the output writer object.

    Args:
      databases_path: the path to the database files.
    """
    super(Sqlite3OutputWriter, self).__init__()
    self._databases_path = databases_path
    self._database_writer = None

  def Close(self):
    """Closes the output writer object."""
    self._database_writer.Close()
    self._database_writer = None

  def Open(self):
    """Opens the output writer object.

    Returns:
      A boolean containing True if successful or False if not.
    """
    if not os.path.isdir(self._databases_path):
      return False

    self._database_writer = database.EventProvidersSqlite3DatabaseWriter()
    self._database_writer.Open(os.path.join(
        self._databases_path, self.EVENT_PROVIDERS_DATABASE_FILENAME))

    return True

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
    """
    self._database_writer.WriteEventLogProvider(event_log_provider)

  def WriteMessageFile(
      self, event_log_provider, message_resource_file, message_filename,
      message_file_type):
    """Writes the Windows Message Resource file.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
      message_resource_file: the message file (instance of MessageResourceFile).
      message_filename: string containing the message filename.
      message_file_type: string containing the message file type.
    """
    database_filename = message_resource_file.windows_path
    _, _, database_filename = database_filename.rpartition(u'\\')
    database_filename = u'{0:s}.db'.format(database_filename.lower())
    database_filename = re.sub(r'\.mui', '', database_filename)

    database_writer = database.MessageFileSqlite3DatabaseWriter(
        message_resource_file)
    database_writer.Open(
        os.path.join(self._databases_path, database_filename))
    database_writer.WriteResources()
    database_writer.Close()

    self._database_writer.WriteMessageFile(message_filename, database_filename)

    # TODO: write the relationship between the event log provider and
    # the message file and the Windows version?
    self._database_writer.WriteMessageFilesPerEventLogProvider(
        event_log_provider, message_filename, message_file_type)


class StdoutOutputWriter(object):
  """Class that defines a stdout output writer."""

  def _WriteMessageTable(self, message_table):
    """Writes the Windows Message Resource file message table.

    Args:
      message_table: the message table (instance of pywrc.message_table).
    """
    try:
      number_of_languages = message_table.get_number_of_languages()
    except IOError as exception:
      number_of_languages = 0
      logging.warning(
          u'Unable to retrieve number of languages with error: {0:s}.'.format(
              exception))

    if number_of_languages > 0:
      for language_identifier in message_table.language_identifiers:
        number_of_messages = message_table.get_number_of_messages(
            language_identifier)

        if number_of_messages > 0:
          print(u'Message table:')
          print(u'LCID\t\t: 0x{0:08x}'.format(language_identifier))
          for message_index in range(0, number_of_messages):
            message_identifier = message_table.get_message_identifier(
                language_identifier, message_index)
            message_string = message_table.get_string(
                language_identifier, message_index)

            ouput_string = u'0x{0:08x}\t: {1:s}'.format(
                message_identifier, message_string)

            print(ouput_string.encode(u'utf8'))

          print(u'')

  def Close(self):
    """Closes the output writer object."""
    pass

  def Open(self):
    """Opens the output writer object.

    Returns:
      A boolean containing True if successful or False if not.
    """
    return True

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
    """
    print(u'Source\t\t: {0:s}'.format(
        event_log_provider.log_source))

    print(u'Event Log type\t: {0:s}'.format(
        event_log_provider.log_type))

    print(u'Categories\t: {0:s}'.format(
        event_log_provider.category_message_files))

    print(u'Messages\t: {0:s}'.format(
        event_log_provider.event_message_files))

    print(u'Parameters\t: {0:s}'.format(
        event_log_provider.parameter_message_files))

    print(u'')

  def WriteMessageFile(
      self, unused_event_log_provider, message_file, unused_message_filename,
      unused_message_type):
    """Writes the Windows Message Resource file.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
      message_file: the message file (instance of MessageResourceFile).
      message_filename: string containing the message filename.
      message_file_type: string containing the message file type.
    """
    file_version = getattr(message_file, u'file_version', u'')
    product_version = getattr(message_file, u'product_version', u'')

    print(u'Message file:')
    print(u'Path\t\t: {0:s}'.format(message_file.windows_path))
    print(u'File version\t: {0:s}'.format(file_version))
    print(u'Product version\t: {0:s}'.format(product_version))

    message_table = message_file.GetMessageTableResource()
    self._WriteMessageTable(message_table)


def Main():
  """The main program function.

  Returns:
    A boolean containing True if successful or False if not.
  """
  args_parser = argparse.ArgumentParser(description=(
      u'Extract strings from message resource files for Event Log sources.'))

  args_parser.add_argument(
      u'source', nargs=u'?', action=u'store', metavar=u'/mnt/c/',
      default=None, help=(
          u'path of the volume containing C:\\Windows or the filename of '
          u'a storage media image containing the C:\\Windows directory.'))

  args_parser.add_argument(
      u'--db', u'--database', dest=u'database', action=u'store',
      metavar=u'./winevt-kb/', default=None, help=(
          u'directory to write the sqlite3 databases to.'))

  args_parser.add_argument(
      u'--winver', dest=u'windows_version', action=u'store', metavar=u'xp',
      default=None, help=(
          u'string that identifies the Windows version in the database.'))

  options = args_parser.parse_args()

  if not options.source:
    print(u'Source value is missing.')
    print(u'')
    args_parser.print_help()
    print(u'')
    return False

  logging.basicConfig(
      level=logging.INFO, format=u'[%(levelname)s] %(message)s')

  if options.database:
    if not os.path.exists(options.database):
      os.mkdir(options.database)

    if not os.path.isdir(options.database):
      print(u'{0:s} must be a directory'.format(options.database))
      print(u'')
      return False

    output_writer = Sqlite3OutputWriter(options.database)
  else:
    output_writer = StdoutOutputWriter()

  if not output_writer.Open():
    print(u'Unable to open output writer.')
    print(u'')
    return False

  extractor = EventMessageStringExtractor()

  if not extractor.GetWindowsVolumePathSpec(options.source):
    print((u'Unable to retrieve the volume with the Windows directory from: '
           u'{0:s}.').format(options.source))
    print(u'')
    return False

  if not extractor.windows_version:
    if not options.windows_version:
      print(u'Unable to determine Windows version.')

      if options.database:
        print(u'Database output requires a Windows version, specify one with '
              u'--winver.')
        print(u'')
        return False

    extractor.windows_version = options.windows_version

  print(u'Windows version: {0:s}.'.format(extractor.windows_version))
  print(u'')

  extractor.ExtractEventLogMessageStrings(output_writer)
  output_writer.Close()

  if extractor.invalid_message_filenames:
    print(u'Message resource files not found or without resource section:')
    for message_filename in extractor.invalid_message_filenames:
      print(u'{0:s}'.format(message_filename))
    print(u'')

  if extractor.missing_table_message_filenames:
    print(u'Message resource files without a message table resource:')
    for message_filename in extractor.missing_table_message_filenames:
      print(u'{0:s}'.format(message_filename))
    print(u'')

  return True


if __name__ == u'__main__':
  if not Main():
    sys.exit(1)
  else:
    sys.exit(0)

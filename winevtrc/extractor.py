# -*- coding: utf-8 -*-
"""Classes to represent a Windows Event Log message resource extractor."""

import logging

from dfvfs.helpers import volume_scanner as dfvfs_volume_scanner
from dfvfs.resolver import resolver as dfvfs_resolver
from dfwinreg import interface as dfwinreg_interface
from dfwinreg import regf as dfwinreg_regf
from dfwinreg import registry as dfwinreg_registry

from winevtrc import definitions
from winevtrc import resource_file
from winevtrc import resources


class EventMessageStringRegistryFileReader(
    dfwinreg_interface.WinRegistryFileReader):
  """Class that defines a Windows Registry file reader."""

  def __init__(self, volume_scanner):
    """Initializes a Windows Registry file reader.

    Args:
      volume_scanner (WindowsVolumeScanner): Windows volume scanner.
    """
    super(EventMessageStringRegistryFileReader, self).__init__()
    self._volume_scanner = volume_scanner

  def Open(self, path, ascii_codepage=u'cp1252'):
    """Opens the Windows Registry file specificed by the path.

    Args:
      path (str): path of the Windows Registry file. The path is a Windows path
          relative to the root of the file system that contains the specfic
          Windows Registry file. E.g.  C:\\Windows\\System32\\config\\SYSTEM
      ascii_codepage (Optional[str]): ASCII string codepage.

    Returns:
      WinRegistryFile: Windows Registry file or None if the file cannot
          be opened.
    """
    file_object = self._volume_scanner.OpenFile(path)
    if file_object is None:
      return

    registry_file = dfwinreg_regf.REGFWinRegistryFile(
        ascii_codepage=ascii_codepage)

    try:
      registry_file.Open(file_object)
    except IOError:
      file_object.close()
      return

    return registry_file


class EventMessageStringExtractor(dfvfs_volume_scanner.WindowsVolumeScanner):
  """Class that defines a Windows Event Log message string extractor.

  Attributes:
    ascii_codepage (str): ASCII string codepage.
    invalid_message_filenames (list[str]): invalid message file names.
    missing_table_message_filenames (list[str]): message file names, where the
        message table resource is missing.
    preferred_language_identifier (int): preferred language identifier (LCID).
  """

  def __init__(self, debug=False, mediator=None):
    """Initializes a Windows Event Log message string extractor.

    Args:
      debug (Optional[bool]): True if debug information should be printed.
      mediator (dfvfs.VolumeScannerMediator): a volume scanner mediator or None.
    """
    super(EventMessageStringExtractor, self).__init__(mediator=mediator)
    registry_file_reader = EventMessageStringRegistryFileReader(self)

    self._debug = debug
    self._registry = dfwinreg_registry.WinRegistry(
        registry_file_reader=registry_file_reader)
    self._windows_version = None

    self.ascii_codepage = u'cp1252'
    self.invalid_message_filenames = []
    self.missing_table_message_filenames = []
    self.preferred_language_identifier = 0x0409

  @property
  def windows_version(self):
    """The Windows version (getter)."""
    if self._windows_version is None:
      self._windows_version = self._GetWindowsVersion()
    return self._windows_version

  @windows_version.setter
  def windows_version(self, value):
    """The Windows version (setter)."""
    self._windows_version = value

  def _CollectEventLogTypes(self, all_control_sets=False):
    """Collects the Event Log types.

    Args:
      all_control_sets (Optional[bool]): True if all control sets should
          be processed or only the current control set.

    Returns:
      dict[str, dict[str, EventLogProvider]]: Event Log providers per event
          log type.
    """
    event_log_types = {}
    for event_log_provider in self._GetEventLogProviders(
        all_control_sets=all_control_sets):
      if event_log_provider.log_type not in event_log_types:
        event_log_types[event_log_provider.log_type] = {}

      event_log_sources = event_log_types[event_log_provider.log_type]
      if event_log_provider.log_source in event_log_sources:
        logging.warning((
            u'Found duplicate Event Log source: {0:s} in type: {1:s}.').format(
                event_log_provider.log_source, event_log_provider.log_type))

      event_log_sources[event_log_provider.log_source] = event_log_provider

    return event_log_types

  def _CollectEventLogProvidersFromKey(self, eventlog_key):
    """Retrieves the Event Log providers from a specific key.

    Args:
      eventlog_key (dfwinreg.WinRegistryKey): Event Log key.

    Yields:
      EventLogProvider: Event Log provider.
    """
    if not eventlog_key:
      return

    for log_type_key in eventlog_key.GetSubkeys():
      log_type = log_type_key.name

      for log_source_key in log_type_key.GetSubkeys():
        log_source = log_source_key.name

        provider_guid_value = log_source_key.GetValueByName(u'ProviderGuid')

        if provider_guid_value:
          provider_guid = provider_guid_value.GetDataAsObject()
        else:
          provider_guid = None

        event_log_provider = resources.EventLogProvider(
            log_type, log_source, provider_guid)

        category_message_file_value = log_source_key.GetValueByName(
            u'CategoryMessageFile')

        if category_message_file_value:
          event_log_provider.SetCategoryMessageFilenames(
              category_message_file_value.GetDataAsObject())

        event_message_file_value = log_source_key.GetValueByName(
            u'EventMessageFile')

        if event_message_file_value:
          event_log_provider.SetEventMessageFilenames(
              event_message_file_value.GetDataAsObject())

        parameter_message_file_value = log_source_key.GetValueByName(
            u'ParameterMessageFile')

        if parameter_message_file_value:
          event_log_provider.SetParameterMessageFilenames(
              parameter_message_file_value.GetDataAsObject())

        yield event_log_provider

  def _ExtractMessageFile(
      self, output_writer, processed_message_filenames, event_log_provider,
      message_filename, message_file_type):
    """Extracts the Event Log message strings from a message file.

    Args:
      output_writer (OutputWriter): output writer.
      processed_message_filenames (list[str]): processed message filenames.
      event_log_provider (EventLogProvider): Event Log provider.
      message_filename (str): message filename.
      message_file_type (str): message file type.
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
      mui_language = message_file.GetMUILanguage()

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

  def _GetEventLogProviders(self, all_control_sets=False):
    """Retrieves the Event Log providers.

    Args:
      all_control_sets (Optional[bool]): True if all control sets should
          be processed or only the current control set.

    Yields:
      EventLogProvider: Event Log provider.
    """
    if all_control_sets:
      system_key = self._registry.GetKeyByPath(u'HKEY_LOCAL_MACHINE\\System\\')
      if not system_key:
        return

      for control_set_key in system_key.GetSubkeys():
        if control_set_key.name.startswith(u'ControlSet'):
          eventlog_key = control_set_key.GetSubkeyByPath(
              u'Services\\EventLog')
          if eventlog_key:
            logging.info(u'Control set: {0:s}'.format(control_set_key.name))
            for event_log_provider in self._CollectEventLogProvidersFromKey(
                eventlog_key):
              yield event_log_provider

    else:
      eventlog_key = self._registry.GetKeyByPath(
          u'HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\EventLog')
      if eventlog_key:
        logging.info(u'Current control set')
        for event_log_provider in self._CollectEventLogProvidersFromKey(
            eventlog_key):
          yield event_log_provider

  def _GetSystemRoot(self):
    """Determines the value of %SystemRoot%.

    Returns:
      str: value of SystemRoot or None if the value cannot be determined.
    """
    current_version_key = self._registry.GetKeyByPath(
        u'HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion')

    system_root = None
    if current_version_key:
      system_root_value = current_version_key.GetValueByName(u'SystemRoot')
      if system_root_value:
        system_root = system_root_value.GetDataAsObject()

    if not system_root:
      system_root = self._windows_directory

    return system_root

  def _GetWindowsVersion(self):
    """Determines the Windows version from kernel executable file.

    Returns:
      str: Windows version or None otherwise.
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
      return

    return message_file.file_version

  def _OpenMessageResourceFile(self, windows_path):
    """Opens the message resource file specificed by the Windows path.

    Args:
      windows_path (str): Windows path containing the messagge resource
          filename.

    Returns:
      MessageResourceFile: message resource file or None.
    """
    path_spec = self._path_resolver.ResolvePath(windows_path)
    if path_spec is None:
      return

    return self._OpenMessageResourceFileByPathSpec(path_spec)

  def _OpenMessageResourceFileByPathSpec(self, path_spec):
    """Opens the message resource file specificed by the path specification.

    Args:
      path_spec (dfvfs.PathSpec): path specification.

    Returns:
      MessageResourceFile: message resource file or None.
    """
    windows_path = self._path_resolver.GetWindowsPath(path_spec)
    if windows_path is None:
      logging.warning(u'Unable to retrieve Windows path.')

    try:
      file_object = dfvfs_resolver.Resolver.OpenFileObject(path_spec)
    except IOError as exception:
      logging.warning(u'Unable to open: {0:s} with error: {1:s}'.format(
          path_spec.comparable, exception))
      file_object = None

    if file_object is None:
      return

    message_file = resource_file.MessageResourceFile(
        windows_path, ascii_codepage=self.ascii_codepage,
        preferred_language_identifier=self.preferred_language_identifier)
    if not message_file.OpenFileObject(file_object):
      return

    return message_file

  def ExtractEventLogMessageStrings(self, output_writer):
    """Extracts the Event Log message strings from the message files.

    Args:
      output_writer (OutputWriter): output writer.
    """
    # TODO: have CLI argument control this mode.
    all_control_sets = False

    self.invalid_message_filenames = []
    self.missing_table_message_filenames = []
    processed_message_filenames = []
    event_log_types = self._CollectEventLogTypes(
        all_control_sets=all_control_sets)

    for _, event_log_sources in iter(event_log_types.items()):
      for _, event_log_provider in iter(event_log_sources.items()):
        output_writer.WriteEventLogProvider(event_log_provider)

        if event_log_provider.event_message_files:
          for message_filename in event_log_provider.event_message_files:
            self._ExtractMessageFile(
                output_writer, processed_message_filenames, event_log_provider,
                message_filename, definitions.MESSAGE_FILE_TYPE_EVENT)

        if event_log_provider.category_message_files:
          for message_filename in event_log_provider.category_message_files:
            self._ExtractMessageFile(
                output_writer, processed_message_filenames, event_log_provider,
                message_filename, definitions.MESSAGE_FILE_TYPE_CATEGORY)

        if event_log_provider.parameter_message_files:
          for message_filename in event_log_provider.parameter_message_files:
            self._ExtractMessageFile(
                output_writer, processed_message_filenames, event_log_provider,
                message_filename, definitions.MESSAGE_FILE_TYPE_PARAMETER)

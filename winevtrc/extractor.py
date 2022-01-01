# -*- coding: utf-8 -*-
"""Windows Event Log message resource extractor."""

import logging

from dfvfs.helpers import volume_scanner as dfvfs_volume_scanner
from dfvfs.resolver import resolver as dfvfs_resolver
from dfwinreg import interface as dfwinreg_interface
from dfwinreg import regf as dfwinreg_regf
from dfwinreg import registry as dfwinreg_registry

from winevtrc import eventlog_providers
from winevtrc import resource_file


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

  def Open(self, path, ascii_codepage='cp1252'):
    """Opens the Windows Registry file specified by the path.

    Args:
      path (str): path of the Windows Registry file. The path is a Windows path
          relative to the root of the file system that contains the specific
          Windows Registry file. E.g.  C:\\Windows\\System32\\config\\SYSTEM
      ascii_codepage (Optional[str]): ASCII string codepage.

    Returns:
      WinRegistryFile: Windows Registry file or None if the file cannot
          be opened.
    """
    file_object = self._volume_scanner.OpenFile(path)
    if file_object is None:
      return None

    registry_file = dfwinreg_regf.REGFWinRegistryFile(
        ascii_codepage=ascii_codepage)

    try:
      registry_file.Open(file_object)
    except IOError:
      file_object.close()
      return None

    return registry_file


class EventMessageStringExtractor(dfvfs_volume_scanner.WindowsVolumeScanner):
  """Class that defines a Windows Event Log message string extractor.

  Attributes:
    ascii_codepage (str): ASCII string codepage.
    missing_message_filenames (list[str]): names of message files that were
        not found or without a resource section.
    missing_resources_message_filenames (list[str]): names of message files,
        where both a string and a message table resource is missing.
    preferred_language_identifier (int): preferred language identifier (LCID).
  """

  _SERVICES_EVENTLOG_KEY_PATH = (
      'HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\EventLog')

  _WINEVT_PUBLISHERS_KEY_PATH = (
      'HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\'
      'WINEVT\\Publishers')

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
    self._processed_message_filenames = []
    self._windows_version = None

    self.ascii_codepage = 'cp1252'
    self.missing_message_filenames = []
    self.missing_resources_message_filenames = []
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

  def _GetMUIMessageResourceFile(
      self, message_file_path, message_resource_file):
    """Retrieves a MUI Event Log message resource file.

    Args:
      message_file_path (str): path of the message file.
      message_resource_file (MessageResourceFile): language neutral message
          resource file.

    Returns:
      MessageResourceFile: MUI message resource file or None if not available.
    """
    mui_language = message_resource_file.GetMUILanguage()
    if not mui_language:
      return None

    path, _, name = message_file_path.rpartition('\\')

    mui_message_file_path = '{0:s}\\{1:s}\\{2:s}.mui'.format(
        path, mui_language, name)
    mui_message_resource_file = self._OpenMessageResourceFile(
        mui_message_file_path)

    if not mui_message_resource_file:
      mui_message_file_path = '{0:s}\\{1:s}.mui'.format(path, name)
      mui_message_resource_file = self._OpenMessageResourceFile(
          mui_message_file_path)

    if mui_message_resource_file:
      logging.info('Processing MUI message file: {0:s}'.format(
          mui_message_file_path))

    return mui_message_resource_file

  def _GetNormalizedMessageFilename(self, message_file_path):
    """Retrieves a normalized path of an Event Log message file.

    Args:
      message_file_path (str): path of a message file.

    Returns:
      str: normalized path of a message file.
    """
    message_file_path_lower = message_file_path.lower()

    if message_file_path_lower.startswith(self._windows_directory.lower()):
      return '%SystemRoot%{0:s}'.format(message_file_path[
          len(self._windows_directory):])

    if message_file_path_lower.startswith('%SystemRoot%'.lower()):
      return '%SystemRoot%{0:s}'.format(message_file_path[
          len('%SystemRoot%'):])

    return message_file_path

  def _GetSystemRoot(self):
    """Determines the value of %SystemRoot%.

    Returns:
      str: value of SystemRoot or None if the value cannot be determined.
    """
    current_version_key = self._registry.GetKeyByPath(
        'HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion')

    system_root = None
    if current_version_key:
      system_root_value = current_version_key.GetValueByName('SystemRoot')
      if system_root_value:
        system_root = system_root_value.GetDataAsObject()

    if not system_root:
      system_root = self._windows_directory

    return system_root

  def _GetValueAsStringFromKey(
      self, registry_key, value_name, default_value=''):
    """Retrieves a value as a string from a Registry value.

    Args:
      registry_key (dfwinreg.WinRegistryKey): Windows Registry key.
      value_name (str): name of the value.
      default_value (Optional[str]): default value.

    Returns:
      str: value or the default value if not available.
    """
    if not registry_key:
      return default_value

    value = registry_key.GetValueByName(value_name)
    if not value:
      return default_value

    return value.GetDataAsObject()

  def _GetWindowsSystemPath(self, path):
    """Retrieves a Windows system path.

    Args:
      path (str): Windows path with environment variables.

    Returns:
      tuple[str, str]: Windows system path and filename.
    """
    path, _, filename = path.rpartition('\\')

    # If the path is just a filename assume the file is stored in:
    # "%SystemRoot%\System32".
    if not path:
      path = '%SystemRoot%\\System32'

    return '\\'.join([path, filename])

  def _GetWindowsVersion(self):
    """Determines the Windows version from kernel executable file.

    Returns:
      str: Windows version or None otherwise.
    """
    system_root = self._GetSystemRoot()

    # Window NT variants.
    kernel_executable_path = '\\'.join([
        system_root, 'System32', 'ntoskrnl.exe'])
    message_file = self._OpenMessageResourceFile(kernel_executable_path)

    if not message_file:
      # Window 9x variants.
      kernel_executable_path = '\\'.join([
          system_root, 'System32', '\\kernel32.dll'])
      message_file = self._OpenMessageResourceFile(kernel_executable_path)

    if not message_file:
      return None

    return message_file.file_version

  def _OpenMessageResourceFile(self, windows_path):
    """Opens the message resource file specified by the Windows path.

    Args:
      windows_path (str): Windows path containing the message resource
          filename.

    Returns:
      MessageResourceFile: message resource file or None.
    """
    path_spec = self._path_resolver.ResolvePath(windows_path)
    if path_spec is None:
      return None

    return self._OpenMessageResourceFileByPathSpec(path_spec)

  def _OpenMessageResourceFileByPathSpec(self, path_spec):
    """Opens the message resource file specified by the path specification.

    Args:
      path_spec (dfvfs.PathSpec): path specification.

    Returns:
      MessageResourceFile: message resource file or None.
    """
    windows_path = self._path_resolver.GetWindowsPath(path_spec)
    if windows_path is None:
      logging.warning('Unable to retrieve Windows path.')

    try:
      file_object = dfvfs_resolver.Resolver.OpenFileObject(path_spec)
    except IOError as exception:
      logging.warning('Unable to open: {0:s} with error: {1:s}'.format(
          path_spec.comparable, exception))
      file_object = None

    if file_object is None:
      return None

    message_file = resource_file.MessageResourceFile(
        windows_path, ascii_codepage=self.ascii_codepage,
        preferred_language_identifier=self.preferred_language_identifier)
    if not message_file.OpenFileObject(file_object):
      return None

    return message_file

  def CollectEventLogProviders(self):
    """Retrieves the Event Log providers.

    Returns:
      generator[EventLogProvider]: Event Log providers generator.
    """
    # TODO: have CLI argument control this mode.
    # all_control_sets = False

    collector_object = eventlog_providers.EventLogProvidersCollector()
    return collector_object.Collect(self._registry)

  def GetMessageResourceFile(self, event_log_provider, message_filename):
    """Retrieves an Event Log message resource file.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
      message_filename (str): message filename.

    Returns:
      MessageResourceFile: message resource file or None if not available or
          already processed.
    """
    lookup_path = message_filename.lower()
    if lookup_path in self._processed_message_filenames:
      return None

    message_file_path = self._GetWindowsSystemPath(message_filename)

    path_spec = self._path_resolver.ResolvePath(message_file_path)
    if path_spec:
      file_entry = self._file_system.GetFileEntryByPathSpec(path_spec)

      # If message_file_path points to a directory try appending the Event Log
      # provider log source as the file name.
      if file_entry.IsDirectory():
        logging.info('Message file: {0:s} refers to directory'.format(
            message_filename))

        for log_source in event_log_provider.log_sources:
          message_file_path = '\\'.join([message_file_path, log_source])
          path_spec = self._path_resolver.ResolvePath(message_file_path)
          if path_spec:
            break

    message_resource_file = None
    if path_spec:
      message_resource_file = self._OpenMessageResourceFileByPathSpec(path_spec)

    if not message_resource_file:
      if message_filename not in self.missing_message_filenames:
        self.missing_message_filenames.append(message_filename)

      logging.warning('Missing message file: {0:s}'.format(message_filename))
      return None

    # Skip message file if it was already processed but was referenced
    # by a different path.
    lookup_path = message_resource_file.windows_path.lower()
    if lookup_path in self._processed_message_filenames:
      message_resource_file.Close()
      return None

    message_table_resource = message_resource_file.GetMessageTableResource()
    if not message_table_resource:
      # Windows Vista and later use a MUI resource to redirect to
      # a language specific message file.
      mui_message_resource_file = self._GetMUIMessageResourceFile(
          message_file_path, message_resource_file)
      if mui_message_resource_file:
        message_resource_file.Close()
        message_resource_file = mui_message_resource_file

        message_table_resource = message_resource_file.GetMessageTableResource()

    if not message_table_resource:
      string_resource = message_resource_file.GetStringResource()
      if not string_resource:
        if message_filename not in self.missing_resources_message_filenames:
          self.missing_resources_message_filenames.append(message_filename)

      logging.warning(
          'Message table resource missing from message file: {0:s}'.format(
              message_filename))

      message_resource_file.Close()

      return None

    message_resource_file.windows_path = self._GetNormalizedMessageFilename(
        message_file_path)

    if message_file_path != message_resource_file.windows_path:
      self._processed_message_filenames.append(
          message_resource_file.windows_path.lower())

    self._processed_message_filenames.append(message_filename.lower())

    return message_resource_file

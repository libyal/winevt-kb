# -*- coding: utf-8 -*-
"""Windows Event Log message resource extractor."""

import logging

from dfimagetools import environment_variables
from dfimagetools import windows_registry

from dfvfs.helpers import volume_scanner as dfvfs_volume_scanner
from dfvfs.resolver import resolver as dfvfs_resolver

from dfwinreg import registry as dfwinreg_registry

from winevtrc import eventlog_providers
from winevtrc import resource_file


class EventMessageStringExtractor(dfvfs_volume_scanner.WindowsVolumeScanner):
  """Windows Event Log message string extractor.

  Attributes:
    ascii_codepage (str): ASCII string codepage.
    missing_message_filenames (list[str]): names of message files that were
        not found or without a resource section.
    missing_resources_message_filenames (list[str]): names of message files,
        where both a string and a message table resource is missing.
    preferred_language_identifier (int): preferred language identifier (LCID).
  """

  # Environment variables used in Windows paths.
  _PATH_ENVIRONMENT_VARIABLES = (
      '%COMMONPROGRAMFILES%',
      '%COMMONPROGRAMFILES(X86)%',
      '%COMMONPROGRAMW6432%',
      '%PROGRAMDATA%',
      '%PROGRAMFILES%',
      '%PROGRAMFILES(X86)%',
      '%PROGRAMW6432%',
      '%PUBLIC%')

  def __init__(self, debug=False, mediator=None):
    """Initializes a Windows Event Log message string extractor.

    Args:
      debug (Optional[bool]): True if debug information should be printed.
      mediator (dfvfs.VolumeScannerMediator): a volume scanner mediator or None.
    """
    super(EventMessageStringExtractor, self).__init__(mediator=mediator)
    self._debug = debug
    self._registry = None
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

    mui_message_file_path = '\\'.join([path, mui_language, f'{name:s}.mui'])
    mui_message_resource_file = self._OpenMessageResourceFile(
        mui_message_file_path)

    if not mui_message_resource_file:
      mui_message_file_path = '\\'.join([path, f'{name:s}.mui'])
      mui_message_resource_file = self._OpenMessageResourceFile(
          mui_message_file_path)

    if mui_message_resource_file:
      logging.info((
          f'Message file: {message_file_path:s} references MUI message file: '
          f'{mui_message_file_path:s}'))

    return mui_message_resource_file

  def _GetNormalizedPath(self, path):
    """Retrieves a normalized variant of a path.

    Args:
      path (str): path of a message file.

    Returns:
      str: normalized path of a message file.
    """
    path_segments = path.split('\\')

    if path_segments:
      # Check if the first path segment is a drive letter or "%SystemDrive%".
      first_path_segment = path_segments[0].lower()
      if ((len(first_path_segment) == 2 and first_path_segment[1:] == ':') or
          first_path_segment == '%systemdrive%'):
        path_segments[0] = ''

      # Check if the second path segment is "Windows".
      if (len(path_segments) >= 2 and path_segments[0] == '' and
          path_segments[1].lower() == 'windows'):
        path_segments.pop(0)
        path_segments[0] = '%SystemRoot%'

    return '\\'.join(path_segments) or '\\'

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
      logging.warning(
          f'Unable to open: {path_spec.comparable:s} with error: {exception!s}')
      file_object = None

    if file_object is None:
      return None

    message_file = resource_file.MessageResourceFile(
        windows_path, ascii_codepage=self.ascii_codepage,
        preferred_language_identifier=self.preferred_language_identifier)
    message_file.OpenFileObject(file_object)

    return message_file

  def CollectEventLogProviders(self):
    """Retrieves the Event Log providers.

    Yields:
      EventLogProvider: Event Log provider.
    """
    # TODO: have CLI argument control this mode.
    # all_control_sets = False

    collector = eventlog_providers.EventLogProvidersCollector()
    for event_log_provider in collector.Collect(self._registry):
      event_log_provider.category_message_files = [
          self.GetNormalizedMessageFilePath(path)
          for path in event_log_provider.category_message_files]

      event_log_provider.event_message_files = [
          self.GetNormalizedMessageFilePath(path)
          for path in event_log_provider.event_message_files]

      event_log_provider.parameter_message_files = [
          self.GetNormalizedMessageFilePath(path)
          for path in event_log_provider.parameter_message_files]

      yield event_log_provider

  def CollectSystemEnvironmentVariables(self):
    """Collects the system environment variables."""
    collector = environment_variables.WindowsEnvironmentVariablesCollector()

    for environment_variable in collector.Collect(self._registry):
      if environment_variable.name.upper() in self._PATH_ENVIRONMENT_VARIABLES:
        normalized_path = self._GetNormalizedPath(environment_variable.value)
        self._path_resolver.SetEnvironmentVariable(
            environment_variable.name[1:-1], normalized_path)

  def GetMessageResourceFile(self, event_log_provider, message_filename):
    """Retrieves an Event Log message resource file.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
      message_filename (str): message filename.

    Returns:
      MessageResourceFile: message resource file or None if not available or
          already processed.
    """
    normalized_message_file_path = self.GetNormalizedMessageFilePath(
        message_filename)

    # Skip message file if it was already processed.
    lookup_path = normalized_message_file_path.lower()
    if lookup_path in self._processed_message_filenames:
      return None

    path_spec = self._path_resolver.ResolvePath(normalized_message_file_path)
    if path_spec:
      file_entry = self._file_system.GetFileEntryByPathSpec(path_spec)

      # If normalized_message_file_path points to a directory try appending
      # the Event Log provider log source as the file name.
      if file_entry.IsDirectory():
        logging.info(f'Message file: {message_filename:s} refers to directory')

        for log_source in event_log_provider.log_sources:
          message_file_path = '\\'.join([
              normalized_message_file_path, log_source])
          path_spec = self._path_resolver.ResolvePath(message_file_path)
          if path_spec:
            break

    message_resource_file = None
    if path_spec:
      message_resource_file = self._OpenMessageResourceFileByPathSpec(path_spec)

    if not message_resource_file:
      logging.warning(f'Missing message file: {message_filename:s}')

      if message_filename not in self.missing_message_filenames:
        self.missing_message_filenames.append(message_filename)

      return None

    if not message_resource_file.HasMessageTableResource():
      # Windows Vista and later use a MUI resource to redirect to
      # a language specific message file.
      mui_message_resource_file = self._GetMUIMessageResourceFile(
          normalized_message_file_path, message_resource_file)
      if mui_message_resource_file:
        message_resource_file.Close()

        message_resource_file = mui_message_resource_file

    if not message_resource_file.HasMessageTableResource():
      logging.warning((
          f'Message table resource missing from message file: '
          f'{message_filename:s}'))

      if message_filename not in self.missing_resources_message_filenames:
        self.missing_resources_message_filenames.append(message_filename)

      message_resource_file.Close()

      return None

    message_resource_file.windows_path = normalized_message_file_path

    lookup_path = normalized_message_file_path.lower()
    self._processed_message_filenames.append(lookup_path)

    return message_resource_file

  def GetNormalizedMessageFilePath(self, path):
    """Retrieves a normalized variant of a message file path.

    Args:
      path (str): path of a message file.

    Returns:
      str: normalized path of a message file.
    """
    path_segments = path.split('\\')
    filename = path_segments.pop()

    if path_segments:
      # Check if the first path segment is a drive letter or "%SystemDrive%".
      first_path_segment = path_segments[0].lower()
      if ((len(first_path_segment) == 2 and first_path_segment[1:] == ':') or
          first_path_segment == '%systemdrive%'):
        path_segments[0] = ''

    path_segments_lower = [
        path_segment.lower() for path_segment in path_segments]

    if not path_segments_lower:
      # If the path is a filename assume the file is stored in:
      # "%SystemRoot%\System32".
      path_segments = ['%SystemRoot%', 'System32']

    elif path_segments_lower[0] in ('system32', '$(runtime.system32)'):
        # Note that the path can be relative so if it starts with "System32"
        # assume this represents "%SystemRoot%\System32".
      path_segments = ['%SystemRoot%', 'System32'] + path_segments[1:]

    elif path_segments_lower[0] in (
        '%systemroot%', '%windir%', '$(runtime.windows)'):
      path_segments = ['%SystemRoot%'] + path_segments[1:]

    # Check if path starts with "\SystemRoot\", "\Windows\" or "\WinNT\" for
    # example: "\SystemRoot\system32\drivers\SerCx.sys"
    elif not path_segments_lower[0] and path_segments_lower[1] in (
        'systemroot', 'windows', 'winnt'):
      path_segments = ['%SystemRoot%'] + path_segments[2:]

    path_segments.append(filename)
    return '\\'.join(path_segments) or '\\'

  def ScanForWindowsVolume(self, source_path, options=None):
    """Scans for a Windows volume.

    Args:
      source_path (str): source path.
      options (Optional[VolumeScannerOptions]): volume scanner options. If None
          the default volume scanner options are used, which are defined in the
          VolumeScannerOptions class.

    Returns:
      bool: True if a Windows volume was found.

    Raises:
      ScannerError: if the source path does not exists, or if the source path
          is not a file or directory, or if the format of or within
          the source file is not supported.
    """
    result = super(EventMessageStringExtractor, self).ScanForWindowsVolume(
        source_path, options=options)
    if not result:
      return False

    registry_file_reader = (
        windows_registry.StorageMediaImageWindowsRegistryFileReader(
            self._file_system, self._path_resolver))
    self._registry = dfwinreg_registry.WinRegistry(
        registry_file_reader=registry_file_reader)

    return True

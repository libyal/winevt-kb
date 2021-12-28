# -*- coding: utf-8 -*-
"""Windows Event Log message resource extractor."""

import logging

from dfvfs.helpers import volume_scanner as dfvfs_volume_scanner
from dfvfs.resolver import resolver as dfvfs_resolver
from dfwinreg import interface as dfwinreg_interface
from dfwinreg import regf as dfwinreg_regf
from dfwinreg import registry as dfwinreg_registry

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
    invalid_message_filenames (list[str]): invalid message file names.
    missing_table_message_filenames (list[str]): message file names, where the
        message table resource is missing.
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

  def _CollectEventLogProvidersFromPublishersKeys(self, winevt_publishers_key):
    """Retrieves Event Log providers from a WINEVT publishers key.

    Args:
      winevt_publishers_key (dfwinreg.WinRegistryKey): WINEVT publishers key.

    Yield:
      EventLogProvider: Event Log provider.
    """
    if winevt_publishers_key:
      for guid_key in winevt_publishers_key.GetSubkeys():
        log_source = self._GetValueAsStringFromKey(guid_key, '')

        event_message_files = self._GetValueAsStringFromKey(
            guid_key, 'MessageFileName', default_value='')
        event_message_files = sorted(filter(None, [
            path.strip().lower() for path in event_message_files.split(';')]))

        provider_identifier = guid_key.name.lower()

        eventlog_provider = resources.EventLogProvider(
            '', log_source, provider_identifier)
        eventlog_provider.category_message_files = []
        eventlog_provider.event_message_files = event_message_files
        eventlog_provider.parameter_message_files = []

        yield eventlog_provider

  def _CollectEventLogProvidersFromRegistry(self, registry):
    """Retrieves the Event Log providers from a Windows Registry.

    Args:
      registry (dfwinreg.WinRegistry): Windows Registry.

    Returns:
      list[EventLogProvider]: Event Log providers.
    """
    services_eventlog_key = registry.GetKeyByPath(
        self._SERVICES_EVENTLOG_KEY_PATH)
    winevt_publishers_key = registry.GetKeyByPath(
        self._WINEVT_PUBLISHERS_KEY_PATH)

    if not services_eventlog_key and not winevt_publishers_key:
      return []

    eventlog_providers_per_identifier = {}
    eventlog_providers_per_log_source = {}

    for eventlog_provider in self._CollectEventLogProvidersFromServicesKey(
        services_eventlog_key):
      existing_eventlog_provider = eventlog_providers_per_identifier.get(
          eventlog_provider.provider_guid, None)
      if existing_eventlog_provider:
        self._UpdateExistingEventLogProvider(
            existing_eventlog_provider, eventlog_provider)
        continue

      if eventlog_provider.log_source in eventlog_providers_per_log_source:
        logging.warning((
            'Found multiple definitions for Event Log provider: '
            '{0:s}').format(eventlog_provider.log_source))
        continue

      eventlog_providers_per_log_source[
          eventlog_provider.log_source] = eventlog_provider

      if eventlog_provider.provider_guid:
        eventlog_providers_per_identifier[eventlog_provider.provider_guid] = (
              eventlog_provider)

    for eventlog_provider in self._CollectEventLogProvidersFromPublishersKeys(
        winevt_publishers_key):
      existing_eventlog_provider = eventlog_providers_per_log_source.get(
          eventlog_provider.log_source, None)
      if not existing_eventlog_provider:
        existing_eventlog_provider = eventlog_providers_per_identifier.get(
            eventlog_provider.provider_guid, None)

        if existing_eventlog_provider:
          existing_eventlog_provider.log_source_alias = (
              existing_eventlog_provider.log_source)
          existing_eventlog_provider.log_source = eventlog_provider.log_source

      if existing_eventlog_provider:
        # TODO: handle mismatches where message files don't define a path.

        if not existing_eventlog_provider.event_message_files:
          existing_eventlog_provider.event_message_files = (
              eventlog_provider.event_message_files)
        elif eventlog_provider.event_message_files not in (
            [], existing_eventlog_provider.event_message_files):
          logging.warning((
              'Mismatch in event message files of alternate definition: '
              '{0:s} for Event Log provider: {1:s}').format(
                  existing_eventlog_provider.log_source_alias or '',
                  existing_eventlog_provider.log_source))

        if not existing_eventlog_provider.provider_guid:
          existing_eventlog_provider.provider_guid = (
              eventlog_provider.provider_guid)
        elif existing_eventlog_provider.provider_guid != (
            eventlog_provider.provider_guid):
          logging.warning((
              'Mismatch in provider identifier of alternate definition: '
              '{0:s} for Event Log provider: {1:s}').format(
                  existing_eventlog_provider.log_source_alias or '',
                  existing_eventlog_provider.log_source))

      else:
        eventlog_providers_per_log_source[eventlog_provider.log_source] = (
            eventlog_provider)
        eventlog_providers_per_identifier[eventlog_provider.provider_guid] = (
            eventlog_provider)

    return [eventlog_provider for _, eventlog_provider in sorted(
        eventlog_providers_per_log_source.items())]

  def _CollectEventLogProvidersFromServicesKey(self, services_eventlog_key):
    """Retrieves Event Log providers from a services Event Log key.

    Args:
      services_eventlog_key (dfwinreg.WinRegistryKey): services Event Log key.

    Yield:
      EventLogProvider: Event Log provider.
    """
    if services_eventlog_key:
      for log_type_key in services_eventlog_key.GetSubkeys():
        for provider_key in log_type_key.GetSubkeys():
          log_source = provider_key.name
          log_type = log_type_key.name

          category_message_files = self._GetValueAsStringFromKey(
              provider_key, 'CategoryMessageFile', default_value='')
          category_message_files = sorted(filter(None, [
              path.strip().lower()
              for path in category_message_files.split(';')]))

          event_message_files = self._GetValueAsStringFromKey(
              provider_key, 'EventMessageFile', default_value='')
          event_message_files = sorted(filter(None, [
              path.strip().lower() for path in event_message_files.split(';')]))

          parameter_message_files = self._GetValueAsStringFromKey(
              provider_key, 'ParameterMessageFile', default_value='')
          parameter_message_files = sorted(filter(None, [
              path.strip().lower()
              for path in parameter_message_files.split(';')]))

          provider_identifier = self._GetValueAsStringFromKey(
              provider_key, 'ProviderGuid')
          if provider_identifier:
            provider_identifier = provider_identifier.lower()

          eventlog_provider = resources.EventLogProvider(
              log_type, log_source, provider_identifier)
          eventlog_provider.category_message_files = category_message_files
          eventlog_provider.event_message_files = event_message_files
          eventlog_provider.parameter_message_files = parameter_message_files

          yield eventlog_provider

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

  def _UpdateExistingEventLogProvider(
      self, existing_eventlog_provider, eventlog_provider):
    """Updates an existing Event Log provider.

    Args:
      existing_eventlog_provider (EventLogProvider): existing Event Log
          provider.
      eventlog_provider (EventLogProvider): Event Log provider.
    """
    if existing_eventlog_provider.log_source_alias not in (
        None, eventlog_provider.log_source):
      logging.warning('Event Log provider: {0:s} already has an alias'.format(
          existing_eventlog_provider.log_source))
    else:
      existing_eventlog_provider.log_source_alias = (
          eventlog_provider.log_source)

    if not existing_eventlog_provider.category_message_files:
      existing_eventlog_provider.category_message_files = (
          eventlog_provider.category_message_files)
    elif eventlog_provider.category_message_files not in (
        [], existing_eventlog_provider.category_message_files):
      logging.warning((
          'Mismatch in category message files of alternate definition: '
          '{0:s} for Event Log provider: {1:s}').format(
              eventlog_provider.log_source,
              existing_eventlog_provider.log_source))

    if not existing_eventlog_provider.event_message_files:
      existing_eventlog_provider.event_message_files = (
          eventlog_provider.event_message_files)
    elif eventlog_provider.event_message_files not in (
        [], existing_eventlog_provider.event_message_files):
      logging.warning((
          'Mismatch in event message files of alternate definition: '
          '{0:s} for Event Log provider: {1:s}').format(
              eventlog_provider.log_source,
              existing_eventlog_provider.log_source))

    if not existing_eventlog_provider.parameter_message_files:
      existing_eventlog_provider.parameter_message_files = (
          eventlog_provider.parameter_message_files)
    elif eventlog_provider.parameter_message_files not in (
        [], existing_eventlog_provider.parameter_message_files):
      logging.warning((
          'Mismatch in provider message files of alternate definition: '
          '{0:s} for Event Log provider: {1:s}').format(
              eventlog_provider.log_source,
              existing_eventlog_provider.log_source))

  def ExtractEventLogProviders(self):
    """Extracts Event Log providers.

    Returns:
      generator(EventLogProvider): Event Log provider generator.
    """
    # TODO: have CLI argument control this mode.
    # all_control_sets = False

    return self._CollectEventLogProvidersFromRegistry(self._registry)

  def GetMessageFile(self, event_log_provider, message_filename):
    """Retrieves an Event Log message file.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
      message_filename (str): message filename.

    Returns:
      MessageFile: message file.
    """
    path_spec = self._path_resolver.ResolvePath(message_filename)
    if path_spec is not None:
      file_entry = self._file_system.GetFileEntryByPathSpec(path_spec)

      # If message_filename points to a directory try appending the Event Log
      # provider log source as the file name.
      if file_entry.IsDirectory():
        message_filename = '\\'.join([
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
      return None

    if message_file.windows_path in self._processed_message_filenames:
      message_file.Close()
      return None

    message_table = message_file.GetMessageTableResource()
    if not message_table:
      # Windows Vista and later use a MUI resource to redirect to
      # a language specific message file.
      mui_language = message_file.GetMUILanguage()

      if mui_language:
        message_filename_path, _, message_filename_name = (
            message_filename.rpartition('\\'))

        mui_message_filename = '{0:s}\\{1:s}\\{2:s}.mui'.format(
            message_filename_path, mui_language, message_filename_name)

        mui_message_file = self._OpenMessageResourceFile(
            mui_message_filename)

        if not mui_message_file:
          mui_message_filename = '{0:s}\\{1:s}.mui'.format(
              message_filename_path, message_filename_name)

          mui_message_file = self._OpenMessageResourceFile(
              mui_message_filename)

        if mui_message_file:
          logging.info('Processing MUI message file: {0:s}'.format(
              mui_message_filename))

          message_file.Close()
          message_file = mui_message_file

          message_table = message_file.GetMessageTableResource()

    if not message_table:
      if message_filename not in self.missing_table_message_filenames:
        self.missing_table_message_filenames.append(message_filename)

      message_file.Close()

      return None

    normalized_message_filename = message_filename.lower()

    if normalized_message_filename.startswith(
        self._windows_directory.lower()):
      normalized_message_filename = '%SystemRoot%{0:s}'.format(
          message_filename[len(self._windows_directory):])

    elif normalized_message_filename.startswith(
        '%SystemRoot%'.lower()):
      normalized_message_filename = '%SystemRoot%{0:s}'.format(
          message_filename[len('%SystemRoot%'):])

    else:
      normalized_message_filename = message_filename

    message_file.windows_path = normalized_message_filename

    if message_filename != message_file.windows_path:
      self._processed_message_filenames.append(message_file.windows_path)

    return message_file

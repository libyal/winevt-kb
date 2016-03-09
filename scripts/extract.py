#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Script to extract the strings from Event Log message resource files."""

from __future__ import print_function
import argparse
import logging
import os
import re
import sys

import pyexe
import pywrc

from dfvfs.resolver import resolver
from dfwinreg import registry

from winevtrc import collector
from winevtrc import database
from winevtrc import resource_file
from winevtrc import resources


if pyexe.get_version() < u'20131229':
  raise ImportWarning(u'extract.py requires pyexe 20131229 or later.')

if pywrc.get_version() < u'20140128':
  raise ImportWarning(u'extract.py requires pywrc 20140128 or later.')


# pylint: disable=logging-format-interpolation

class EventMessageStringExtractor(collector.WindowsVolumeCollector):
  """Class that defines an event message string extractor."""

  def __init__(self, debug=False, mediator=None):
    """Initializes the event message string extractor object.

    Args:
      debug: optional boolean value to indicate if debug information should
             be printed.
      mediator: a volume scanner mediator (instance of
                dfvfs.VolumeScannerMediator) or None.
    """
    super(EventMessageStringExtractor, self).__init__(mediator=mediator)
    self._debug = debug
    registry_file_reader = collector.CollectorRegistryFileReader(self)
    self._registry = registry.WinRegistry(
        registry_file_reader=registry_file_reader)
    self._windows_version = None

    self.ascii_codepage = u'cp1252'
    self.invalid_message_filenames = None
    self.missing_table_message_filenames = None
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

  def _CollectEventLogTypes(self):
    """Collects the event log types.

    Returns:
      A dictionary containing a dictionary of event log providers per event
      log type. E.g. { 'Application': { 'EventSystem': instance of
                                        EventLogProvider, ... }, ... }
    """
    event_log_types = {}
    for event_log_provider in self._GetEventLogProviders():
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
      eventlog_key: the event log key object (instance of
                    dfwinreg.WinRegistryKey).

    Yields:
      An event log provider object (instance of EventLogProvider).
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

  def _GetEventLogProviders(self):
    """Retrieves the Event Log providers.

    Yields:
      An event log provider object (instance of EventLogProvider).
    """
    # TODO: have CLI argument control this mode.
    all_control_sets = False
    if all_control_sets:
      system_key = self._registry.GetKeyByPath(u'HKEY_LOCAL_MACHINE\\System\\')
      if not system_key:
        return

      for control_set_key in system_key.GetSubkeys():
        if control_set_key.name.startswith(u'ControlSet'):
          eventlog_key = control_set_key.GetSubkeyByPath(
              u'Services\\EventLog')
          if eventlog_key:
            print(u'Control set: {0:s}'.format(control_set_key.name))
            for event_log_provider in self._CollectEventLogProvidersFromKey(
                eventlog_key):
              yield event_log_provider

    else:
      eventlog_key = self._registry.GetKeyByPath(
          u'HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\EventLog')
      if eventlog_key:
        print(u'Current control set')
        for event_log_provider in self._CollectEventLogProvidersFromKey(
            eventlog_key):
          yield event_log_provider

  def _GetSystemRoot(self):
    """Determines the value of %SystemRoot%.

    Returns:
      A string containing the value of SystemRoot or None if the value cannot
      be determined.
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

    message_file = resource_file.MessageResourceFile(
        windows_path, ascii_codepage=self.ascii_codepage,
        preferred_language_identifier=self.preferred_language_identifier)
    if not message_file.Open(file_object):
      return None

    return message_file

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
  argument_parser = argparse.ArgumentParser(description=(
      u'Extract strings from message resource files for Event Log sources.'))

  argument_parser.add_argument(
      u'-d', u'--debug', dest=u'debug', action=u'store_true', default=False,
      help=u'enable debug output.')

  argument_parser.add_argument(
      u'--db', u'--database', dest=u'database', action=u'store',
      metavar=u'./winevt-kb/', default=None, help=(
          u'directory to write the sqlite3 databases to.'))

  argument_parser.add_argument(
      u'--winver', dest=u'windows_version', action=u'store', metavar=u'xp',
      default=None, help=(
          u'string that identifies the Windows version in the database.'))

  argument_parser.add_argument(
      u'source', nargs=u'?', action=u'store', metavar=u'/mnt/c/',
      default=None, help=(
          u'path of the volume containing C:\\Windows or the filename of '
          u'a storage media image containing the C:\\Windows directory.'))

  options = argument_parser.parse_args()

  if not options.source:
    print(u'Source value is missing.')
    print(u'')
    argument_parser.print_help()
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

  # TODO: pass mediator.
  extractor = EventMessageStringExtractor(debug=options.debug)

  if not extractor.ScanForWindowsVolume(options.source):
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

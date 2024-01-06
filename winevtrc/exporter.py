# -*- coding: utf-8 -*-
"""Windows Event Log message resource exporter."""

import abc
import difflib
import logging
import os

from acstore import sqlite_store

from winevtrc import resources
from winevtrc import storage  # pylint: disable=unused-import


class ExportEventLogProvider(object):
  """Event Log provider.

  Attributes:
    name (str): name.
    providers_with_versions (list[tuple[EventLogProvider, list[str]]]): Event
        Log providers with corresponding Windows versions.
  """

  def __init__(self, name):
    """Initialized an Event Log provider.

    Args:
      name (str): name.
    """
    super(ExportEventLogProvider, self).__init__()
    self.name = name
    self.providers_with_versions = []


class ExporterOutputWriter(object):
  """Exporter output writer."""

  @abc.abstractmethod
  def Close(self):
    """Closes the output writer."""

  @abc.abstractmethod
  def Open(self):
    """Opens the output writer.

    Returns:
      bool: True if successful or False if not.
    """

  @abc.abstractmethod
  def WriteEventLogProvider(self, export_event_log_provider):
    """Writes an Event Log provider.

    Args:
      export_event_log_provider (ExportEventLogProvider): Event Log provider.
    """

  @abc.abstractmethod
  def WriteMessageFile(self, message_file):
    """Writes a message file.

    Args:
      message_file (MessageFile): message file.
    """

  @abc.abstractmethod
  def WriteMessageFilesPerEventLogProvider(
      self, event_log_provider, message_file):
    """Writes a mapping between an Event Log provider and a message file.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
      message_file (MessageFile): message file.
    """


class Exporter(object):
  """Exports the strings extracted from Windows EventLog message files."""

  _EVENT_PROVIDERS_DATABASE_FILENAME = 'winevt-kb.db'

  def __init__(self):
    """Initializes a Windows Event Log message resource exporter."""
    super(Exporter, self).__init__()
    # TODO: refactor
    self._event_log_providers = {}

  def _CompareEventLogProviders(
      self, event_log_provider, other_event_log_provider):
    """Compares 2 Event Log providers to determine if they are equivalent.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
      other_event_log_provider (EventLogProvider): other Event Log provider.

    Returns:
      bool: True if the Event Log providers are equivalent, False otherwise.
    """
    if event_log_provider.identifier and (
       event_log_provider.identifier != other_event_log_provider.identifier):
      return False

    message_files = other_event_log_provider.category_message_files
    if event_log_provider.category_message_files and (
       event_log_provider.category_message_files != message_files):
      return False

    message_files = other_event_log_provider.event_message_files
    if event_log_provider.event_message_files and (
       event_log_provider.event_message_files != message_files):
      return False

    message_files = other_event_log_provider.parameter_message_files
    if event_log_provider.parameter_message_files and (
       event_log_provider.parameter_message_files != message_files):
      return False

    return True

  def _ExportEventLogProviders(self, database_reader, output_writer):
    """Exports the Event Log providers from an event provider database.

    Args:
      database_reader (SQLiteAttributeContainerStore): event provider database
          reader.
      output_writer (ExporterOutputWriter): output writer.
    """
    providers_per_log_source = {}

    for event_log_provider in database_reader.GetAttributeContainers(
        resources.EventLogProvider.CONTAINER_TYPE):
      name = event_log_provider.name
      if not name:
        log_sources = sorted(event_log_provider.log_sources)
        name = log_sources[0]

      is_equivalent = False

      export_event_log_provider = providers_per_log_source.get(name, None)
      if not export_event_log_provider:
        export_event_log_provider = ExportEventLogProvider(name)

        providers_per_log_source[name] = export_event_log_provider

        # TODO: refactor
        self._event_log_providers[name] = event_log_provider

      else:
        for existing_event_log_provider, windows_versions in (
            export_event_log_provider.providers_with_versions):
          is_equivalent = self._CompareEventLogProviders(
              event_log_provider, existing_event_log_provider)
          if is_equivalent:
            windows_versions.append(event_log_provider.windows_version)
            break

      if not is_equivalent:
        export_event_log_provider.providers_with_versions.append((
            event_log_provider, [event_log_provider.windows_version]))

    for export_event_log_provider in providers_per_log_source.values():
      output_writer.WriteEventLogProvider(export_event_log_provider)

  def _ExportMessageFile(self, message_file, message_file_database_path):
    """Exports a message file.

    Args:
      message_file (MessageFile): message file.
      message_file_database_path (str): path of the message file database.
    """
    database_reader = sqlite_store.SQLiteAttributeContainerStore()
    database_reader.Open(path=message_file_database_path, read_only=True)

    self._ExportMessageStrings(message_file, database_reader)

    database_reader.Close()

  def _ExportMessageFiles(self, source_path, database_reader, output_writer):
    """Exports the message files from an event provider database.

    Args:
      source_path (str): source path.
      database_reader (SQLiteAttributeContainerStore): event provider database
          reader.
      output_writer (ExporterOutputWriter): output writer.
    """
    for descriptor in database_reader.GetAttributeContainers(
        resources.MessageFileDatabaseDescriptor.CONTAINER_TYPE):
      message_file_database_path = os.path.join(
          source_path, descriptor.database_filename)
      if not os.path.exists(message_file_database_path):
        logging.warning(
            f'Missing message file database: {descriptor.database_filename:s}.')
        continue

      logging.info(f'Processing: {descriptor.database_filename:s}')

      # Strip ".db" from the database filename.
      name = descriptor.database_filename[:-3]
      message_file = resources.MessageFile(name)
      message_file.windows_path = descriptor.message_filename

      self._ExportMessageFile(message_file, message_file_database_path)

      output_writer.WriteMessageFile(message_file)

  def _ExportMessageFilesPerEventLogProvider(self, output_writer):
    """Exports the message files used by an Event Log provider.

    Args:
      output_writer (ExporterOutputWriter): output writer.
    """
    # TODO: refactor
    for event_log_provider in self._event_log_providers.values():
      for message_filename in event_log_provider.event_message_files:
        output_writer.WriteMessageFilesPerEventLogProvider(
            event_log_provider, message_filename)

  def _ExportMessageStrings(self, message_file, database_reader):
    """Exports the message strings from a message file database.

    Args:
      message_file (MessageFile): message file.
      database_reader (SQLiteAttributeContainerStore): message file
          database reader.
    """
    for extracted_message_table in database_reader.GetAttributeContainers(
        resources.MessageTableDescriptor.CONTAINER_TYPE):
      extracted_message_file_identifier = (
          extracted_message_table.GetMessageFileIdentifier())
      extracted_message_file = (
          database_reader.GetAttributeContainerByIdentifier(
              resources.MessageFileDescriptor.CONTAINER_TYPE,
              extracted_message_file_identifier))

      message_file.AppendMessageTable(
          f'0x{extracted_message_table.language_identifier:08x}',
          extracted_message_file.file_version)

    for extracted_message_string in database_reader.GetAttributeContainers(
        resources.MessageStringDescriptor.CONTAINER_TYPE):
      extracted_message_table_identifier = (
          extracted_message_string.GetMessageTableIdentifier())
      extracted_message_table = (
          database_reader.GetAttributeContainerByIdentifier(
              resources.MessageTableDescriptor.CONTAINER_TYPE,
              extracted_message_table_identifier))

      language_identifier = (
          f'0x{extracted_message_table.language_identifier:08x}')

      message_table = message_file.GetMessageTable(language_identifier)
      message_identifier = extracted_message_string.identifier
      extracted_message_text = extracted_message_string.text

      message_string = message_table.message_strings.get(
          message_identifier, None)
      if not message_string:
        message_table.message_strings[message_identifier] = (
            extracted_message_text)

      elif message_string != extracted_message_text:
        extracted_message_file_identifier = (
            extracted_message_table.GetMessageFileIdentifier())
        extracted_message_file = (
            database_reader.GetAttributeContainerByIdentifier(
                resources.MessageFileDescriptor.CONTAINER_TYPE,
                extracted_message_file_identifier))

        file_version = extracted_message_file.file_version

        differ = difflib.Differ()
        diff_list = list(differ.compare(
            [message_string], [extracted_message_text]))
        diff_list = '\n'.join(diff_list)
        logging.warning((
            f'Found duplicate alternating message string: '
            f'0x{message_identifier:08x} in LCID: {language_identifier:s} and '
            f'version: {file_version:s}.\n{diff_list:s}\n'))

        # TODO: is there a better way to determine which string to use.
        # E.g. latest build version?

  def Export(self, source_path, output_writer):
    """Exports the strings extracted from message files.

    Args:
      source_path (str): source path.
      output_writer (ExporterOutputWriter): output writer.
    """
    event_providers_database_path = os.path.join(
        source_path, self._EVENT_PROVIDERS_DATABASE_FILENAME)

    database_reader = sqlite_store.SQLiteAttributeContainerStore()
    database_reader.Open(path=event_providers_database_path, read_only=True)

    try:
      self._ExportEventLogProviders(database_reader, output_writer)
      self._ExportMessageFiles(source_path, database_reader, output_writer)

    finally:
      database_reader.Close()

    self._ExportMessageFilesPerEventLogProvider(output_writer)

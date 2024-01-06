# -*- coding: utf-8 -*-
"""Windows Event Log message resource exporter."""

import difflib
import logging
import os

from acstore import sqlite_store

from winevtrc import resources
from winevtrc import storage  # pylint: disable=unused-import


class Exporter(object):
  """Exports the strings extracted from Windows EventLog message files."""

  _EVENT_PROVIDERS_DATABASE_FILENAME = 'winevt-kb.db'

  def __init__(self):
    """Initializes a Windows Event Log message resource exporter."""
    super(Exporter, self).__init__()
    self._event_log_providers = {}

  def _ExportEventLogProviders(self, database_reader, output_writer):
    """Exports the event log provides from an event provider database.

    Args:
      database_reader (SQLiteAttributeContainerStore): event provider database
          reader.
      output_writer (OutputWriter): output writer.
    """
    for event_log_provider in database_reader.GetAttributeContainers(
        resources.EventLogProvider.CONTAINER_TYPE):
      log_source = event_log_provider.log_source
      display_name = event_log_provider.name or event_log_provider.log_source
      existing_event_log_provider = self._event_log_providers.get(
          log_source, None)
      if existing_event_log_provider:
        # TODO: merge event providers on mismatch?

        existing_identifier = existing_event_log_provider.identifier
        if event_log_provider.identifier and (
           event_log_provider.identifier != existing_identifier):
          logging.warning((
              f'Found duplicate alternating event log provider: '
              f'{display_name:s}. GUID mismatch'))
          continue

        message_files = existing_event_log_provider.category_message_files
        if event_log_provider.category_message_files and (
           event_log_provider.category_message_files != message_files):
          logging.warning((
              f'Found duplicate alternating event log provider: '
              f'{display_name:s}. Category message files mismatch'))
          continue

        message_files = existing_event_log_provider.event_message_files
        if event_log_provider.event_message_files and (
           event_log_provider.event_message_files != message_files):
          logging.warning((
              f'Found duplicate alternating event log provider: '
              f'{display_name:s}. Event message files mismatch'))
          continue

        message_files = existing_event_log_provider.parameter_message_files
        if event_log_provider.parameter_message_files and (
           event_log_provider.parameter_message_files != message_files):
          logging.warning((
              f'Found duplicate alternating event log provider: '
              f'{display_name:s}. Parameter message files mismatch'))
          continue

      self._event_log_providers[log_source] = event_log_provider
      output_writer.WriteEventLogProvider(event_log_provider)

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
      output_writer (OutputWriter): output writer.
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

      for message_table in message_file.GetMessageTables():
          # TODO: track the languages.
        output_writer.WriteMessageTable(message_file, message_table)

  def _ExportMessageFilesPerEventLogProvider(self, output_writer):
    """Exports the message files used by an Event Log provider.

    Args:
      output_writer (OutputWriter): output writer.
    """
    for event_log_provider in self._event_log_providers.values():
      for message_filename in event_log_provider.event_message_files:
        normalized_path = self._GetNormalizedPath(message_filename)
        output_writer.WriteMessageFilesPerEventLogProvider(
            event_log_provider, normalized_path)

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

  def Export(self, source_path, output_writer):
    """Exports the strings extracted from message files.

    Args:
      source_path (str): source path.
      output_writer (OutputWriter): output writer.
    """
    event_providers_database_path = os.path.join(
        source_path, self._EVENT_PROVIDERS_DATABASE_FILENAME)

    database_reader = sqlite_store.SQLiteAttributeContainerStore()
    database_reader.Open(path=event_providers_database_path, read_only=True)

    self._ExportEventLogProviders(database_reader, output_writer)

    self._ExportMessageFiles(
        source_path, database_reader, output_writer)

    # TODO: export parameter and category files.

    self._ExportMessageFilesPerEventLogProvider(output_writer)

    database_reader.Close()

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


class MessageFileAttributeContainerStore(
    sqlite_store.SQLiteAttributeContainerStore):
  """Message file attribute container store.

  Attributes:
    format_version (int): storage format version.
    name (str): name of the the message database.
    serialization_format (str): serialization format.
    windows_path (str): Windows path.
  """

  def __init__(self, attribute_container):
    """Initializes a message file attribute container store.

    Args:
      attribute_container (WinevtResourcesMessageFileDatabase): message file
          database attribute container..
    """
    super(MessageFileAttributeContainerStore, self).__init__()
    # Strip ".db" from the database filename.
    self.name = attribute_container.database_filename[:-3]
    self.windows_path = attribute_container.windows_path



class ExporterOutputWriter(object):
  """Exporter output writer."""

  def _DiffMessageString(
      self, file_version, language_identifier, message_identifier,
      message_string, other_message_string):
    """Determines differences in 2 message strings.

    Args:
      file_version (str): file version.
      language_identifier (int): language identifier.
      message_identifier (int): message identifier.
      message_string (list[str]): message string.
      other_message_string (list[str]): other message string.
    """
    color_green = '\x1b[0;32m'
    color_red = '\x1b[0;31m'
    color_end = '\x1b[0m'

    matcher = difflib.SequenceMatcher(
       None, message_string, other_message_string)

    opcodes = list(matcher.get_opcodes())
    if opcodes:
      logging.warning((
          f'Found duplicate alternating message string: '
          f'0x{message_identifier:08x} in LCID: 0x{language_identifier:08x} '
          f'and version: {file_version:s}.'))

    for opcode, first_start, first_end, second_start, second_end in opcodes:
      first_lines = message_string[first_start:first_end]
      second_lines = other_message_string[second_start:second_end]

      if opcode == 'insert':
        for line in second_lines:
          print(f'{color_green:s}+ {line:s}{color_end:s}')

      elif opcode == 'delete':
        for line in first_lines:
          print(f'{color_red:s}- {line:s}{color_end:s}')

      elif opcode == 'replace':
        for index in range(len(first_lines)):  # pylint: disable=consider-using-enumerate
          first_line = first_lines[index]
          second_line = second_lines[index]

          first_output = []
          second_output = []

          line_matcher = difflib.SequenceMatcher(
              None, first_line, second_line, autojunk=False)
          for line_opcode, a0, a1, b0, b1 in line_matcher.get_opcodes():
            if line_opcode == 'equal':
              text = first_line[a0:a1]
              first_output.append(text)
              second_output.append(text)

            elif opcode == 'insert':
              text = second_line[b0:b1]
              second_output.append(f'{color_green:s}{text:s}{color_end:s}')

            elif opcode == 'delete':
              text = first_line[a0:a1]
              first_output.append(f'{color_red:s}{text:s}{color_end:s}')

            elif opcode == 'replace':
              text = second_line[b0:b1]
              second_output.append(f'{color_green:s}{text:s}{color_end:s}')
              text = first_line[a0:a1]
              first_output.append(f'{color_red:s}{text:s}{color_end:s}')

          first_output = ''.join(first_output)
          second_output = ''.join(second_output)

          print(f'+ {second_output:s}')
          print(f'- {first_output:s}')

  @abc.abstractmethod
  def Close(self):
    """Closes the output writer."""

  def GetMessageTables(self, message_file):
    """Retrieves message tables.

    Args:
      message_file (MessageFileAttributeContainerStore): message file.

    Yields:
      MessageTable: message table.
    """
    extracted_message_tables_per_file_versions = {}

    for extracted_message_table in message_file.GetAttributeContainers(
        resources.MessageTableDescriptor.CONTAINER_TYPE):
      extracted_message_file_identifier = (
          extracted_message_table.GetMessageFileIdentifier())
      extracted_message_file = (
          message_file.GetAttributeContainerByIdentifier(
              resources.WinevtResourcesMessageFile.CONTAINER_TYPE,
              extracted_message_file_identifier))

      # pylint: disable=consider-using-generator
      file_version_tuple = tuple([
          int(number, 10)
          for number in extracted_message_file.file_version.split('.')])
      extracted_message_tables_per_file_versions[file_version_tuple] = (
          extracted_message_table)

    message_tables = []
    for file_version_tuple, extracted_message_table in sorted(
        extracted_message_tables_per_file_versions.items()):
      file_version = '.'.join([f'{number:d}' for number in file_version_tuple])

      message_table = resources.MessageTable(
          extracted_message_table.language_identifier)
      message_table.file_versions.append(file_version)

      table_identifier = extracted_message_table.GetIdentifier()
      identifier_string = table_identifier.CopyToString()
      filter_expression = f'_message_table_identifier=="{identifier_string:s}"'

      for extracted_message_string in (
          message_file.GetAttributeContainers(
              resources.WinevtResourcesMessageString.CONTAINER_TYPE,
              filter_expression=filter_expression)):
        message_table.message_strings[
            extracted_message_string.message_identifier] = (
                extracted_message_string.text)

      message_tables.append((file_version, message_table))

    file_version, message_table = message_tables[0]
    language_identifier = message_table.language_identifier

    # TODO: handle multiple language identifiers.
    export_message_tables = [message_table]
    for other_file_version, other_message_table in message_tables[1:]:
      if message_table.message_strings == other_message_table.message_strings:
        message_table.file_versions.append(other_file_version)
      else:
        message_identifiers = set(message_table.message_strings.keys())
        message_identifiers.update(set(
            other_message_table.message_strings.keys()))
        for message_identifier in message_identifiers:
          message_string = message_table.message_strings.get(
              message_identifier, None)
          other_message_string = other_message_table.message_strings.get(
              message_identifier, None)

          if not message_string:
            logging.warning((
                f'Message string: 0x{message_identifier:08x} was added in '
                f'LCID: 0x{language_identifier:08x} and version: '
                f'{other_file_version:s}.'))

          elif not other_message_string:
            logging.warning((
                f'Message string: 0x{message_identifier:08x} was removed in '
                f'LCID: 0x{language_identifier:08x} and version: '
                f'{other_file_version:s}.'))

          elif message_string != other_message_string:
            self._DiffMessageString(
                file_version, message_table.language_identifier,
                message_identifier, [message_string], [other_message_string])

        file_version = other_file_version
        message_table = other_message_table

        export_message_tables.append(message_table)

    yield from export_message_tables

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
      message_file (MessageFileAttributeContainerStore): message file.
    """


class Exporter(object):
  """Exports the strings extracted from Windows EventLog message files."""

  _EVENT_PROVIDERS_DATABASE_FILENAME = 'winevt-kb.db'

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

    category_message_files = {
        message_file.lower()
        for message_file in event_log_provider.category_message_files}
    message_files = {
        message_file.lower()
        for message_file in other_event_log_provider.category_message_files}
    if category_message_files and category_message_files != message_files:
      return False

    event_message_files = {
        message_file.lower()
        for message_file in event_log_provider.event_message_files}
    message_files = {
        message_file.lower()
        for message_file in other_event_log_provider.event_message_files}
    if event_message_files and event_message_files != message_files:
      return False

    parameter_message_files = {
        message_file.lower()
        for message_file in event_log_provider.parameter_message_files}
    message_files = {
        message_file.lower()
        for message_file in other_event_log_provider.parameter_message_files}
    if parameter_message_files and parameter_message_files != message_files:
      return False

    return True

  def _ExportEventLogProviders(self, database_reader, output_writer):
    """Exports the Event Log providers from an Event Log provider database.

    Args:
      database_reader (SQLiteAttributeContainerStore): Event Log provider
          attribute container store.
      output_writer (ExporterOutputWriter): output writer.
    """
    providers_per_log_source = {}

    for event_log_provider in database_reader.GetAttributeContainers(
        resources.WinevtResourcesEventLogProvider.CONTAINER_TYPE):
      name = event_log_provider.name
      if not name:
        log_sources = sorted(event_log_provider.log_sources)
        name = log_sources[0]

      is_equivalent = False

      export_event_log_provider = providers_per_log_source.get(name, None)
      if not export_event_log_provider:
        export_event_log_provider = ExportEventLogProvider(name)

        providers_per_log_source[name] = export_event_log_provider

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

    for export_event_log_provider in sorted(
        providers_per_log_source.values(),
        key=lambda export_event_log_provider: export_event_log_provider.name):
      output_writer.WriteEventLogProvider(export_event_log_provider)

  def _ExportMessageResourceFiles(
      self, source_path, database_reader, output_writer):
    """Exports the message files from an Event Log provider database.

    Args:
      source_path (str): source path.
      database_reader (SQLiteAttributeContainerStore): Event Log provider
          attribute container store.
      output_writer (ExporterOutputWriter): output writer.
    """
    for attribute_container in database_reader.GetAttributeContainers(
        resources.WinevtResourcesMessageFileDatabase.CONTAINER_TYPE):
      message_file_database_path = os.path.join(
          source_path, attribute_container.database_filename)
      if not os.path.exists(message_file_database_path):
        logging.warning((
            f'Missing message file database: '
            f'{attribute_container.database_filename:s}.'))
        continue

      logging.info(f'Processing: {attribute_container.database_filename:s}')

      message_file = MessageFileAttributeContainerStore(attribute_container)
      message_file.Open(message_file_database_path)

      try:
        output_writer.WriteMessageFile(message_file)
      finally:
        message_file.Close()

  def Export(self, source_path, output_writer):
    """Exports message resources.

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
      self._ExportMessageResourceFiles(
          source_path, database_reader, output_writer)

    finally:
      database_reader.Close()

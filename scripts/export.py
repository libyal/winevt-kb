#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Script to export strings extracted from message files."""

from __future__ import print_function
import argparse
import difflib
import logging
import os
import re
import sys

from winevtrc import database
from winevtrc import resources


class Exporter(object):
  """Class that exports the strings extracted from message files."""

  EVENT_PROVIDERS_DATABASE_FILENAME = u'winevt-kb.db'

  def __init__(self):
    """Initializes the exporter object."""
    super(Exporter, self).__init__()
    self._event_log_providers = {}

  def _ExportEventLogProviders(self, database_reader, output_writer):
    """Exports the event log provides from an event provider database.

    Args:
      database_reader (EventProvidersSqlite3DatabaseReader): event provider
          database reader.
      output_writer (OutputWriter): output writer.
    """
    for event_log_provider in database_reader.GetEventLogProviders():
      log_source = event_log_provider.log_source
      existing_event_log_provider = self._event_log_providers.get(
          log_source, None)
      if existing_event_log_provider:
        # TODO: merge event providers on mismatch?

        provider_guid = existing_event_log_provider.provider_guid
        if event_log_provider.provider_guid != provider_guid:
          if event_log_provider.provider_guid:
            logging.warning((
                u'Found duplicate alternating event log provider: {0:s}. '
                u'GUID mismatch').format(log_source))
          continue

        message_files = existing_event_log_provider.category_message_files
        if event_log_provider.category_message_files != message_files:
          if event_log_provider.category_message_files:
            logging.warning((
                u'Found duplicate alternating event log provider: {0:s}. '
                u'Category message files mismatch').format(log_source))
          continue

        message_files = existing_event_log_provider.event_message_files
        if event_log_provider.event_message_files != message_files:
          if event_log_provider.event_message_files:
            logging.warning((
                u'Found duplicate alternating event log provider: {0:s}. '
                u'Event message files mismatch').format(log_source))
          continue

        message_files = existing_event_log_provider.parameter_message_files
        if event_log_provider.parameter_message_files != message_files:
          if event_log_provider.parameter_message_files:
            logging.warning((
                u'Found duplicate alternating event log provider: {0:s}. '
                u'Parameter message files mismatch').format(log_source))
          continue

      self._event_log_providers[log_source] = event_log_provider
      output_writer.WriteEventLogProvider(event_log_provider)

  def _ExportMessageFile(self, message_file, message_file_database_path):
    """Exports a message file.

    Args:
      message_file (MessageFile): message file.
      message_file_database_path (str): path of the message file database.
    """
    database_reader = database.MessageFileSqlite3DatabaseReader()
    database_reader.Open(message_file_database_path)

    self._ExportMessageStrings(message_file, database_reader)
    # TODO: implement has table check.
    # self._ExportStrings(message_file, database_reader)

    database_reader.Close()

  def _ExportMessageFiles(
      self, source_path, database_reader, output_writer):
    """Exports the message files from an event provider database.

    Args:
      source_path (str): source path.
      database_reader (EventProvidersSqlite3DatabaseReader): event provider
          database reader.
      output_writer (OutputWriter): output writer.
    """
    for windows_path, database_filename in database_reader.GetMessageFiles():
      message_file_database_path = os.path.join(source_path, database_filename)
      if not os.path.exists(message_file_database_path):
        logging.warning(
            u'Missing message file database: {0:s}.'.format(database_filename))
        continue

      logging.info(u'Processing: {0:s}'.format(database_filename))

      message_file = resources.MessageFile(database_filename[:-3])
      message_file.windows_path = windows_path

      self._ExportMessageFile(message_file, message_file_database_path)

      output_writer.WriteMessageFile(message_file)

  def _ExportMessageFilesPerEventLogProvider(self, output_writer):
    """Exports the message files used by an Event Log provider.

    Args:
      output_writer (OutputWriter): output writer.
    """
    for event_log_provider in self._event_log_providers.itervalues():
      for message_filename in event_log_provider.event_message_files:
        output_writer.WriteMessageFilesPerEventLogProvider(
            event_log_provider, message_filename)

  def _ExportMessageStrings(self, message_file, database_reader):
    """Exports the message strings from a message file database.

    Args:
      message_file (MessageFile): message file.
      database_reader (MessageFileSqlite3DatabaseReader): message file
          database reader.
    """
    for lcid, file_version in database_reader.GetMessageTables():
      message_file.AppendMessageTable(lcid, file_version)

    for message_table in message_file.GetMessageTables():
      for file_version in message_table.file_versions:
        for message_identifier, message_string in database_reader.GetMessages(
            message_table.lcid, file_version):
          stored_message_string = message_table.message_strings.get(
              message_identifier, None)

          if not stored_message_string:
            message_table.message_strings[message_identifier] = message_string

          elif message_string != stored_message_string:
            differ = difflib.Differ()
            diff_list = list(differ.compare(
                [stored_message_string], [message_string]))
            logging.warning((
                u'Found duplicate alternating message string: {0:s} '
                u'in LCID: {1:s} and version: {2:s}.\n{3:s}\n').format(
                    message_identifier, message_table.lcid, file_version,
                    u'\n'.join(diff_list)))

            # TODO: is there a better way to determine which string to use.
            # E.g. latest build version?

  def _ExportStrings(self, message_file, database_reader):
    """Exports the strings in a message file database.

    Args:
      message_file (MessageFile): message file.
      database_reader (MessageFileSqlite3DatabaseReader): message file
          database reader.
    """
    for lcid, file_version in database_reader.GetStringTables():
      message_file.AppendStringTable(lcid, file_version)

    for string_table in message_file.GetStringTables():
      for file_version in string_table.file_versions:
        for string_identifier, string in database_reader.GetStrings(
            string_table.lcid, file_version):
          stored_string = string_table.strings.get(string_identifier, None)

          if not stored_string:
            string_table.strings[string_identifier] = string

          elif string != stored_string:
            logging.warning((
                u'Found duplicate alternating string: {0:s} in LCID: {1:s} '
                u'and version: {2:s}.\nPrevious: {3:s}\nNew:{4:s}\n').format(
                    string_identifier, string_table.lcid, file_version,
                    stored_string, string))

            # TODO: is there a better way to determine which string to use.
            # E.g. latest build version?

  def Export(self, source_path, output_writer):
    """Exports the strings extracted from message files.

    Args:
      source_path (str): source path.
      output_writer (OutputWriter): output writer.
    """
    database_reader = database.EventProvidersSqlite3DatabaseReader()
    database_reader.Open(os.path.join(
        source_path, self.EVENT_PROVIDERS_DATABASE_FILENAME))

    self._ExportEventLogProviders(database_reader, output_writer)

    self._ExportMessageFiles(
        source_path, database_reader, output_writer)

    # TODO: export parameter and category files.

    self._ExportMessageFilesPerEventLogProvider(output_writer)

    database_reader.Close()


class Sqlite3OutputWriter(object):
  """Class that defines a sqlite3 output writer."""

  def __init__(self, database_path, string_format=u'wrc'):
    """Initializes an output writer object.

    Args:
      database_path (str): path to the database file.
      string_format (Optional[str]): string format.
    """
    super(Sqlite3OutputWriter, self).__init__()
    self._database_path = database_path
    self._database_writer = None
    self._string_format = string_format

  def _WriteMetadata(self):
    """Writes the metadata."""
    self._database_writer.WriteMetadataAttribute(
        u'version', u'20150315')
    self._database_writer.WriteMetadataAttribute(
        u'string_format', self._string_format)

  def Close(self):
    """Closes the output writer object."""
    self._database_writer.Close()
    self._database_writer = None

  def Open(self):
    """Opens the output writer object.

    Returns:
      bool: True if successful or False if not.
    """
    if os.path.isdir(self._database_path):
      return False

    self._database_writer = database.ResourcesSqlite3DatabaseWriter(
        string_format=self._string_format)
    self._database_writer.Open(self._database_path)
    self._WriteMetadata()

    return True

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
    """
    # TODO: check if already exists.
    self._database_writer.WriteEventLogProvider(event_log_provider)

  def WriteMessageFile(self, message_file):
    """Writes the Windows Message Resource file.

    Args:
      message_file (MessageFile): message file.
    """
    self._database_writer.WriteMessageFile(message_file)

  def WriteMessageFilesPerEventLogProvider(
      self, event_log_provider, message_file):
    """Writes the Windows Message Resource file per Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
      message_file (MessageFile): message file.
    """
    self._database_writer.WriteMessageFilesPerEventLogProvider(
        event_log_provider, message_file, database.MESSAGE_FILE_TYPE_EVENT)


class StdoutOutputWriter(object):
  """Class that defines a stdout output writer."""

  def _WriteMessageTable(self, message_table):
    """Writes the message table.

    Args:
      message_table (MessageTable): message table.
    """
    print(u'{0:s} (LCID: {1:s})'.format(
        message_table.language, message_table.lcid))
    print(u'')
    print(u'Message identifier\tMessage string')

    for identifier, string in message_table.message_strings.iteritems():
      string = re.sub(r'\n', u'\\\\n', string)
      string = re.sub(r'\r', u'\\\\r', string)
      string = re.sub(r'\t', u'\\\\t', string)

      ouput_string = u'{0:s}\t{1:s}'.format(identifier, string)

      print(ouput_string.encode(u'utf8'))

    print(u'')

  def Open(self):
    """Opens the file.

    Returns:
      bool: True if successful or False if not.
    """
    return True

  def Close(self):
    """Closes the file."""

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
    """
    print(u'Log type:\t{0:s}'.format(event_log_provider.log_type))
    print(u'Log source:\t{0:s}'.format(event_log_provider.log_source))

    # TODO: print more details.

  def WriteMessageFile(self, message_file):
    """Writes the Windows Message Resource file.

    Args:
      message_file (MessageFile): message file.
    """
    print(u'{0:s}'.format(message_file.name))
    print(u'Path:\t{0:s}'.format(message_file.windows_path))

    for message_table in message_file.GetMessageTables():
      self._WriteMessageTable(message_table)

  def WriteMessageFilesPerEventLogProvider(
      self, event_log_provider, message_file):
    """Writes the Windows Message Resource file per Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
      message_file (MessageFile): message file.
    """
    pass


class AsciidocFileWriter(object):
  """Class to represent an asciidoc file writer."""
  # TODO: aparantly the filename should only contain 1 dot and
  # end with .asciidoc

  def __init__(self):
    """Initializes the asciidoc file writer object."""
    super(AsciidocFileWriter, self).__init__()
    self._file = None

  def Open(self, filename):
    """Opens the file.

    Args:
      filename (str): name of the file.

    Returns:
      bool: True if successful or False if not.
    """
    # Using binary mode to make sure to write Unix end of lines.
    self._file = open(filename, 'wb')
    return True

  def Close(self):
    """Closes the file."""
    self._file.close()

  def WriteLine(self, line):
    """Writes a line."""
    self._file.write(u'{0:s}\n'.format(line).encode(u'utf8'))

  def WriteLines(self, lines):
    """Writes lines."""
    for line in lines:
      self.WriteLine(line)


class AsciidocOutputWriter(object):
  """Class that defines an asciidoc output writer."""

  def __init__(self, path):
    """Initializes the asciidoc output writer object.

    Args:
      path (str): path to the directory containing the asciidoc files.
    """
    super(AsciidocOutputWriter, self).__init__()
    self._path = path

  def _WriteMessageTable(self, message_table, file_writer):
    """Writes the message table.

    Args:
      message_table (MessageTable): message table.
      file_writer (AsciidocFileWriter): file writer.
    """
    file_writer.WriteLines([
        u'=== {0:s} (LCID: {1:s})'.format(
            message_table.language, message_table.lcid),
        u'',
        u'[cols="1,5",options="header"]',
        u'|===',
        u'| Message identifier | Message string'])

    for identifier, string in message_table.message_strings.iteritems():
      string = re.sub(r'\n', u'\\\\n', string)
      string = re.sub(r'\r', u'\\\\r', string)
      string = re.sub(r'\t', u'\\\\t', string)

      ouput_string = u'| {0:s} | {1:s}'.format(identifier, string)

      file_writer.WriteLine(ouput_string.encode(u'utf8'))

    file_writer.WriteLines([
        u'|===',
        u''])

  def Close(self):
    """Closes the output writer object."""
    pass

  def Open(self):
    """Opens the output writer object.

    Returns:
      bool: True if successful or False if not.
    """
    if not os.path.isdir(self._path):
      return False
    return True

  def WriteEventLogProvider(self, unused_event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
    """
    # TODO: print details.
    return

  def WriteMessageFile(self, message_file):
    """Writes the Windows Message Resource file.

    Args:
      message_file (MessageFile): message file.
    """
    file_writer = AsciidocFileWriter()
    path = os.path.join(
        self._path, u'{0:s}.asciidoc'.format(message_file.name))

    if file_writer.Open(path):

      file_writer.WriteLines([
          u'== {0:s}'.format(message_file.name),
          u'|===',
          u'| Path: | {0:s}'.format(message_file.windows_path),
          u'|===',
          u''])

      for message_table in message_file.GetMessageTables():
        self._WriteMessageTable(message_table, file_writer)

      file_writer.Close()

  def WriteMessageFilesPerEventLogProvider(
      self, event_log_provider, message_file):
    """Writes the Windows Message Resource file per Event Log provider.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
      message_file (MessageFile): message file.
    """
    pass


def Main():
  """The main program function.

  Returns:
    bool: True if successful or False if not.
  """
  argument_parser = argparse.ArgumentParser(description=(
      u'Export strings extracted from message files.'))

  argument_parser.add_argument(
      u'source', nargs=u'?', action=u'store', metavar=u'./winevt-db/',
      default=None, help=(
          u'directory that contains the sqlite3 with the extracted strings.'))

  argument_parser.add_argument(
      u'--db', u'--database', dest=u'database', action=u'store',
      metavar=u'winevt-rc.db', default=None, help=(
          u'filename of the sqlite3 database to write to.'))

  argument_parser.add_argument(
      u'--string_format', u'--string-format', dest=u'string_format',
      action=u'store', metavar=u'FORMAT', default=u'wrc',
      choices=[u'pep3101', u'wrc'], help=u'the message string format.')

  argument_parser.add_argument(
      u'--wiki', dest=u'wiki', action=u'store', metavar=u'./winevt-kb.wiki/',
      default=None, help=u'path to write the wiki pages to.')

  # TODO: allow to set preferred language.

  options = argument_parser.parse_args()

  if not options.source:
    print(u'Source value is missing.')
    print(u'')
    argument_parser.print_help()
    print(u'')
    return False

  if not os.path.isdir(options.source):
    print(u'Invalid source.')
    print(u'')
    return False

  logging.basicConfig(
      level=logging.INFO, format=u'[%(levelname)s] %(message)s')

  if options.database:
    output_writer = Sqlite3OutputWriter(
        options.database, string_format=options.string_format)
  elif options.wiki:
    output_writer = AsciidocOutputWriter(options.wiki)
  else:
    output_writer = StdoutOutputWriter()

  if not output_writer.Open():
    print(u'Unable to open output writer.')
    print(u'')
    return False

  exporter = Exporter()
  exporter.Export(options.source, output_writer)
  output_writer.Close()

  return True


if __name__ == '__main__':
  if not Main():
    sys.exit(1)
  else:
    sys.exit(0)

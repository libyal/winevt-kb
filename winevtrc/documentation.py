# -*- coding: utf-8 -*-
"""Documentation writers."""

import re

from winevtrc import versions


class DocumentationFileWriter(object):
  """Documentation file writer."""

  def __init__(self, path):
    """Initializes a documentation file writer."""
    super(DocumentationFileWriter, self).__init__()
    self._file_object = None
    self._path = path

  def __enter__(self):
    """Make this work with the 'with' statement."""
    self.Open()
    return self

  def __exit__(self, exception_type, value, traceback):
    """Make this work with the 'with' statement."""
    self.Close()

  def _WriteHeader(self):
    """Writes a header."""
    return

  def Close(self):
    """Closes the documentation file writer object."""
    self._file_object.close()
    self._file_object = None

  def Open(self):
    """Opens the documentation file writer object."""
    # pylint: disable=consider-using-with
    self._file_object = open(self._path, 'w', encoding='utf-8')
    self._WriteHeader()


class EventLogProviderMarkdownWriter(DocumentationFileWriter):
  """Event Log provider Markdown file writer."""

  _WINDOWS_VERSIONS_KEY_FUNCTION = versions.WindowsVersions.KeyFunction

  def WriteEventLogProvider(self, event_log_provider, windows_versions):
    """Writes an Event Log provider to a Markdown file.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
      windows_versions (list[str]): strings that identify the Windows
          versions.
    """
    name = event_log_provider.name
    if not name:
      log_sources = sorted(event_log_provider.log_sources)
      name = log_sources[0]

    lines = []
    if self._file_object.tell() == 0:
      lines = [
          f'## {name:s}',
          '']

    if windows_versions:
      # TODO: combine Windows versions into a more compact string
      versions_per_prefix = {}
      for version in sorted(windows_versions):
        for prefix in ('Windows 10', 'Windows 11', None):
          if prefix and version.startswith(prefix):
            break

        if not prefix:
          versions_per_prefix[version] = []
        else:
          if prefix not in versions_per_prefix:
            versions_per_prefix[prefix] = []
          versions_per_prefix[prefix].append(version[len(prefix) + 2:-1])

      lines.append('Seen on:')

      for prefix, sub_versions in sorted(
          versions_per_prefix.items(),
          key=lambda item: self._WINDOWS_VERSIONS_KEY_FUNCTION(item[0])):
        if not sub_versions:
          line = f'* {prefix:s}'
        else:
          sub_versions_string = ', '.join(sub_versions)
          line = f'* {prefix:s} ({sub_versions_string:s})'

        lines.append(line)

      lines.append('')

    lines.extend([
        '<table border="1" class="docutils">',
        '  <tbody>'])

    if event_log_provider.name:
      lines.extend([
          '    <tr>',
          '      <td><b>Name:</b></td>',
          f'      <td>{event_log_provider.name:s}</td>',
          '    </tr>'])

    if event_log_provider.identifier:
      lines.extend([
          '    <tr>',
          '      <td><b>Identifier:</b></td>',
          f'      <td>{event_log_provider.identifier:s}</td>',
          '    </tr>'])

    if event_log_provider.additional_identifier:
      lines.extend([
          '    <tr>',
          '      <td><b>Additional identifier:</b></td>',
          f'      <td>{event_log_provider.additional_identifier:s}</td>',
          '    </tr>'])

    for index, log_type in enumerate(event_log_provider.log_types):
      if index == 0:
        lines.extend([
          '    <tr>',
          '      <td><b>Log type(s):</b></td>',
          f'      <td>{log_type:s}</td>',
          '    </tr>'])
      else:
        lines.extend([
          '    <tr>',
          '      <td>&nbsp;</td>',
          f'      <td>{log_type:s}</td>',
          '    </tr>'])

    for index, log_source in enumerate(event_log_provider.log_sources):
      if index == 0:
        lines.extend([
          '    <tr>',
          '      <td><b>Log source(s):</b></td>',
          f'      <td>{log_source:s}</td>',
          '    </tr>'])
      else:
        lines.extend([
          '    <tr>',
          '      <td>&nbsp;</td>',
          f'      <td>{log_source:s}</td>',
          '    </tr>'])

    for index, path in enumerate(sorted((
        event_log_provider.category_message_files))):
      if index == 0:
        lines.extend([
          '    <tr>',
          '      <td><b>Category message file(s):</b></td>',
          f'      <td>{path:s}</td>',
          '    </tr>'])
      else:
        lines.extend([
          '    <tr>',
          '      <td>&nbsp;</td>',
          f'      <td>{path:s}</td>',
          '    </tr>'])

    for index, path in enumerate(sorted((
        event_log_provider.event_message_files))):
      if index == 0:
        lines.extend([
          '    <tr>',
          '      <td><b>Event message file(s):</b></td>',
          f'      <td>{path:s}</td>',
          '    </tr>'])
      else:
        lines.extend([
          '    <tr>',
          '      <td>&nbsp;</td>',
          f'      <td>{path:s}</td>',
          '    </tr>'])

    for index, path in enumerate(sorted((
        event_log_provider.parameter_message_files))):
      if index == 0:
        lines.extend([
          '    <tr>',
          '      <td><b>Parameter message file(s):</b></td>',
          f'      <td>{path:s}</td>',
          '    </tr>'])
      else:
        lines.extend([
          '    <tr>',
          '      <td>&nbsp;</td>',
          f'      <td>{path:s}</td>',
          '    </tr>'])

    lines.extend([
        '  </tbody>',
        '</table>',
        '',
        '&nbsp;',
        '',
        ''])

    text = '\n'.join(lines)
    self._file_object.write(text)


class EventLogProvidersIndexRstWriter(DocumentationFileWriter):
  """Event Log providers index.rst file writer."""

  _HEADER_TEXT = '\n'.join([
      '###################',
      'Event Log providers',
      '###################',
      '',
      '.. toctree::',
      '   :maxdepth: 1',
      '',
      ''])

  def _WriteHeader(self):
    """Writes a header."""
    self._file_object.write(self._HEADER_TEXT)

  def WriteEventLogProvider(self, name):
    """Writes an Event Log provider to the index.rst file.

    Args:
      name (str): name of the Event Log provider.
    """
    output_filename = f'Provider-{name:s}'.replace(' ', '-').replace('/', '-')
    self._file_object.write(f'   {name:s} <{output_filename:s}>\n')


class MessageFileMarkdownWriter(DocumentationFileWriter):
  """Message file Markdown file writer."""

  def _WriteMessageTable(self, message_table):
    """Writes a message table.

    Args:
      message_table (MessageTable): message table.
    """
    file_versions = ', '.join(message_table.file_versions)
    lines = [
        '',
        f'### {file_versions:s}',
        '',
        'Message identifier | Message string',
        '--- | ---']

    for identifier, string in message_table.message_strings.items():
      string = re.sub(r'\n', '\\\\n', string)
      string = re.sub(r'\r', '\\\\r', string)
      string = re.sub(r'\t', '\\\\t', string)

      lines.append(f'0x{identifier:08x} | {string:s}')

    lines.append('')

    text = '\n'.join(lines)
    self._file_object.write(text)

  def WriteMessageFile(self, message_file):
    """Writes a message file.

    Args:
      message_file (ExportMessageFile): message file.
    """
    lines = [
        f'## {message_file.name:s}',
        '',
        f'Path: {message_file.windows_path:s}',
        '']

    text = '\n'.join(lines)
    self._file_object.write(text)

    for message_table in message_file.GetMessageTables():
      self._WriteMessageTable(message_table)


class MessageFilesIndexRstWriter(DocumentationFileWriter):
  """Message files index.rst file writer."""

  _HEADER_TEXT = '\n'.join([
      '#############',
      'Message files',
      '#############',
      '',
      '.. toctree::',
      '   :maxdepth: 1',
      '',
      ''])

  def _WriteHeader(self):
    """Writes a header."""
    self._file_object.write(self._HEADER_TEXT)

  def WriteMessageFile(self, name):
    """Writes a message file to the index.rst file.

    Args:
      name (str): name of the message file.
    """
    output_filename = f'MessageFile-{name:s}'.replace(
        ' ', '-').replace('/', '-')
    self._file_object.write(f'   {name:s} <{output_filename:s}>\n')

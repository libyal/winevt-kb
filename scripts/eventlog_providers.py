#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script to extract Windows Event Log providers from the Windows Registry."""

import argparse
import logging
import os
import sys
import yaml

from dfvfs.helpers import command_line as dfvfs_command_line
from dfvfs.helpers import volume_scanner as dfvfs_volume_scanner
from dfvfs.lib import errors as dfvfs_errors

from winevtrc import extractor


class IndexRstOutputWriter(object):
  """Index.rst output writer."""

  def __init__(self, path):
    """Initializes a Markdown output writer."""
    super(IndexRstOutputWriter, self).__init__()
    self._file_object = None
    self._path = path

  def __enter__(self):
    """Make this work with the 'with' statement."""
    self._file_object = open(self._path, 'w', encoding='utf-8')

    text = '\n'.join([
        '###################',
        'Event Log providers',
        '###################',
        '',
        '.. toctree::',
        '   :maxdepth: 1',
        '',
        ''])
    self._file_object.write(text)

    return self

  def __exit__(self, exception_type, value, traceback):
    """Make this work with the 'with' statement."""
    self._file_object.close()
    self._file_object = None

  def WriteEventLogProvider(self, log_source):
    """Writes a Event Log provider to the output.

    Args:
      log_source (str): log source.
    """
    output_filename = 'Provider-{0:s}'.format(log_source)
    output_filename = output_filename.replace(' ', '-').replace('/', '-')

    text = '   {0:s} <{1:s}>\n'.format(log_source, output_filename)
    self._file_object.write(text)


class MarkdownOutputWriter(object):
  """Markdown output writer."""

  def __init__(self, path):
    """Initializes a Markdown output writer."""
    super(MarkdownOutputWriter, self).__init__()
    self._file_object = None
    self._path = path

  def __enter__(self):
    """Make this work with the 'with' statement."""
    self._file_object = open(self._path, 'w', encoding='utf-8')
    return self

  def __exit__(self, exception_type, value, traceback):
    """Make this work with the 'with' statement."""
    self._file_object.close()
    self._file_object = None

  def WriteEventLogProvider(self, event_log_provider, windows_versions):
    """Writes a Event Log provider to the output.

    Args:
      event_log_provider (EventLogProvider): Event Log provider.
      windows_versions (list[str]): strings that identify the Windows
          versions.
    """
    log_sources = sorted(event_log_provider.log_sources)

    lines = []
    if self._file_object.tell() == 0:
      lines.extend([
          '## {0:s}'.format(log_sources[0]),
          ''])

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

      for prefix, versions in versions_per_prefix.items():
        line = '* {0:s}'.format(prefix)
        if versions:
          line = '{0:s} ({1:s})'.format(line, ', '.join(versions))
        lines.append(line)

      lines.append('')

    lines.extend([
        '<table border="1" class="docutils">',
        '  <tbody>'])

    for index, log_source in enumerate(log_sources):
      if index == 0:
        lines.extend([
          '    <tr>',
          '      <td><b>Log source(s):</b></td>',
          '      <td>{0:s}</td>'.format(log_source),
          '    </tr>'])
      else:
        lines.extend([
          '    <tr>',
          '      <td>&nbsp;</td>',
          '      <td>{0:s}</td>'.format(log_source),
          '    </tr>'])

    if event_log_provider.log_type:
      lines.extend([
          '    <tr>',
          '      <td><b>Log type:</b></td>',
          '      <td>{0:s}</td>'.format(event_log_provider.log_type),
          '    </tr>'])

    if event_log_provider.identifier:
      lines.extend([
          '    <tr>',
          '      <td><b>Identifier:</b></td>',
          '      <td>{0:s}</td>'.format(event_log_provider.identifier),
          '    </tr>'])

    if event_log_provider.additional_identifier:
      lines.extend([
          '    <tr>',
          '      <td><b>Additional identifier:</b></td>',
          '      <td>{0:s}</td>'.format(
              event_log_provider.additional_identifier),
          '    </tr>'])

    for index, path in enumerate(sorted((
        event_log_provider.category_message_files))):
      if index == 0:
        lines.extend([
          '    <tr>',
          '      <td><b>Category message file(s):</b></td>',
          '      <td>{0:s}</td>'.format(path),
          '    </tr>'])
      else:
        lines.extend([
          '    <tr>',
          '      <td>&nbsp;</td>',
          '      <td>{0:s}</td>'.format(path),
          '    </tr>'])

    for index, path in enumerate(sorted((
        event_log_provider.event_message_files))):
      if index == 0:
        lines.extend([
          '    <tr>',
          '      <td><b>Event message file(s):</b></td>',
          '      <td>{0:s}</td>'.format(path),
          '    </tr>'])
      else:
        lines.extend([
          '    <tr>',
          '      <td>&nbsp;</td>',
          '      <td>{0:s}</td>'.format(path),
          '    </tr>'])

    for index, path in enumerate(sorted((
        event_log_provider.parameter_message_files))):
      if index == 0:
        lines.extend([
          '    <tr>',
          '      <td><b>Parameter message file(s):</b></td>',
          '      <td>{0:s}</td>'.format(path),
          '    </tr>'])
      else:
        lines.extend([
          '    <tr>',
          '      <td>&nbsp;</td>',
          '      <td>{0:s}</td>'.format(path),
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


def Main():
  """The main program function.

  Returns:
    bool: True if successful or False if not.
  """
  argument_parser = argparse.ArgumentParser(description=(
      'Extracts Windows Event Log providers from the Windows Registry.'))

  argument_parser.add_argument(
      '-d', '--debug', dest='debug', action='store_true', default=False,
      help='enable debug output.')

  argument_parser.add_argument(
      '-w', '--windows_version', '--windows-version',
      dest='windows_version', action='store', metavar='Windows XP',
      default=None, help='string that identifies the Windows version.')

  argument_parser.add_argument(
      'source', nargs='?', action='store', metavar='/mnt/c/',
      default=None, help=(
          'path of the volume containing C:\\Windows or the filename of '
          'a storage media image containing the C:\\Windows directory.'))

  options = argument_parser.parse_args()

  # TODO: support a sources configuration file
  if not options.source:
    print('Source value is missing.')
    print('')
    argument_parser.print_help()
    print('')
    return False

  logging.basicConfig(
      level=logging.INFO, format='[%(levelname)s] %(message)s')

  try:
    with open(options.source, 'r', encoding='utf-8') as file_object:
      source_definitions = list(yaml.safe_load_all(file_object))

  except (SyntaxError, UnicodeDecodeError):
    source_definitions = [{
        'path': options.source, 'windows_version': options.windows_version}]

  mediator = dfvfs_command_line.CLIVolumeScannerMediator()

  volume_scanner_options = dfvfs_volume_scanner.VolumeScannerOptions()
  volume_scanner_options.partitions = ['all']
  volume_scanner_options.snapshots = ['none']
  volume_scanner_options.volumes = ['none']

  event_log_providers_per_version = []
  for source_definition in source_definitions:
    source_path = source_definition['path']
    logging.info('Processing: {0:s}'.format(source_path))

    extractor_object = extractor.EventMessageStringExtractor(
        debug=options.debug, mediator=mediator)

    try:
      result = extractor_object.ScanForWindowsVolume(
          source_path, options=volume_scanner_options)
    except dfvfs_errors.ScannerError:
      result = False

    if not result:
      print(('Unable to retrieve the volume with the Windows directory from: '
             '{0:s}.').format(source_path))
      print('')
      return False

    windows_version = source_definition['windows_version']
    if windows_version:
      extractor_object.windows_version = windows_version
    elif extractor_object.windows_version:
      logging.info('Detected Windows version: {0:s}'.format(
          extractor_object.windows_version))
    else:
      print('Unable to determine Windows version.')

      if options.database:
        print('Output requires a Windows version, specify one with '
              '--windows-version.')
        print('')
        return False

    extractor_object.CollectSystemEnvironmentVariables()

    event_log_providers = {}

    for event_log_provider in extractor_object.CollectEventLogProviders():
      log_sources = sorted(event_log_provider.log_sources)
      first_log_source = log_sources[0]

      # pylint: disable=consider-using-set-comprehension

      event_log_provider.category_message_files = set([
          extractor_object.GetNormalizedMessageFilePath(path).lower()
          for path in event_log_provider.category_message_files])

      event_log_provider.event_message_files = set([
          extractor_object.GetNormalizedMessageFilePath(path).lower()
          for path in event_log_provider.event_message_files])

      event_log_provider.parameter_message_files = set([
          extractor_object.GetNormalizedMessageFilePath(path).lower()
          for path in event_log_provider.parameter_message_files])

      event_log_providers[first_log_source] = event_log_provider

    if event_log_providers:
      event_log_providers_per_version.append(
          (windows_version, event_log_providers))

  results_per_log_source = {
      log_source: [] for log_source in event_log_providers.keys()
      for _, event_log_providers in event_log_providers_per_version}

  for first_log_source, results in sorted(results_per_log_source.items()):
    for windows_version, event_log_providers in event_log_providers_per_version:
      event_log_provider = event_log_providers.get(first_log_source, None)
      if not event_log_provider:
        continue

      is_equivalent = False
      for result_dict in results:
        result_event_log_provider = result_dict['event_log_provider']
        is_equivalent = True

        if event_log_provider.identifier != (
            result_event_log_provider.identifier):
          is_equivalent = False

        elif event_log_provider.category_message_files != (
            result_event_log_provider.category_message_files):
          is_equivalent = False

        elif event_log_provider.event_message_files != (
            result_event_log_provider.event_message_files):
          is_equivalent = False

        elif event_log_provider.parameter_message_files != (
            result_event_log_provider.parameter_message_files):
          is_equivalent = False

        if is_equivalent:
          result_dict['windows_versions'].append(windows_version)
          break

      if not is_equivalent:
        result_event_log_provider = {
            'event_log_provider': event_log_provider,
            'windows_versions': [windows_version]}
        results.append(result_event_log_provider)

  output_directory = os.path.join('docs', 'sources', 'eventlog-providers')
  os.makedirs(output_directory, exist_ok=True)

  index_rst_file_path = os.path.join(output_directory, 'index.rst')
  with IndexRstOutputWriter(index_rst_file_path) as index_rst_writer:
    for first_log_source, results in sorted(results_per_log_source.items()):
      index_rst_writer.WriteEventLogProvider(first_log_source)

      output_filename = 'Provider-{0:s}.md'.format(first_log_source)
      output_filename = output_filename.replace(' ', '-').replace('/', '-')

      markdown_file_path = os.path.join(output_directory, output_filename)
      with MarkdownOutputWriter(markdown_file_path) as markdown_writer:
        for result_dict in results:
          markdown_writer.WriteEventLogProvider(
              result_dict['event_log_provider'],
              result_dict['windows_versions'])

  if not results_per_log_source:
    print('No Windows Event Log providers found.')

  return True


if __name__ == '__main__':
  if not Main():
    sys.exit(1)
  else:
    sys.exit(0)

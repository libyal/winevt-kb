#!/usr/bin/env python3
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

from winevtrc import documentation
from winevtrc import extractor


def CompareEventLogProviders(event_log_provider, other_event_log_provider):
  """Compares 2 Event Log providers to determine if they are equivalent.

  Args:
    event_log_provider (EventLogProvider): Event Log provider.
    other_event_log_provider (EventLogProvider): other Event Log provider.

  Returns:
    bool: True if the Event Log providers are equivalent, False otherwise.
  """
  if event_log_provider.identifier != other_event_log_provider.identifier:
    return False

  message_files = other_event_log_provider.category_message_files
  if event_log_provider.category_message_files != message_files:
    return False

  message_files = other_event_log_provider.event_message_files
  if event_log_provider.event_message_files != message_files:
    return False

  message_files = other_event_log_provider.parameter_message_files
  if event_log_provider.parameter_message_files != message_files:
    return False

  return True


def Main():
  """Entry point of console script to extract Windows Event Log providers.

  Returns:
    int: exit code that is provided to sys.exit().
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

  if not options.source:
    print('Source value is missing.')
    print('')
    argument_parser.print_help()
    print('')
    return 1

  logging.basicConfig(
      level=logging.INFO, format='[%(levelname)s] %(message)s')

  try:
    with open(options.source, 'r', encoding='utf-8') as file_object:
      source_definitions = list(yaml.safe_load_all(file_object))

  except (SyntaxError, UnicodeDecodeError, yaml.parser.ParserError):
    source_definitions = [{
        'source': options.source, 'windows_version': options.windows_version}]

  mediator = dfvfs_command_line.CLIVolumeScannerMediator()

  volume_scanner_options = dfvfs_volume_scanner.VolumeScannerOptions()
  volume_scanner_options.partitions = ['all']
  volume_scanner_options.snapshots = ['none']
  volume_scanner_options.volumes = ['none']

  event_log_providers_per_version = []
  providers_per_log_source = {}

  for source_definition in source_definitions:
    source_path = source_definition['source']
    logging.info(f'Processing: {source_path:s}')

    extractor_object = extractor.EventMessageStringExtractor(
        debug=options.debug, mediator=mediator)

    try:
      result = extractor_object.ScanForWindowsVolume(
          source_path, options=volume_scanner_options)
    except dfvfs_errors.ScannerError:
      result = False

    if not result:
      print((f'Unable to retrieve the volume with the Windows directory from: '
             f'{source_path:s}.'))
      print('')
      return 1

    if extractor_object.windows_version:
      windows_version = extractor_object.windows_version
      logging.info(f'Detected Windows version: {windows_version:s}')

      if source_definition['windows_version']:
        windows_version = source_definition['windows_version']

    else:
      print('Unable to determine Windows version.')

      windows_version = source_definition['windows_version']
      if not windows_version:
        print('Windows version required, specify one with --windows-version.')
        print('')
        return 1

    extractor_object.CollectSystemEnvironmentVariables()

    event_log_providers = {}
    original_message_file_paths = {}

    for event_log_provider in extractor_object.CollectEventLogProviders():
      name = event_log_provider.name
      if not name:
        log_sources = sorted(event_log_provider.log_sources)
        name = log_sources[0]

      providers_per_log_source[name] = []

      message_files = set()
      for path in event_log_provider.category_message_files:
        path_lower = path.lower()
        if path_lower not in original_message_file_paths:
          original_message_file_paths[path_lower] = path

        message_files.add(path_lower)

      event_log_provider.category_message_files = message_files

      message_files = set()
      for path in event_log_provider.event_message_files:
        path_lower = path.lower()
        if path_lower not in original_message_file_paths:
          original_message_file_paths[path_lower] = path

        message_files.add(path_lower)

      event_log_provider.event_message_files = message_files

      message_files = set()
      for path in event_log_provider.parameter_message_files:
        path_lower = path.lower()
        if path_lower not in original_message_file_paths:
          original_message_file_paths[path_lower] = path

        message_files.add(path_lower)

      event_log_provider.parameter_message_files = message_files

      event_log_providers[name] = event_log_provider

    if event_log_providers:
      event_log_providers_per_version.append(
          (windows_version, event_log_providers))

  for name, providers in sorted(providers_per_log_source.items()):
    for windows_version, event_log_providers in event_log_providers_per_version:
      event_log_provider = event_log_providers.get(name, None)
      if not event_log_provider:
        continue

      is_equivalent = False
      for provider_and_versions in providers:
        result_event_log_provider = provider_and_versions['event_log_provider']
        is_equivalent = CompareEventLogProviders(
            result_event_log_provider, event_log_provider)

        if is_equivalent:
          provider_and_versions['windows_versions'].append(windows_version)
          break

      if not is_equivalent:
        result_event_log_provider = {
            'event_log_provider': event_log_provider,
            'windows_versions': [windows_version]}
        providers.append(result_event_log_provider)

  output_directory = os.path.join('docs', 'sources', 'eventlog-providers')
  os.makedirs(output_directory, exist_ok=True)

  index_rst_file_path = os.path.join(output_directory, 'index.rst')
  with documentation.EventLogProvidersIndexRstWriter(
      index_rst_file_path) as index_rst_writer:
    for name, providers in sorted(providers_per_log_source.items()):
      index_rst_writer.WriteEventLogProvider(name)

      output_filename = f'Provider-{name:s}.md'.replace(
          ' ', '-').replace('/', '-')

      markdown_file_path = os.path.join(output_directory, output_filename)
      with documentation.EventLogProviderMarkdownWriter(
          markdown_file_path) as markdown_writer:
        for provider_and_versions in providers:
          event_log_provider = provider_and_versions['event_log_provider']
          # TODO: preserver original message paths in output

          markdown_writer.WriteEventLogProvider(
              event_log_provider, provider_and_versions['windows_versions'])

  if not providers_per_log_source:
    print('No Windows Event Log providers found.')

  return 0


if __name__ == '__main__':
  sys.exit(Main())

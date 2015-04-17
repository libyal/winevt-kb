#!/usr/bin/python
"""Classes to implement a Windows volume collector."""

import os

import dfvfs

from dfvfs.lib import definitions as dfvfs_definitions
from dfvfs.lib import errors as dfvfs_errors
from dfvfs.helpers import source_scanner
from dfvfs.helpers import windows_path_resolver
from dfvfs.resolver import resolver
from dfvfs.volume import tsk_volume_system


if dfvfs.__version__ < u'20140727':
  raise ImportWarning(u'extract.py requires dfvfs 20140727 or later.')


class CollectorError(Exception):
  """Class that defines collector errors."""


class WindowsVolumeCollector(object):
  """Class that defines a Windows volume collector."""

  _WINDOWS_DIRECTORIES = frozenset([
      u'C:\\Windows',
      u'C:\\WINNT',
      u'C:\\WTSRV',
      u'C:\\WINNT35',
  ])

  def __init__(self):
    """Initializes the Windows volume collector object."""
    super(WindowsVolumeCollector, self).__init__()
    self._file_system = None
    self._path_resolver = None
    self._scanner = source_scanner.SourceScanner()
    self._windows_directory = None

  def _ScanFileSystem(self, path_resolver):
    """Scans a file system for the Windows volume.

    Args:
      path_resolver: the path resolver (instance of dfvfs.WindowsPathResolver).

    Returns:
      True if the Windows directory was found, false otherwise.

    """
    result = False

    for windows_path in self._WINDOWS_DIRECTORIES:
      windows_path_spec = path_resolver.ResolvePath(windows_path)

      result = windows_path_spec is not None
      if result:
        self._windows_directory = windows_path
        break

    return result

  def _ScanTSKPartionVolumeSystemPathSpec(self, scan_context):
    """Scans a path specification for the Windows volume.

    Args:
      scan_context: the scan context (instance of dfvfs.ScanContext).

    Returns:
      The volume scan node (instance of dfvfs.SourceScanNode) of the volume
      that contains the Windows directory or None.

    Raises:
      CollectorError: if the scan context is invalid.
    """
    if (not scan_context or not scan_context.last_scan_node or
        not scan_context.last_scan_node.path_spec):
      raise CollectorError(u'Invalid scan context.')

    volume_system = tsk_volume_system.TSKVolumeSystem()
    volume_system.Open(scan_context.last_scan_node.path_spec)

    volume_identifiers = self._scanner.GetVolumeIdentifiers(volume_system)
    if not volume_identifiers:
      return

    volume_scan_node = None
    result = False

    for volume_identifier in volume_identifiers:
      volume_location = u'/{0:s}'.format(volume_identifier)
      volume_scan_node = scan_context.last_scan_node.GetSubNodeByLocation(
          volume_location)
      volume_path_spec = getattr(volume_scan_node, u'path_spec', None)

      # The leaf scan node shoudl contain the actual file system.
      file_system_scan_node = volume_scan_node.GetSubNodeByLocation(u'/')
      if not file_system_scan_node:
        continue

      while file_system_scan_node.sub_nodes:
        file_system_scan_node = file_system_scan_node.GetSubNodeByLocation(u'/')

      file_system_path_spec = getattr(file_system_scan_node, u'path_spec', None)
      file_system = resolver.Resolver.OpenFileSystem(file_system_path_spec)

      if file_system is None:
        continue

      path_resolver = windows_path_resolver.WindowsPathResolver(
          file_system, volume_path_spec)

      result = self._ScanFileSystem(path_resolver)
      if result:
        break

    if not result:
      return

    return volume_scan_node

  def GetWindowsVolumePathSpec(self, source_path):
    """Determines the file system path specification of the Windows volume.

    Args:
      source_path: the source path.

    Returns:
      True if successful or False otherwise.

    Raises:
      CollectorError: if the source path does not exists, or if the source path
                      is not a file or directory, or if the format of or within
                      the source file is not supported.
    """
    # Note that os.path.exists() does not support Windows device paths.
    if (not source_path.startswith(u'\\\\.\\') and
        not os.path.exists(source_path)):
      raise CollectorError(
          u'No such device, file or directory: {0:s}.'.format(source_path))

    scan_context = source_scanner.SourceScannerContext()
    scan_path_spec = None

    scan_context.OpenSourcePath(source_path)

    while True:
      last_scan_node = scan_context.last_scan_node
      try:
        scan_context = self._scanner.Scan(
            scan_context, scan_path_spec=scan_path_spec)
      except dfvfs_errors.BackEndError as exception:
        raise CollectorError(
            u'Unable to scan source, with error: {0:s}'.format(exception))

      # The source is a directory or file.
      if scan_context.source_type in [
          scan_context.SOURCE_TYPE_DIRECTORY, scan_context.SOURCE_TYPE_FILE]:
        break

      if (not scan_context.last_scan_node or
          scan_context.last_scan_node == last_scan_node):
        raise CollectorError(
            u'No supported file system found in source: {0:s}.'.format(
                self._source_path))

      # The source scanner found a file system.
      if scan_context.last_scan_node.type_indicator in [
          dfvfs_definitions.TYPE_INDICATOR_TSK]:
        break

      # The source scanner found a BitLocker encrypted volume and we need
      # a credential to unlock the volume.
      if scan_context.last_scan_node.type_indicator in [
          dfvfs_definitions.TYPE_INDICATOR_BDE]:
        # TODO: ask for password.
        raise CollectorError(
            u'BitLocker encrypted volume not yet supported.')

      # The source scanner found a partition table and we need to determine
      # which partition contains the Windows directory.
      elif scan_context.last_scan_node.type_indicator in [
          dfvfs_definitions.TYPE_INDICATOR_TSK_PARTITION]:
        scan_node = self._ScanTSKPartionVolumeSystemPathSpec(scan_context)
        if not scan_node:
          return False
        scan_context.last_scan_node = scan_node

      # The source scanner found Volume Shadow Snapshot which is ignored.
      elif scan_context.last_scan_node.type_indicator in [
          dfvfs_definitions.TYPE_INDICATOR_VSHADOW]:
        # Get the scan node of the current volume.
        scan_node = scan_context.last_scan_node.GetSubNodeByLocation(u'/')
        scan_context.last_scan_node = scan_node
        break

      else:
        raise CollectorError(
            u'Unsupported volume system found in source: {0:s}.'.format(
                self._source_path))

    # TODO: add single file support.
    if scan_context.source_type == scan_context.SOURCE_TYPE_FILE:
      raise CollectorError(
          u'Unsupported source: {0:s}.'.format(source_path))

    if scan_context.source_type != scan_context.SOURCE_TYPE_DIRECTORY:
      if not scan_context.last_scan_node.type_indicator in [
          dfvfs_definitions.TYPE_INDICATOR_TSK]:
        raise CollectorError(
            u'Unsupported source: {0:s} found unsupported file system.'.format(
                source_path))

    file_system_path_spec = getattr(
        scan_context.last_scan_node, u'path_spec', None)
    self._file_system = resolver.Resolver.OpenFileSystem(
        file_system_path_spec)

    if file_system_path_spec.type_indicator in [
        dfvfs_definitions.TYPE_INDICATOR_OS]:
      mount_point = file_system_path_spec
    else:
      mount_point = file_system_path_spec.parent

    self._path_resolver = windows_path_resolver.WindowsPathResolver(
        self._file_system, mount_point)

    # The source is a directory or single volume storage media image.
    if not self._windows_directory:
      if not self._ScanFileSystem(self._path_resolver):
        return False

    if not self._windows_directory:
      return False

    self._path_resolver.SetEnvironmentVariable(
        u'WinDir', self._windows_directory)

    return True

  def OpenFile(self, windows_path):
    """Opens the file specificed by the Windows path.

    Args:
      windows_path: the Windows path to the file.

    Returns:
      The file-like object (instance of dfvfs.FileIO) or None if
      the file does not exist.
    """
    path_spec = self._path_resolver.ResolvePath(windows_path)
    if path_spec is None:
      return None

    return resolver.Resolver.OpenFileObject(path_spec)

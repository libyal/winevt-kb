# -*- coding: utf-8 -*-
"""Classes to implement a Windows volume collector."""

import dfvfs
import dfwinreg

from dfvfs.helpers import volume_scanner as dfvfs_volume_scanner
from dfvfs.lib import definitions as dfvfs_definitions
from dfvfs.path import factory as dfvfs_path_spec_factory
from dfvfs.resolver import resolver as dfvfs_resolver
from dfwinreg import interface as dfwinreg_interface
from dfwinreg import regf as dfwinreg_regf


if dfvfs.__version__ < u'20160227':
  raise ImportWarning(u'collector.py requires dfvfs 20160227 or later.')

if dfwinreg.__version__ < u'20151026':
  raise ImportWarning(u'collector.py requires dfwinreg 20151026 or later.')


class WindowsVolumeCollector(dfvfs_volume_scanner.WindowsVolumeScanner):
  """Class that defines a Windows volume collector."""


class CollectorRegistryFileReader(dfwinreg_interface.WinRegistryFileReader):
  """Class that defines the collector-based Windows Registry file reader."""

  def __init__(self, volume_scanner):
    """Initializes the Windows Registry file reader object.

    Args:
      volume_scanner: the Windows volume scanner (instance of
                      WindowsVolumeScanner).
    """
    super(CollectorRegistryFileReader, self).__init__()
    self._volume_scanner = volume_scanner

  def Open(self, path, ascii_codepage=u'cp1252'):
    """Opens the Windows Registry file specificed by the path.

    Args:
      path: string containing the path of the Windows Registry file. The path
            is a Windows path relative to the root of the file system that
            contains the specfic Windows Registry file. E.g.
            C:\\Windows\\System32\\config\\SYSTEM
      ascii_codepage: optional ASCII string codepage.

    Returns:
      The Windows Registry file (instance of WinRegistryFile) or None.
    """
    file_object = self._volume_scanner.OpenFile(path)
    if file_object is None:
      return

    registry_file = dfwinreg_regf.REGFWinRegistryFile(
        ascii_codepage=ascii_codepage)

    try:
      registry_file.Open(file_object)
    except IOError:
      file_object.close()
      return

    return registry_file

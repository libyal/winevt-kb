# -*- coding: utf-8 -*-
"""Script to extract the strings from Event Log message resource files."""

import logging

import pyexe
import pywrc


if pyexe.get_version() < u'20131229':
  raise ImportWarning(u'extract.py requires pyexe 20131229 or later.')

if pywrc.get_version() < u'20140128':
  raise ImportWarning(u'extract.py requires pywrc 20140128 or later.')


# pylint: disable=logging-format-interpolation

class MessageResourceFile(object):
  """Class that defines a Windows Message Resource file."""

  _RESOURCE_IDENTIFIER_STRING = 0x06
  _RESOURCE_IDENTIFIER_MESSAGE_TABLE = 0x0b
  _RESOURCE_IDENTIFIER_VERSION = 0x10

  def __init__(
      self, windows_path, ascii_codepage=u'cp1252',
      preferred_language_identifier=0x0409):
    """Initializes the Windows Message Resource file.

    Args:
      windows_path: normalized version of the Windows path.
      ascii_codepage: optional ASCII string codepage. The default is cp1252
                      (or windows-1252).
      preferred_language_identifier: optional preferred language identifier
                                     (LCID). The default is 0x0409 (en-US).
    """
    super(MessageResourceFile, self).__init__()
    self._ascii_codepage = ascii_codepage
    self._exe_file = pyexe.file()
    self._exe_file.set_ascii_codepage(self._ascii_codepage)
    self._file_object = None
    self._file_version = None
    self._is_open = False
    self._preferred_language_identifier = preferred_language_identifier
    self._product_version = None
    self._wrc_stream = pywrc.stream()
    # TODO: wrc stream set codepage?
    self.windows_path = windows_path

  def _GetVersionInformation(self):
    """Retrieves the file and product version."""
    version_resource = self._wrc_stream.get_resource_by_identifier(
        self._RESOURCE_IDENTIFIER_VERSION)
    if not version_resource:
      return None, None

    file_version = None
    product_version = None
    language_identifier = self._preferred_language_identifier
    if language_identifier in version_resource.language_identifiers:
      file_version = version_resource.get_file_version(language_identifier)
      product_version = version_resource.get_product_version(
          language_identifier)

    if not file_version or not product_version:
      for language_identifier in version_resource.language_identifiers:
        file_version = version_resource.get_file_version(language_identifier)
        product_version = version_resource.get_product_version(
            language_identifier)

        if file_version and product_version:
          break

    self._file_version = u'{0:d}.{1:d}.{2:d}.{3:d}'.format(
        (file_version >> 48) & 0xffff, (file_version >> 32) & 0xffff,
        (file_version >> 16) & 0xffff, file_version & 0xffff)

    self._product_version = u'{0:d}.{1:d}.{2:d}.{3:d}'.format(
        (product_version >> 48) & 0xffff, (product_version >> 32) & 0xffff,
        (product_version >> 16) & 0xffff, product_version & 0xffff)

    if file_version != product_version:
      logging.warning((
          u'Mismatch between file version: {0:s} and product version: '
          u'{1:s} in message file: {2:s}.').format(
              self._file_version, self._product_version, self.windows_path))

  @property
  def file_version(self):
    """The file version."""
    if self._file_version is None:
      self._GetVersionInformation()
    return self._file_version

  @property
  def product_version(self):
    """The product version."""
    if self._product_version is None:
      self._GetVersionInformation()
    return self._product_version

  def GetMessageTableResource(self):
    """Retrieves the message table resource."""
    return self._wrc_stream.get_resource_by_identifier(
        self._RESOURCE_IDENTIFIER_MESSAGE_TABLE)

  def GetMuiLanguage(self):
    """Retrieves the MUI language or None if not available."""
    mui_resource = self._wrc_stream.get_resource_by_name(u'MUI')
    if not mui_resource:
      return None

    mui_language = None
    language_identifier = self._preferred_language_identifier
    if language_identifier in mui_resource.language_identifiers:
      mui_language = mui_resource.get_language(language_identifier)

    if not mui_language:
      for language_identifier in mui_resource.language_identifiers:
        mui_language = mui_resource.get_language(language_identifier)
        if mui_language:
          break

    return mui_language

  def GetStringResource(self):
    """Retrieves the string resource."""
    return self._wrc_stream.get_resource_by_identifier(
        self._RESOURCE_IDENTIFIER_STRING)

  def Open(self, file_object):
    """Opens the Windows Message Resource file using a file-like object.

    Args:
      file_object: the file-like object.

    Returns:
      A boolean containing True if successful or False if not.

    Raises:
      IOError: if already open.
    """
    if self._is_open:
      raise IOError(u'Already open.')

    self._file_object = file_object
    self._exe_file.open_file_object(self._file_object)
    exe_section = self._exe_file.get_section_by_name(u'.rsrc')

    if not exe_section:
      self._exe_file.close()
      return False

    self._wrc_stream.set_virtual_address(exe_section.virtual_address)
    self._wrc_stream.open_file_object(exe_section)

    return True

  def Close(self):
    """Closes the Windows Message Resource file.

    Raises:
      IOError: if not open.
    """
    if self._is_open:
      raise IOError(u'Not opened.')

    self._wrc_stream.close()
    self._exe_file.close()
    self._file_object.close()
    self._file_object = None

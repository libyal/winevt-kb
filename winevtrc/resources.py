# -*- coding: utf-8 -*-
"""Classes to represent Windows Event Log resources."""

from winevtrc import py2to3


class EventLogProvider(object):
  """Class that defines a Windows Event Log provider.

  Attributes:
    category_message_files (list[str]): filenames of the category message files.
    event_message_files (list[str]): filenames of the event message files.
    log_type (str): Event Log type.
    log_source (str): Event Log source.
    parameter_message_files (list[str]): filenames of the parameter message
        files.
    provider_guid (str): Log provider GUID.
  """

  def __init__(self, log_type, log_source, provider_guid):
    """Initializes the Windows Event Log provider.

    Args:
      log_type (str): Event Log type.
      log_source (str): Event Log source.
      provider_guid (str): Event Log provider GUID.
    """
    super(EventLogProvider, self).__init__()
    self.category_message_files = None
    self.event_message_files = None
    self.log_type = log_type
    self.log_source = log_source
    self.parameter_message_files = None
    self.provider_guid = provider_guid

  def SetCategoryMessageFilenames(self, category_message_filenames):
    """Sets the category message filenames.

    Args:
      category_message_filenames (str|list[str]): category message filenames,
          where multiple filenames in the same string are separated by ';'.
    """
    if isinstance(category_message_filenames, py2to3.STRING_TYPES):
      self.category_message_files = category_message_filenames.split(u';')
    else:
      self.category_message_files = category_message_filenames

  def SetEventMessageFilenames(self, event_message_filenames):
    """Sets the event message filenames.

    Args:
      event_message_filenames (str|list[str]): event message filenames,
          where multiple filenames in the same string are separated by ';'.
    """
    if isinstance(event_message_filenames, py2to3.STRING_TYPES):
      self.event_message_files = event_message_filenames.split(u';')
    else:
      self.event_message_files = event_message_filenames

  def SetParameterMessageFilenames(self, parameter_message_filenames):
    """Sets the parameter message filenames.

    Args:
      parameter_message_filenames (str|list[str]): parameter message filenames,
          where multiple filenames in the same string are separated by ';'.
    """
    if isinstance(parameter_message_filenames, py2to3.STRING_TYPES):
      self.parameter_message_files = parameter_message_filenames.split(u';')
    else:
      self.parameter_message_files = parameter_message_filenames


class MessageFile(object):
  """Class that defines a Windows Event Log message file.

  Attributes:
    name (str): name.
    windows_path (str): Windows path.
  """

  def __init__(self, name):
    """Initializes the message file.

    Args:
      name (str): name.
    """
    super(MessageFile, self).__init__()
    self._message_tables_per_language = {}
    self._string_tables_per_language = {}
    self.name = name
    self.windows_path = None

  def AppendMessageTable(self, lcid, file_version):
    """Appends a message table.

    Args:
      lcid (int): language identifier (LCID).
      file_version (str): Windows Event Log resource file version of the file
          that contains the message table.
    """
    if lcid not in self._message_tables_per_language:
      self._message_tables_per_language[lcid] = MessageTable(lcid)

    self._message_tables_per_language[lcid].file_versions.append(file_version)

  def AppendStringTable(self, lcid, file_version):
    """Appends a string table.

    Args:
      lcid (int): language identifier (LCID).
      file_version (str): Windows Event Log resource file version of the file
          that contains the string table.
    """
    if lcid not in self._string_tables_per_language:
      self._string_tables_per_language[lcid] = StringTable(lcid)

    self._string_tables_per_language[lcid].file_versions.append(file_version)

  def GetMessageTable(self, lcid):
    """Retrieves the message table for a specific language.

    Args:
      lcid (int): language identifier (LCID).

    Returns:
      MessageTable: message table or None.
    """
    return self._message_tables_per_language.get(lcid, None)

  def GetStringTable(self, lcid):
    """Retrieves the string table for a specific language.

    Args:
      lcid (int): language identifier (LCID).

    Returns:
      StringTable: string table or None.
    """
    return self._string_tables_per_language.get(lcid, None)

  def GetMessageTables(self):
    """Retrieves the message tables.

    Yields:
      MessageTable: message table.
    """
    for message_table in iter(self._message_tables_per_language.values()):
      yield message_table

  def GetStringTables(self):
    """Retrieves the string tables.

    Yields:
      StringTable: string table.
    """
    for string_table in iter(self._string_tables_per_language.values()):
      yield string_table


class MessageTable(object):
  """Class that contains the messages per language.

  Attributes:
    file_versions (list[str]): Windows Event Log resource file versions.
    lcid (int): language identifier (LCID).
    message_strings (list[str]): Windows Event Log resource message strings.
  """

  def __init__(self, lcid):
    """Initializes the message table.

    Args:
      lcid (int): language identifier (LCID).
    """
    super(MessageTable, self).__init__()
    self.file_versions = []
    self.lcid = lcid
    self.message_strings = {}


class StringTable(object):
  """Class that contains the strings per language.

  Attributes:
    file_versions (list[str]): Windows Event Log resource file versions.
    lcid (int): language identifier (LCID).
    strings (list[str]): Windows Event Log resource strings.
  """

  def __init__(self, lcid):
    """Initializes the string table.

    Args:
      lcid (int): language identifier (LCID).
    """
    super(StringTable, self).__init__()
    self.file_versions = []
    self.lcid = lcid
    self.strings = {}

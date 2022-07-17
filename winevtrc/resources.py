# -*- coding: utf-8 -*-
"""Windows Event Log resources."""


class EnvironmentVariable(object):
  """Environment variable.

  Attributes:
    name (str): name.
    value (str): value.
  """

  def __init__(self, name, value):
    """Initializes an environment variable.

    Args:
      name (str): name.
      value (str): value.
    """
    super(EnvironmentVariable, self).__init__()
    self.name = name
    self.value = value


class EventLogProvider(object):
  """Windows Event Log provider.

  Attributes:
    additional_identifier (str): additional identifier of the provider,
        contains a GUID.
    category_message_files (set[str]): paths of the category message files.
    event_message_files (set[str]): paths of the event message files.
    identifier (str): identifier of the provider, contains a GUID.
    log_sources (list[str]): names of the corresponding Event Log sources.
    log_types (list[str]): Windows Event Log types.
    name (str): name of the provider.
    parameter_message_files (set[str]): paths of the parameter message
        files.
  """

  def __init__(self):
    """Initializes the Windows Event Log provider."""
    super(EventLogProvider, self).__init__()
    self.additional_identifier = None
    self.category_message_files = set()
    self.event_message_files = set()
    self.identifier = None
    self.log_sources = []
    self.log_types = []
    self.name = None
    self.parameter_message_files = set()

  @property
  def log_source(self):
    """str: name of the Windows Event Log source."""
    try:
      return self.log_sources[0]
    except IndexError:
      return None

  @property
  def log_type(self):
    """str: name of the Windows Event Log type."""
    try:
      return self.log_types[0]
    except IndexError:
      return None

  def SetCategoryMessageFilenames(self, category_message_filenames):
    """Sets the category message filenames.

    Args:
      category_message_filenames (str|list[str]): category message filenames,
          where multiple filenames in the same string are separated by ';'.
    """
    if isinstance(category_message_filenames, str):
      category_message_filenames = category_message_filenames.split(';')

    self.category_message_files = set(category_message_filenames)

  def SetEventMessageFilenames(self, event_message_filenames):
    """Sets the event message filenames.

    Args:
      event_message_filenames (str|list[str]): event message filenames,
          where multiple filenames in the same string are separated by ';'.
    """
    if isinstance(event_message_filenames, str):
      event_message_filenames = event_message_filenames.split(';')

    self.event_message_files = set(event_message_filenames)

  def SetParameterMessageFilenames(self, parameter_message_filenames):
    """Sets the parameter message filenames.

    Args:
      parameter_message_filenames (str|list[str]): parameter message filenames,
          where multiple filenames in the same string are separated by ';'.
    """
    if isinstance(parameter_message_filenames, str):
      parameter_message_filenames = parameter_message_filenames.split(';')

    self.parameter_message_files = set(parameter_message_filenames)


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
    for message_table in self._message_tables_per_language.values():
      yield message_table

  def GetStringTables(self):
    """Retrieves the string tables.

    Yields:
      StringTable: string table.
    """
    for string_table in self._string_tables_per_language.values():
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

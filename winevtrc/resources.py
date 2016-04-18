# -*- coding: utf-8 -*-
"""Classes to represent Windows Event Log resources."""


class EventLogProvider(object):
  """Class that defines a Windows Event Log provider.

  Attributes:
    category_message_filenames: a list of strings containing the filenames
                                of the category message files.
    event_message_filenames: a list of strings containing the filenames
                             of the event message files.
    log_type: a string containing the Event Log type.
    log_source: a string containing the Event Log source.
    parameter_message_filenames: a list of strings containing the filenames
                                 of the parameter message files.
    provider_guid: a string containing the Event Log provider GUID.
  """

  def __init__(self, log_type, log_source, provider_guid):
    """Initializes the Windows Event Log provider.

    Args:
      log_type: a string containing the Event Log type.
      log_source: a string containing the Event Log source.
      provider_guid: a string containing the Event Log provider GUID.
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
      category_message_filenames: a string containing ; separated filenames,
                                  or a list of filenames.
    """
    if isinstance(category_message_filenames, basestring):
      self.category_message_files = category_message_filenames.split(u';')
    else:
      self.category_message_files = category_message_filenames

  def SetEventMessageFilenames(self, event_message_filenames):
    """Sets the event message filenames.

    Args:
      event_message_filenames: a string containing ; separated filenames,
                               or a list of filenames.
    """
    if isinstance(event_message_filenames, basestring):
      self.event_message_files = event_message_filenames.split(u';')
    else:
      self.event_message_files = event_message_filenames

  def SetParameterMessageFilenames(self, parameter_message_filenames):
    """Sets the parameter message filenames.

    Args:
      parameter_message_filenames: a string containing ; separated filenames,
                                   or a list of filenames.
    """
    if isinstance(parameter_message_filenames, basestring):
      self.parameter_message_files = parameter_message_filenames.split(u';')
    else:
      self.parameter_message_files = parameter_message_filenames


class MessageFile(object):
  """Class that contains the messages per file.

  Attributes:
    name: a string containing the name.
    windows_path: a string containing the Windows path.
  """

  def __init__(self, name):
    """Initializes the message file object.

    Args:
      name: a string containing the name.
    """
    super(MessageFile, self).__init__()
    self._message_tables_per_language = {}
    self._string_tables_per_language = {}
    self.name = name
    self.windows_path = None

  def AppendMessageTable(self, lcid, file_version):
    """Appends a message table.

    Args:
      lcid: an integer containing the language identifier.
      file_version: a string containing the Windows Event Log resource
                    file version.
    """
    if lcid not in self._message_tables_per_language:
      self._message_tables_per_language[lcid] = MessageTable(lcid)

    self._message_tables_per_language[lcid].file_versions.append(file_version)

  def AppendStringTable(self, lcid, file_version):
    """Appends a string table.

    Args:
      lcid: an integer containing the language identifier.
      file_version: the string file version.
    """
    if lcid not in self._string_tables_per_language:
      self._string_tables_per_language[lcid] = StringTable(lcid)

    self._string_tables_per_language[lcid].file_versions.append(file_version)

  def GetMessageTable(self, lcid):
    """Retrieves the message table for a specific language.

    Args:
      lcid: an integer containing the language identifier.

    Returns:
      The message table (instance of MessageTable).
    """
    return self._message_tables_per_language.get(lcid, None)

  def GetStringTable(self, lcid):
    """Retrieves the string table for a specific language.

    Args:
      lcid: an integer containing the language identifier.

    Returns:
      The string table (instance of StringTable).
    """
    return self._string_tables_per_language.get(lcid, None)

  def GetMessageTables(self):
    """Retrieves the message tables.

    Yields:
      A message table (instance of MessageTable).
    """
    for message_table in self._message_tables_per_language.itervalues():
      yield message_table

  def GetStringTables(self):
    """Retrieves the string tables.

    Yields:
      A string table (instance of StringTable).
    """
    for string_table in self._string_tables_per_language.itervalues():
      yield string_table


class MessageTable(object):
  """Class that contains the messages per language.

  Attributes:
    file_versions: a list of strings containing the Windows Event Log
                   resource file versions.
    lcid: an integer containing the language identifier.
    message_strings: a list of Windows Event Log resource message strings.
  """

  def __init__(self, lcid):
    """Initializes the message table object.

    Args:
      lcid: the language identifier.
    """
    super(MessageTable, self).__init__()
    self.file_versions = []
    self.lcid = lcid
    self.message_strings = {}


class StringTable(object):
  """Class that contains the strings per language.

  Attributes:
    file_versions: a list of strings containing the Windows Event Log
                   resource file versions.
    lcid: an integer containing the language identifier.
    strings: a list of Windows Event Log resource strings.
  """

  def __init__(self, lcid):
    """Initializes the string table object.

    Args:
      lcid: an integer containing the language identifier.
    """
    super(StringTable, self).__init__()
    self.file_versions = []
    self.lcid = lcid
    self.strings = {}

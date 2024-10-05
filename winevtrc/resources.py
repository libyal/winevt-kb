# -*- coding: utf-8 -*-
"""Windows Event Log resources."""

from acstore.containers import interface as containers_interface
from acstore.containers import manager as containers_manager


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


class WinevtResourcesEventLogProvider(containers_interface.AttributeContainer):
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
    windows_version (str): Windows version.
  """

  CONTAINER_TYPE = 'winevtrc_eventlog_provider'

  SCHEMA = {
      'additional_identifier': 'str',
      'category_message_files': 'List[str]',
      'event_message_files': 'List[str]',
      'identifier': 'str',
      'log_sources': 'List[str]',
      'log_types': 'List[str]',
      'name': 'str',
      'parameter_message_files': 'List[str]',
      'windows_version': 'str'}

  def __init__(self):
    """Initializes the Windows Event Log provider."""
    super(WinevtResourcesEventLogProvider, self).__init__()
    self.additional_identifier = None
    self.category_message_files = set()
    self.event_message_files = set()
    self.identifier = None
    self.log_sources = []
    self.log_types = []
    self.name = None
    self.parameter_message_files = set()
    self.windows_version = None

  @property
  def log_source(self):
    """str: name of the Windows Event Log source."""
    try:
      return self.log_sources[0]
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


class MessageFileDatabaseDescriptor(containers_interface.AttributeContainer):
  """Windows Event Log message file database descriptor.

  Attributes:
    database_filename (str): database filename.
    windows_path (str): Windows path of the message file.
  """

  CONTAINER_TYPE = 'winevtrc_message_file_database'

  SCHEMA = {
      'database_filename': 'str',
      'windows_path': 'str'}

  def __init__(self, database_filename=None, windows_path=None):
    """Initializes a Windows Event Log message file database descriptor.

    Args:
      database_filename (Optional[str]): database filename.
      windows_path (Optional[str]): message filename.
    """
    super(MessageFileDatabaseDescriptor, self).__init__()
    self.database_filename = database_filename
    self.windows_path = windows_path


class MessageFileDescriptor(containers_interface.AttributeContainer):
  """Windows Event Log message file descriptor.

  Attributes:
    file_version (str): file version.
    product_version (str): product version.
    windows_path (str): path as defined by the Window Event Log provider.
    windows_version (str): Windows version.
  """

  CONTAINER_TYPE = 'winevtrc_message_file'

  SCHEMA = {
      'file_version': 'str',
      'product_version': 'str',
      'windows_path': 'str',
      'windows_version': 'str'}

  def __init__(
      self, file_version=None, product_version=None, windows_path=None,
      windows_version=None):
    """Initializes a Windows Event Log message file descriptor.

    Args:
      file_version (Optional[str]): file version.
      product_version (Optional[str]): product version.
      windows_path (Optional[str]): path as defined by the Window Event Log
          provider.
      windows_version (Optional[str]): Windows version.
    """
    super(MessageFileDescriptor, self).__init__()
    self.file_version = file_version
    self.product_version = product_version
    self.windows_path = windows_path
    self.windows_version = windows_version


class MessageStringDescriptor(containers_interface.AttributeContainer):
  """Windows Event Log message string descriptor.

  Attributes:
    identifier (int): message identifier.
    text (str): message text.
  """

  CONTAINER_TYPE = 'winevtrc_message_string'

  SCHEMA = {
      '_message_table_identifier': 'AttributeContainerIdentifier',
      'language_identifier': 'str',
      'message_identifier': 'int',
      'text': 'str'}

  _SERIALIZABLE_PROTECTED_ATTRIBUTES = [
      '_message_table_identifier']

  def __init__(self, message_identifier=None, text=None):
    """Initializes a Windows Event Log message string descriptor.

    Args:
      message_identifier (Optional[int]): message identifier.
      text (Optional[int]): message text.
    """
    super(MessageStringDescriptor, self).__init__()
    self._message_table_identifier = None
    self.message_identifier = message_identifier
    self.text = text

  def GetMessageTableIdentifier(self):
    """Retrieves the identifier of the associated message table.

    Returns:
      AttributeContainerIdentifier: message table identifier or None when not
          set.
    """
    return self._message_table_identifier

  def SetMessageTableIdentifier(self, message_table_identifier):
    """Sets the identifier of the associated message table.

    Args:
      message_table_identifier (AttributeContainerIdentifier): message table
          identifier.
    """
    self._message_table_identifier = message_table_identifier


class MessageStringMappingDescriptor(containers_interface.AttributeContainer):
  """Windows Event Log message string mapping descriptor.

  Attributes:
    event_identifier (int): event identifier.
    event_version (int): event version.
    message_identifier (int): message identifier.
    provider_identifier (str): Event Log provider identifier.
  """

  CONTAINER_TYPE = 'winevtrc_message_string_mapping'

  SCHEMA = {
      '_message_file_identifier': 'AttributeContainerIdentifier',
      'event_identifier': 'int',
      'event_version': 'int',
      'message_identifier': 'int',
      'provider_identifier': 'str'}

  _SERIALIZABLE_PROTECTED_ATTRIBUTES = [
      '_message_file_identifier']

  def __init__(
      self, event_identifier=None, event_version=None, message_identifier=None,
      provider_identifier=None):
    """Initializes a Windows Event Log message string mapping descriptor.

    Args:
      event_identifier (Optional[int]): event identifier.
      event_version (Optional[int]): event version.
      message_identifier (Optional[int]): message identifier.
      provider_identifier (Optional[str]): Event Log provider identifier.
    """
    super(MessageStringMappingDescriptor, self).__init__()
    self._message_file_identifier = None
    self.event_identifier = event_identifier
    self.event_version = event_version
    self.message_identifier = message_identifier
    self.provider_identifier = provider_identifier

  def GetMessageFileIdentifier(self):
    """Retrieves the identifier of the associated message file.

    Returns:
      AttributeContainerIdentifier: message file identifier or None when
          not set.
    """
    return self._message_file_identifier

  def SetMessageFileIdentifier(self, message_file_identifier):
    """Sets the identifier of the associated message file.

    Args:
      message_file_identifier (AttributeContainerIdentifier): message file
          identifier.
    """
    self._message_file_identifier = message_file_identifier


class MessageTable(object):
  """Class that contains the messages per language.

  Attributes:
    file_versions (list[str]): Windows Event Log resource file versions.
    language_identifier (int): language identifier (LCID).
    message_strings (dict[int, str]): Windows Event Log resource message
       strings per identifier.
  """

  def __init__(self, language_identifier):
    """Initializes the message table.

    Args:
      lcid (int): language identifier (LCID).
    """
    super(MessageTable, self).__init__()
    self.file_versions = []
    self.language_identifier = language_identifier
    self.message_strings = {}

  @property
  def lcid(self):
    """int: language identifier (LCID)."""
    return self.language_identifier


class MessageTableDescriptor(containers_interface.AttributeContainer):
  """Windows Event Log message table descriptor.

  Attributes:
    language_identifier (int): language identifier (LCID).
  """

  CONTAINER_TYPE = 'winevtrc_message_table'

  SCHEMA = {
      '_message_file_identifier': 'AttributeContainerIdentifier',
      'language_identifier': 'int'}

  _SERIALIZABLE_PROTECTED_ATTRIBUTES = [
      '_message_file_identifier']

  def __init__(self, language_identifier=None):
    """Initializes a Windows Event Log message table descriptor.

    Args:
      language_identifier (Optional[int]): language identifier (LCID).
    """
    super(MessageTableDescriptor, self).__init__()
    self._message_file_identifier = None
    self.language_identifier = language_identifier

  def GetMessageFileIdentifier(self):
    """Retrieves the identifier of the associated message file.

    Returns:
      AttributeContainerIdentifier: message file identifier or None when not
          set.
    """
    return self._message_file_identifier

  def SetMessageFileIdentifier(self, message_file_identifier):
    """Sets the identifier of the associated message file.

    Args:
      message_file_identifier (AttributeContainerIdentifier): message file
          identifier.
    """
    self._message_file_identifier = message_file_identifier


containers_manager.AttributeContainersManager.RegisterAttributeContainers([
    WinevtResourcesEventLogProvider, MessageFileDatabaseDescriptor,
    MessageFileDescriptor, MessageStringDescriptor,
    MessageStringMappingDescriptor, MessageTableDescriptor])

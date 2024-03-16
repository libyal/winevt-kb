# -*- coding: utf-8 -*-
"""Attribute container store."""

from acstore import interface as acstore_interface
from acstore.helpers import schema as acstore_schema_helper


class JSONStringsListAttributeSerializer(acstore_interface.AttributeSerializer):
  """JSON strings list attribute serializer."""

  def DeserializeValue(self, value):
    """Deserializes a value.

    Args:
      value (list[str]): serialized value.

    Returns:
      list[str]: runtime value.
    """
    return value

  def SerializeValue(self, value):
    """Serializes a value.

    Args:
      value (list[str]): runtime value.

    Returns:
      list[str]: serialized value.
    """
    return value


acstore_schema_helper.SchemaHelper.RegisterDataTypes({
    'List[str]': {
        'json': JSONStringsListAttributeSerializer()}})

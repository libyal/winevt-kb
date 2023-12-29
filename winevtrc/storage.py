# -*- coding: utf-8 -*-
"""Attribute container store."""

import json

from acstore import interface as acstore_interface
from acstore.helpers import schema as acstore_schema_helper


class JSONStringsListAttributeSerializer(acstore_interface.AttributeSerializer):
  """JSON strings list attribute serializer."""

  def DeserializeValue(self, value):
    """Deserializes a value.

    Args:
      value (str): serialized value.

    Returns:
      list[str]: runtime value.
    """
    return json.loads(value)

  def SerializeValue(self, value):
    """Serializes a value.

    Args:
      value (str): runtime value.

    Returns:
      list[str]: serialized value.
    """
    return json.dumps(value)


acstore_schema_helper.SchemaHelper.RegisterDataTypes({
    'List[str]': {
        'json': JSONStringsListAttributeSerializer()}})

"""Message string formatter."""

import re


class MessageStringFormatter:
    """Message string formatter."""

    # Message string specifiers that mark end-of-string.
    _END_OF_STRING_SPECIFIER_RE = re.compile(r"%0(?!\d)")

    # Message string specifiers that are considered white space.
    _WHITE_SPACE_SPECIFIER_RE = re.compile(r"(%b|[\r\n])")

    # Message string specifiers that expand to text.
    _TEXT_SPECIFIER_RE = re.compile(r"%([ .!%nrt])")

    # Curly brackets in a message string.
    _CURLY_BRACKETS_RE = re.compile(r"([\{\}])")

    # Message string specifiers that expand to a variable place holder.
    _PLACE_HOLDER_SPECIFIER_RE = re.compile(r"%([1-9][0-9]?)[!]?[s]?[!]?")

    def FormatMessageStringInPEP3101(self, message_string):
        """Formats a message string in Python format() (PEP 3101) style.

        Args:
          message_string (str): message string.

        Returns:
          str: message string in Python format() (PEP 3103) style or None
              if not available.
        """

        def PlaceHolderSpecifierReplacer(match_object):
            """Replaces message string place holders into Python format() style."""
            expanded_groups = []
            for group in match_object.groups():
                try:
                    place_holder_number = int(group, 10) - 1
                    expanded_group = f"{{{place_holder_number:d}:s}}"
                except ValueError:
                    expanded_group = group

                expanded_groups.append(expanded_group)

            return "".join(expanded_groups)

        if not message_string:
            return None

        message_string = self._END_OF_STRING_SPECIFIER_RE.split(
            message_string, maxsplit=1
        )[0]
        message_string = self._WHITE_SPACE_SPECIFIER_RE.sub(r"", message_string)
        message_string = self._TEXT_SPECIFIER_RE.sub(r"\\\1", message_string)
        message_string = self._CURLY_BRACKETS_RE.sub(r"\1\1", message_string)
        return self._PLACE_HOLDER_SPECIFIER_RE.sub(
            PlaceHolderSpecifierReplacer, message_string
        )

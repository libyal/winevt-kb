"""Message string formatter."""

import re


class MessageStringFormatter:
    """Message string formatter."""

    # Specifiers that mark end-of-string ("%0").
    _END_OF_STRING_SPECIFIER_RE = re.compile(r"%0(?!\d)")

    # Specifiers that are considered white space ("%b", "\r" and "\n").
    _WHITE_SPACE_SPECIFIER_RE = re.compile(r"(%b|[\r\n])")

    # Specifiers that expand to text ("% ", "%.", "%!", "%n", "%r", "%t").
    _TEXT_SPECIFIER_RE = re.compile(r"%([ .!%nrt])")

    # Curly brackets.
    _CURLY_BRACKETS_RE = re.compile(r"([\{\}])")

    # Specifiers that expand to a variable place holder (e.g. %1 or %12).
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

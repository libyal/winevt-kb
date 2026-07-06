"""Read from and write to SQLite databases."""

import re
import sqlite3

from winevtrc import definitions
from winevtrc import errors
from winevtrc import resources


class SQLite3DatabaseFile:
    """A SQLite database file."""

    _HAS_TABLE_QUERY = (
        "SELECT name FROM sqlite_master WHERE type = 'table' AND name = '{0:s}'"
    )

    def __init__(self):
        """Initializes the database file."""
        super().__init__()
        self._connection = None
        self._cursor = None
        self.filename = None
        self.read_only = None

    def _GetValues(self, cursor, table_names, column_names, condition):
        """Values generator function.

        Args:
          cursor (sqlite3.Cursor): SQLite database cursor.
          table_names (list[str]): table names.
          column_names (list[str]): column names.
          condition (str): condition.

        Yields:
          dict[str, object]: value.

        Raises:
          BackendError: if the database back-end raises an exception.
        """
        table_names = ", ".join(table_names)
        column_names_string = ", ".join(column_names)

        sql_query = f"SELECT {column_names_string:s} FROM {table_names:s}"
        if condition:
            sql_query = "".join([sql_query, f" WHERE {condition:s}"])

        try:
            cursor.execute(sql_query)
        except sqlite3.OperationalError as exception:
            raise errors.BackendError(exception)

        for row in cursor:
            values = {}
            for column_index, column_name in enumerate(column_names):
                values[column_name] = row[column_index]
            yield values

    def Close(self):
        """Closes the database file.

        Raises:
          OSError: if the database is not opened.
        """
        if not self._connection:
            raise OSError("Cannot close database not opened.")

        # We need to run commit or not all data is stored in the database.
        self._connection.commit()
        self._connection.close()

        self._connection = None
        self._cursor = None
        self.filename = None
        self.read_only = None

    def CreateTable(self, table_name, column_definitions):
        """Creates a table.

        Args:
          table_name (str): table name.
          column_definitions (list[str]): column definitions.

        Raises:
          BackendError: if the database back-end raises an exception.
          OSError: if the database is not opened or
              if the database is in read-only mode.
        """
        if not self._connection:
            raise OSError("Cannot create table database not opened.")

        if self.read_only:
            raise OSError("Cannot create table database in read-only mode.")

        column_definitions = ", ".join(column_definitions)

        try:
            self._cursor.execute(
                f"CREATE TABLE {table_name:s} ( {column_definitions:s} )"
            )
        except sqlite3.OperationalError as exception:
            raise errors.BackendError(exception)

    def GetValues(self, table_names, column_names, condition):
        """Retrieves values from a table.

        Args:
          table_names (list[str]): table names.
          column_names (list[str]): column names.
          condition (str): condition.

        Returns:
          generator: values generator.

        Raises:
          OSError: if the database is not opened.
        """
        if not self._connection:
            raise OSError("Cannot retrieve values database not opened.")

        cursor = self._connection.cursor()
        return self._GetValues(cursor, table_names, column_names, condition)

    def HasTable(self, table_name):
        """Determines if a specific table exists.

        Args:
          table_name (str): table name.

        Returns:
          bool: True if the table exists, false otherwise.

        Raises:
          BackendError: if the database back-end raises an exception.
          OSError: if the database is not opened.
        """
        if not self._connection:
            raise OSError("Cannot determine if table exists database not opened.")

        sql_query = self._HAS_TABLE_QUERY.format(table_name)

        try:
            self._cursor.execute(sql_query)

            has_table = bool(self._cursor.fetchone())

        except sqlite3.OperationalError as exception:
            raise errors.BackendError(exception)

        return has_table

    def InsertValues(self, table_name, column_names, values):
        """Inserts values into a table.

        Args:
          table_name (str): table name.
          column_names (list[str]): column names.
          values (list[str]): values formatted as a string.

        Raises:
          BackendError: if the database back-end raises an exception.
          OSError: if the database is not opened or
              if the database is in read-only mode or
              if an unsupported value type is encountered.
        """
        if not self._connection:
            raise OSError("Cannot insert values database not opened.")

        if self.read_only:
            raise OSError("Cannot insert values database in read-only mode.")

        if not values:
            return

        sql_values = []
        for value in values:
            # TODO: handle bool.
            if isinstance(value, str):
                # In sqlite3 the double quote is escaped with a second double quote.
                value = re.sub('"', '""', value)
                value = f'"{value:s}"'
            elif isinstance(value, int):
                value = f"{value:d}"
            elif isinstance(value, float):
                value = f"{value:f}"
            elif value is None:
                value = "NULL"
            else:
                value_type = type(value)
                raise OSError(f"Unsupported value type: {value_type!s}.")
            sql_values.append(value)

        column_names = ", ".join(column_names)
        sql_values = ", ".join(sql_values)

        try:
            self._cursor.execute(
                f"INSERT INTO {table_name:s} ( {column_names:s} ) "
                f"VALUES ( {sql_values:s} )"
            )
        except sqlite3.OperationalError as exception:
            raise errors.BackendError(exception)

    def Open(self, filename, read_only=False):
        """Opens the database file.

        Args:
          filename (str): filename of the database.
          read_only (Optional[bool]): True if the database should be opened in
              read-only mode. Since sqlite3 does not support a real read-only
              mode we fake it by only permitting SELECT queries.

        Returns:
          bool: True if successful or False if not.

        Raises:
          BackendError: if the database back-end raises an exception.
          OSError: if the database is already opened.
        """
        if self._connection:
            raise OSError("Cannot open database already opened.")

        self.filename = filename
        self.read_only = read_only

        self._connection = sqlite3.connect(filename)
        if not self._connection:
            return False

        try:
            self._cursor = self._connection.cursor()
        except sqlite3.OperationalError as exception:
            raise errors.BackendError(exception)

        if not self._cursor:
            return False

        return True


class ResourcesSQLite3DatabaseReader:
    """Event Log resources SQLite database reader."""

    def __init__(self):
        """Initializes the database reader."""
        super().__init__()
        self._database_file = SQLite3DatabaseFile()

    def _GetEventLogProviderKey(self, log_source):
        """Retrieves the Event Log provider key.

        Args:
          log_source (str): Event Log source.

        Returns:
          int: an Event Log provider key or None if not available.

        Raises:
          OSError: if more than one value is found in the database.
        """
        table_names = ["event_log_providers"]
        column_names = ["event_log_provider_key"]
        condition = f'log_source == "{log_source:s}"'

        values_list = list(
            self._database_file.GetValues(table_names, column_names, condition)
        )

        number_of_values = len(values_list)
        if number_of_values == 0:
            return None

        if number_of_values == 1:
            values = values_list[0]
            return values["event_log_provider_key"]

        raise OSError("More than one value found in database.")

    def _GetMessage(self, message_file_key, lcid, message_identifier):
        """Retrieves a specific message from a specific message table.

        Args:
          message_file_key (int): message file key.
          lcid (int): language code identifier (LCID).
          message_identifier (int): message identifier.

        Returns:
          str: the message string or None if not available.

        Raises:
          OSError: if more than one value is found in the database.
        """
        table_name = f"message_table_{message_file_key:d}_0x{lcid:08x}"

        has_table = self._database_file.HasTable(table_name)
        if not has_table:
            return None

        column_names = ["message_string"]
        condition = f'message_identifier == "0x{message_identifier:08x}"'

        values = list(
            self._database_file.GetValues([table_name], column_names, condition)
        )

        number_of_values = len(values)
        if number_of_values == 0:
            return None

        if number_of_values == 1:
            return values[0]["message_string"]

        raise OSError("More than one value found in database.")

    def _GetMessageFileKeys(self, event_log_provider_key):
        """Retrieves the message file keys.

        Args:
          event_log_provider_key (int): the Event Log provider key.

        Yields:
          int: a message file key.
        """
        table_names = ["message_file_per_event_log_provider"]
        column_names = ["message_file_key"]
        condition = f"event_log_provider_key == {event_log_provider_key:d}"

        generator = self._database_file.GetValues(table_names, column_names, condition)

        # pylint: disable=not-an-iterable
        for values in generator:
            yield values["message_file_key"]

    def _GetMessageFilenames(self, log_source, message_file_type):
        """Retrieves the message filenames of a specific Event Log provider.

        Args:
          log_source (str): Event Log source.
          message_file_type (str): message file type.

        Returns:
          list[str]: message filenames.
        """
        table_names = [
            "event_log_providers",
            "message_file_per_event_log_provider",
            "message_files",
        ]
        column_names = ["message_files.path"]
        condition = " AND ".join(
            [
                f'event_log_providers.log_source == "{log_source:s}"',
                (
                    f"message_file_per_event_log_provider.message_file_type == "
                    f'"{message_file_type:s}"'
                ),
                (
                    "event_log_providers.event_log_provider_key == "
                    "message_file_per_event_log_provider.event_log_provider_key"
                ),
                (
                    "message_file_per_event_log_provider.message_file_key == "
                    "message_files.message_file_key"
                ),
            ]
        )

        message_filenames = []
        for values in self._database_file.GetValues(
            table_names, column_names, condition
        ):
            message_filename = values["message_files.path"]
            message_filenames.append(message_filename)

        return message_filenames

    def _GetMessages(self, message_file_key, lcid):
        """Retrieves the messages of a specific message table.

        Args:
          message_file_key (int): message file key.
          lcid (int): language code identifier (LCID).

        Yields:
          tuple[int, str]: message identifier and message string.
        """
        table_name = f"message_table_{message_file_key:d}_0x{lcid:08x}"

        has_table = self._database_file.HasTable(table_name)
        if has_table:
            column_names = ["message_identifier", "message_string"]
            condition = ""

            for values in self._database_file.GetValues(
                [table_name], column_names, condition
            ):
                yield values["message_identifier"], values["message_string"]

    def Close(self):
        """Closes the database reader."""
        self._database_file.Close()

    def GetEventLogProviders(self):
        """Retrieves the Event Log providers.

        Yields:
          EventLogProvider: an Event Log provider.
        """
        table_names = ["event_log_providers"]
        column_names = ["log_source", "provider_guid"]
        condition = ""

        event_log_providers = []
        for values in self._database_file.GetValues(
            table_names, column_names, condition
        ):
            event_log_provider = resources.WinevtResourcesEventLogProvider()
            event_log_provider.identifier = values["provider_guid"]

            event_log_provider.log_sources.append(values["log_source"])

            event_log_providers.append(event_log_provider)

        for event_log_provider in event_log_providers:
            message_filenames = self._GetMessageFilenames(
                event_log_provider.log_source, definitions.MESSAGE_FILE_TYPE_CATEGORY
            )
            event_log_provider.SetCategoryMessageFilenames(message_filenames)

            message_filenames = self._GetMessageFilenames(
                event_log_provider.log_source, definitions.MESSAGE_FILE_TYPE_EVENT
            )
            event_log_provider.SetEventMessageFilenames(message_filenames)

            message_filenames = self._GetMessageFilenames(
                event_log_provider.log_source, definitions.MESSAGE_FILE_TYPE_PARAMETER
            )
            event_log_provider.SetParameterMessageFilenames(message_filenames)

            yield event_log_provider

    def GetMessage(self, log_source, lcid, message_identifier):
        """Retrieves a specific message for a specific Event Log source.

        Args:
          log_source (str): Event Log source.
          lcid (int): language code identifier (LCID).
          message_identifier (int): message identifier.

        Returns:
          str: the message string or None if not available.
        """
        event_log_provider_key = self._GetEventLogProviderKey(log_source)
        if not event_log_provider_key:
            return None

        generator = self._GetMessageFileKeys(event_log_provider_key)
        if not generator:
            return None

        message_string = None
        for message_file_key in generator:
            message_string = self._GetMessage(
                message_file_key, lcid, message_identifier
            )

            if message_string:
                break

        return message_string

    def GetMessages(self, log_source, lcid):
        """Retrieves the messages of a specific Event Log source.

        Args:
          log_source (str): Event Log source.
          lcid (int): language code identifier (LCID).

        Yields:
          tuple[int, str]: message identifier and message string.
        """
        event_log_provider_key = self._GetEventLogProviderKey(log_source)
        if event_log_provider_key:
            for message_file_key in self._GetMessageFileKeys(event_log_provider_key):
                for message_identifier, message_string in self._GetMessages(
                    message_file_key, lcid
                ):
                    yield message_identifier, message_string

    def GetMetadataAttribute(self, attribute_name):
        """Retrieves the metadata attribute.

        Args:
          attribute_name (str): name of the metadata attribute.

        Returns:
          str: value of the metadata attribute or None.

        Raises:
          OSError: if more than one value is found in the database.
        """
        table_name = "metadata"

        has_table = self._database_file.HasTable(table_name)
        if not has_table:
            return None

        column_names = ["value"]
        condition = f'name == "{attribute_name:s}"'

        values = list(
            self._database_file.GetValues([table_name], column_names, condition)
        )

        number_of_values = len(values)
        if number_of_values == 0:
            return None

        if number_of_values == 1:
            return values[0]["value"]

        raise OSError("More than one value found in database.")

    def Open(self, filename):
        """Opens the database reader.

        Args:
          filename (str): filename of the database.

        Returns:
          bool: True if successful or False if not.
        """
        return self._database_file.Open(filename, read_only=True)

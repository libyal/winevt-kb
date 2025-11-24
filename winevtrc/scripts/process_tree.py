#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script to represent process start and stop events as a process tree."""

import argparse
import logging
import os
import sys

from xml.etree import ElementTree

import pyevt
import pyevtx


class EventLogRecord(object):
  """An EventLog record.

  Attributes:
    event_identifier (int): event identifier.
    strings (list[str]): string values.
  """

  def __init__(self):
    """Initializes an EventLog record."""
    super(EventLogRecord, self).__init__()
    self.event_identifier = None
    self.strings = []

  def GetStringValue(self, string_index):
    """Retrieves a specific string value.

    Args:
      string_index (int): string index

    Return:
      str: string value.
    """
    return self.strings[string_index]


class Process(object):
  """Class to represent a process.

  Attributes:
    TODO
  """

  def __init__(self):
    """Initializes an process start event."""
    super(Process, self).__init__()
    self.process_identifier = None
    self.process_name = None
    self.start_time = None
    self.stop_time = None


class ProcessStartEvent(object):
  """Class to represent a process start event.

  Attributes:
    TODO
  """

  def __init__(self):
    """Initializes an process start event."""
    super(ProcessStartEvent, self).__init__()
    self.command_line = None
    self.new_process_id = None
    self.new_process_name = None
    self.process_id = None
    self.subject_domain_name = None
    self.subject_logon_id = None
    self.subject_user_name = None
    self.subject_user_sid = None
    self.token_elevation_type = None
    self.written_time = None


class ProcessStopEvent(object):
  """Class to represent a process stop event.

  Attributes:
    TODO
  """

  def __init__(self):
    """Initializes an process stop event."""
    super(ProcessStopEvent, self).__init__()
    self.process_id = None
    self.process_name = None
    self.status = None
    self.subject_domain_name = None
    self.subject_logon_id = None
    self.subject_user_name = None
    self.subject_user_sid = None
    self.written_time = None


class ProcessTree(object):
  """Class to represent process start and stop events as a process tree.

  event identifiers: 592, 593
  """

  def _ReadEVT(self, source):
    """Read an EventLog file.

    Args:
      source (str): name of the EventLog file that contains the process start
          and stop events.

    Yields:
      pyevt.record: EventLog record.
    """
    evt_file = pyevt.file()
    evt_file.open(source)

    try:
      yield from iter(evt_file.records)

    finally:
      evt_file.close()

  def _ReadEVTX(self, source):
    """Read a XML EventLog file.

    Args:
      source (str): name of the EventLog file that contains the process start
          and stop events.

    Yields:
      pyevtx.record: XML EventLog record.
    """
    evtx_file = pyevtx.file()
    evtx_file.open(source)

    # pylint: disable=not-an-iterable
    for evtx_record in evtx_file.records:
      if evtx_record.event_identifier == 4688:
        process_start_event = ProcessStartEvent()
        process_start_event.command_line = evtx_record.get_string(8)

        try:
          string_value = evtx_record.get_string(4)
          process_start_event.new_process_id = int(string_value, 16)
        except ValueError:
          pass

        process_start_event.new_process_name = evtx_record.get_string(5)

        try:
          string_value = evtx_record.get_string(7)
          process_start_event.process_id = int(string_value, 16)
        except ValueError:
          pass

        process_start_event.subject_domain_name = evtx_record.get_string(2)
        process_start_event.subject_logon_id = evtx_record.get_string(3)
        process_start_event.subject_user_name = evtx_record.get_string(1)
        process_start_event.subject_user_sid = evtx_record.get_string(0)
        process_start_event.token_elevation_type = evtx_record.get_string(6)
        process_start_event.written_time = evtx_record.written_time

        yield process_start_event

      elif evtx_record.event_identifier == 4689:
        process_stop_event = ProcessStopEvent()

        try:
          string_value = evtx_record.get_string(5)
          process_stop_event.process_id = int(string_value, 16)
        except ValueError:
          pass

        process_stop_event.process_name = evtx_record.get_string(6)
        process_stop_event.status = evtx_record.get_string(4)
        process_stop_event.subject_domain_name = evtx_record.get_string(2)
        process_stop_event.subject_logon_id = evtx_record.get_string(3)
        process_stop_event.subject_user_name = evtx_record.get_string(1)
        process_stop_event.subject_user_sid = evtx_record.get_string(0)
        process_stop_event.written_time = evtx_record.written_time

        yield process_stop_event

    evtx_file.close()

  def _ReadXML(self, source):
    """Read an export of the EventLog messages in XML.

    Args:
      source (str): name of the EventLog file that contains the process start
          and stop events.

    Yields:
      EventLogRecord: EventLog record.
    """
    with open(source, 'r', encoding='utf-8') as file_object:
      for line_index, line in enumerate(file_object.readlines()):
        line = line.strip()

        try:
          xml = ElementTree.fromstring(line)
        except ElementTree.ParseError:
          logging.error(f'Unable to parse line: {line_index:d} "{line:s}"')
          continue

        xml_system = xml.find(
            '{http://schemas.microsoft.com/win/2004/08/events/event}System')
        xml_event_id = xml_system.find(
            '{http://schemas.microsoft.com/win/2004/08/events/event}EventID')
        xml_event_data = xml.find(
            '{http://schemas.microsoft.com/win/2004/08/events/event}EventData')

        event_log_record = EventLogRecord()

        try:
          event_log_record.event_identifier = int(xml_event_id.text, 10)
        except ValueError:
          continue

        for xml_data in xml_event_data:
          event_log_record.strings.append(xml_data.text)

        yield event_log_record

  def Generate(self, source):
    """Generates a process tree from the source.

    Args:
      source (str): name of the EventLog file that contains the process start
          and stop events.
    """
    if pyevt.check_file_signature(source):
      record_generator = self._ReadEVT
    elif pyevtx.check_file_signature(source):
      record_generator = self._ReadEVTX
    else:
      record_generator = self._ReadXML

    active_processes = {}
    for process_event in record_generator(source):
      if isinstance(process_event, ProcessStartEvent):
        print((f'Process started: (PID: {process_event.new_process_id:d}, '
               f'PPID: {process_event.process_id:d}) '
               f'{process_event.new_process_name:s} '
               f'{process_event.command_line:s}'))

      elif isinstance(process_event, ProcessStopEvent):
        active_process = active_processes.get(
            process_event.process_id, None)

        if active_process:
          active_process.stop_time = process_event.written_time

        print((f'Process stopped: (PID: {process_event.process_id:d}) '
               f'{process_event.process_name:s}'))

  def Output(self, source):
    """Outputs a process tree.

    Args:
      source (str): name of the EventLog file that contains the process start
          and stop events.
    """
    # TODO: implement.


class StdoutOutputWriter(object):
  """Class that defines a stdout output writer."""

  def Open(self):
    """Opens the file.

    Returns:
      bool: True if successful or False if not.
    """
    return True

  def Close(self):
    """Closes the file."""


def Main():
  """Entry point of console script to represent events a process tree.

  Returns:
    int: exit code that is provided to sys.exit().
  """
  args_parser = argparse.ArgumentParser(description=(
      'Represents process start and stop events as a process tree.'))

  args_parser.add_argument(
      'source', nargs='?', action='store', metavar='EVENT_LOG',
      default=None, help=(
          'EventLog file that contains the start and stop events.'))

  options = args_parser.parse_args()

  if not options.source:
    print('Source value is missing.')
    print('')
    args_parser.print_help()
    print('')
    return 1

  if not os.path.isfile(options.source):
    print('Invalid source.')
    print('')
    return 1

  logging.basicConfig(
      level=logging.INFO, format='[%(levelname)s] %(message)s')

  output_writer = StdoutOutputWriter()

  if not output_writer.Open():
    print('Unable to open output writer.')
    print('')
    return 1

  process_tree = ProcessTree()
  process_tree.Generate(options.source)

  process_tree.Output(output_writer)

  output_writer.Close()

  return 0


if __name__ == '__main__':
  sys.exit(Main())

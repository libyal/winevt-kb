# -*- coding: utf-8 -*-
"""The error objects."""

from __future__ import unicode_literals


class Error(Exception):
  """The error interface."""


class BackendError(Error):
  """Error that is raised for database back-end exceptions."""

# -*- coding: utf-8 -*-
"""The error objects."""


class Error(Exception):
  """The error interface."""


class BackendError(Error):
  """Error that is raised for database back-end exceptions."""

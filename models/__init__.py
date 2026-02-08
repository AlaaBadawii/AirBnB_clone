#!/usr/bin/python3
"""models package init file at models/__init__.py"""

from .engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
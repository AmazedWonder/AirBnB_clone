#!/usr/bin/python3
"""Initialize packages"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

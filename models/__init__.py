#!/usr/bin/env python3
"""init file for File storage"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

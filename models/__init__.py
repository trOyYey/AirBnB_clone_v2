#!/usr/bin/python3
"""module to Distinguish which storage engine to use"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

if 'db' == getenv("HBNB_TYPE_STORAGE"):
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()

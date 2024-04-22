#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, DATETIME, String
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
import models

if getenv("HBNB_TYPE_STORAGE") == 'db':
    Base = declarative_base()
else:
    Base = object

class BaseModel:
    """A base class for all hbnb models"""

    if 'db' == getenv("HBNB_TYPE_STORAGE"):
        __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'latin1'}
    id = Column(String(60), primary_key=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.utcnow())
    updated_at = Column(DATETIME, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            time_f = "%Y-%m-%dT%H:%M:%S.%f"
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                         time_f)
            else:
                self.updated_at = datetime.now()
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                         time_f)
            else:
                self.created_at = datetime.now()
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            for key in kwargs:
                if "__class__" != key:
                    setattr(self, key, kwargs[key])

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        dictt = self.__dict__.copy()
        if "_sa_instance_state" in dictt:
            del dictt["_sa_instance_state"]
        return '[{}] ({}) {}'.format(cls, self.id, dictt)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictt = {}
        dictt.update(self.__dict__)
        dictt.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictt['created_at'] = self.created_at.isoformat()
        dictt['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictt:
            del dictt["_sa_instance_state"]
        return dictt

    def delete(self):
        from models import storage
        """ deletes the instance"""
        models.storage.delete(self)

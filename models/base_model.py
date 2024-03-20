#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime

class BaseModel:
    """A base class for all hbnb models"""
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
        dic = self.__dict__.copy()
        if "_sa_instance_state" in dic:
            del dic["_sa_instance_state"]
        return f'[{cls}] ({self.id}) {dic}'

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

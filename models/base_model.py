#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage

""" baseModel """


class BaseModel:
    """ defines common attributes and methods for inheriting classes """

    def __init__(self, *args, **kwargs):
        """ initialize an instance potentially with a dictionary argument"""

        if "id" in kwargs:
            self.id = kwargs["id"]
        else:
            self.id = str(uuid.uuid4())

        if "created_at" in kwargs:
            x = kwargs["created_at"]
            self.created_at = datetime.strptime(x, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.created_at = datetime.now()

        if "updated_at" in kwargs:
            x = kwargs["updated_at"]
            self.updated_at = datetime.strptime(x, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.updated_at = datetime.now()
        if not kwargs or len(kwargs) == 0:
            storage.new(self)

    def __str__(self):
        """ overwrite string special method """
        r = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return r

    def save(self):
        """ update updated_at with current time """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ return a dict with a key/values of __dict__ of the instance """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['created_at'] = self.created_at.isoformat()
        return new_dict


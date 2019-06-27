#!/usr/bin/python3
import uuid
from datetime import datetime
""" baseModel """


class BaseModel:
    """ defines common attributes and methods for inheriting classes """

    def __init__(self):
        """ initialize an instance """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ overwrite string special method """
        r = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return r

    def save(self):
        """ update updated_at with current time """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ return a dict with a key/values of __dict__ of the instance """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['created_at'] = self.created_at.isoformat()
        return new_dict

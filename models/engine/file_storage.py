#!/usr/bin/python3
import json
from os import path
from models.base_model import BaseModel
from models.user import User


class FileStorage:

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets obj with id value """
        className = type(obj).__name__
        key = className + '.' + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes object """
        with open(self.__file_path, 'w') as myFile:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()},
                      myFile)

    def reload(self):
        """ deserializes a json file """
        try:
            with open('file.json') as myFile:
                f = json.load(myFile)
            for k, v in f.items():
                if "BaseModel" in k:
                    self.__objects[k] = BaseModel(**v)
                elif "User" in k:
                    self.__objects[k] = User(**v)
        except:
            pass

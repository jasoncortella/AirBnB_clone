#!/usr/bin/python3
import json
from os import path

class FileStorage:

    __file_path = '/home/vagrant/AirBnB_clone/file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self,obj):
        """ sets obj with id value """
        className = type(obj).__name__
        key = className + '.' + str(obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """ serializes object """
        with open(self.__file_path, 'w') as myFile:
            json.dump(self.__objects, myFile)

    def reload(self):
        """ deserializes a json file """
        if path.exists(self.__file_path):
            with open(self.__file_path) as myFile:
                return json.load(myFile)

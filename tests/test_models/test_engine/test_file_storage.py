#!/usr/bin/python3
""" unittest for file_storage class """


import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from datetime import datetime
from time import sleep
import models
import os

class test_file_storage_instantiation(unittest.TestCase):
    """ define unit test for testing file storage instantiation tests """

    def test_filestorage_instantiation(self):
        a = FileStorage()
        self.assertIsInstance(a, FileStorage)

    def test_filestorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            a = FileStorage("arg")

    def test_filestorage_file_path_private(self):
        a = FileStorage()
        with self.assertRaises(AttributeError):
            a.file_path

    def test_filestorage_objects_private(self):
        a = FileStorage()
        with self.assertRaises(AttributeError):
            a.objects


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
""" unittest for base_amenity class """


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime
from time import sleep
import models
import os

class test_amenity_class_instantiation(unittest.TestCase):
    """ define unittest for testing the id instance attribute """

    def test_amenity_class_instantiation(self):
        a = Amenity()
        self.assertIsInstance(a, Amenity)

    def test_amenity_inherits(self):
        a = Amenity()
        self.assertIsInstance(a, BaseModel)


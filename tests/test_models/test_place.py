#!/usr/bin/python3
""" unittest for place class """


import unittest
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime
from time import sleep
import models
import os

class test_place_class_instantiation(unittest.TestCase):
    """ define unittest for testing the id instance attribute """

    def test_place_class_instantiation(self):
        a = Place()
        self.assertIsInstance(a, Place)

    def test_place_inherits(self):
        a = Place()
        self.assertIsInstance(a, BaseModel)


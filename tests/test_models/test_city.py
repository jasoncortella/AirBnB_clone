#!/usr/bin/python3
""" unittest for base_model class """


import unittest
from models.base_model import BaseModel
from models.city import City
from datetime import datetime
from time import sleep
import models
import os

class test_city_instantiation(unittest.TestCase):
    """ define unittest for testing the City instance """

    def test_city_instantiation(self):
        a = City()
        self.assertIsInstance(a, City)

    def test_city_inherits(self):
        a = City()
        self.assertIsInstance(a, BaseModel)


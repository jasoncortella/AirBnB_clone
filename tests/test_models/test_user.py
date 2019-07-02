#!/usr/bin/python3
""" unittest for base_model class """


import unittest
from models.base_model import BaseModel
from models.user import User
from datetime import datetime
from time import sleep
import models
import os

class test_user_instantiation(unittest.TestCase):
    """ define unittest for testing the instance attribute """

    def test_user_instantiation(self):
        a = User()
        self.assertIsInstance(a, User)

    def test_user_inherits(self):
        a = User()
        self.assertIsInstance(a, User)


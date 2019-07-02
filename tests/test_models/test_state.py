#!/usr/bin/python3
""" unittest for base_model class """


import unittest
from models.base_model import BaseModel
from models.state import State
from datetime import datetime
from time import sleep
import models
import os

class test_state_instantiation(unittest.TestCase):
    """ define unittest for testing the state instance """

    def test_state_instantiation(self):
        a = State()
        self.assertIsInstance(a, State)

    def test_state_inherits(self):
        a = State()
        self.assertIsInstance(a, BaseModel)


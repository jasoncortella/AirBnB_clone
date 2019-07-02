#!/usr/bin/python3
""" unittest for review class """


import unittest
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime
from time import sleep
import models
import os

class test_review_class_instantiation(unittest.TestCase):
    """ define unittest for testing the id instance attribute """

    def test_review_class_instantiation(self):
        a = Review()
        self.assertIsInstance(a, Review)

    def test_review_inherits(self):
        a = Review()
        self.assertIsInstance(a, BaseModel)


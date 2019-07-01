#!/usr/bin/python3
""" unittest for base_model class """


import unittest
from models.base_model import BaseModel
from datetime import datetime

class test_base_model_instantiation(unittest.TestCase):
    """ define unittest for testing the id instance attribute """

    def test_base_model_instantiation(self):
        a = BaseModel()
        self.assertIsInstance(a, BaseModel)

class test_base_model_id(unittest.TestCase):
    """ define unittest for testing the id instance attribute """

    def test_base_model_id_noarg(self):
        a = BaseModel()
        self.assertGreater(len(a.id), 0)

    def test_base_model_id_length_noarg(self):
        a = BaseModel()
        self.assertEqual(len(a.id), 36)

    def test_base_model_id_dash_noarg(self):
        a = BaseModel()
        self.assertEqual(a.id.count('-'), 4)

    def test_base_model_id_type_noarg(self):
        a = BaseModel()
        self.assertEqual(type(a.id), str)

    def test_base_model_unique_id_noarg(self):
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)

    def test_base_model_id_arg(self):
        a = BaseModel(id='abc123')
        self.assertEqual(a.id, 'abc123')

    def test_base_model_id_list_arg(self):
        a = BaseModel(id=[1, 2])
        self.assertEqual(a.id, [1, 2])

    def test_base_model_non_unique_id(self):
        a = BaseModel(id=123)
        b = BaseModel(id=123)
        self.assertNotEqual(a.created_at, b.created_at)


class test_base_model_created_at(unittest.TestCase):
    """ define unittest for testing the id instance attribute """

    def test_created_at_instantiation(self):
        a = BaseModel()
        self.assertIsInstance(a.created_at, datetime)

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
""" unittest for base_model class """


import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class test_base_model_instantiation(unittest.TestCase):
    """ define unittest for testing the id instance attribute """

    def test_base_model_instantiation(self):
        a = BaseModel()
        self.assertIsInstance(a, BaseModel)

    def test_base_model_instantiation_none_arg(self):
        a = BaseModel(None)
        self.assertIsInstance(a, BaseModel)

    def test_base_model_change_id(self):
        a = BaseModel()
        a.id = 10
        self.assertEqual(a.id, 10)

    def test_base_model_change_created_at(self):
        a = BaseModel()
        a.created_at = 10
        self.assertEqual(a.created_at, 10)

    def test_base_model_change_updated_at(self):
        a = BaseModel()
        a.updated_at = 10
        self.assertEqual(a.updated_at, 10)

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
        sleep(.001)
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

    def test_base_model_extra_kwargs(self):
        a= BaseModel(id=12345, name="hello")
        self.assertEqual(a.id, 12345)
        self.assertEqual(a.name, "hello")

class test_base_model_created_at_updated_at(unittest.TestCase):
    """ define unittest for testing the id instance attribute """

    def test_created_at_instantiation(self):
        a = BaseModel()
        self.assertIsInstance(a.created_at, datetime)

    def test_updated_at_instantiation(self):
        a = BaseModel()
        self.assertIsInstance(a.updated_at, datetime)

    def test_compare_updated_and_created(self):
        a = BaseModel()
        self.assertNotEqual(a.created_at, a.updated_at)

    def test_caua_save_create(self):
        a = BaseModel()
        create = a.created_at
        a.save()
        self.assertEqual(create, a.created_at)

    def test_caua_save_update(self):
        a = BaseModel()
        update = a.updated_at
        a.save()
        self.assertNotEqual(update, a.updated_at)

    def test_caua_save_id(self):
        a = BaseModel()
        ident = a.id
        a.save()
        self.assertEqual(ident, a.id)

class test_base_model_str_method(unittest.TestCase):
    """ define unittest for testing the __str__ method """

    def test_str(self):
        a = BaseModel()
        b= "[{}] ({}) {}".format(a.__class__.__name__, a.id, a.__dict__)
        self.assertEqual(str(a), b)



if __name__ == '__main__':
    unittest.main()

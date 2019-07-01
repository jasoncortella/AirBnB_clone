#!/usr/bin/python3
""" unittest for base_model class """


import unittest
from models.base_model import BaseModel

class test_base_model_instantiation(unittest.TestCase):
    """ define unit test for testing instantiaion for base model class """

    def test_base_model_no_args(self):
        a = BaseModel()
        self.assertGreater(len(a.id), 0)


if __name__ == '__main__':
    unittest.main()

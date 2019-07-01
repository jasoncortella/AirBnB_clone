#!/usr/bin/python3
""" unittest for file_storage class """


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class test_first_file_storage(unittest.TestCase):
    """ define unit test for testing file storage tests """

    def test_file_storage_no_args(self):
        a = BaseModel()
        self.assertGreater(len(a.id), 0)


if __name__ == '__main__':
    unittest.main()

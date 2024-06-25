#!/usr/bin/python3
"""Test module fro BaseModel class"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime, timedelta
from models import storage
import unittest
import os
import time


class TestBaseModel(unittest.TestCase):
    """Class to test BaseModel class"""

    def test_attributes(self):
        """Method to test BaseModel class attributes"""
        b = BaseModel()
        self.assertIsInstance(b.id, str)
        self.assertIsInstance(b.created_at, datetime)
        self.assertIsInstance(b.updated_at, datetime)

    # =======================================================

    def test_kwargs(self):
        """Method to test creation of BaseModel instance using kwargs"""
        b1 = BaseModel()
        dic = b1.to_dict()
        b2 = BaseModel(**dic)
        self.assertIsInstance(b2, BaseModel)
        self.assertIsInstance(b2.updated_at, datetime)
        self.assertIsInstance(b2.created_at, datetime)

    # =======================================================

    def test_str(self):
        """Method to test BaseModel's str method"""
        b = BaseModel()
        st = b.__str__()
        out = "[{}] ({}) {}".format(b.__class__.__name__, b.id, b.__dict__)
        self.assertIsInstance(st, str)
        self.assertEqual(out, st)

    # =======================================================

    def test_save(self):
        """Method to test BaseModel's save method"""
        b = BaseModel()
        time.sleep(0.001)
        b.save()
        val1 = datetime.now()
        self.assertIsInstance(b.updated_at, datetime)
        self.assertGreaterEqual(b.updated_at, val1 - timedelta(milliseconds=1))
        self.assertLessEqual(b.updated_at, val1 + timedelta(milliseconds=1))
        key = "{}.{}".format(b.__class__.__name__, b.id)
        objs = storage.all()
        self.assertIn(key, objs)

    # =======================================================

    def test_to_dict(self):
        """Method to test BaseModel's to_dict method"""
        b = BaseModel()
        dic = b.to_dict()
        self.assertIsInstance(dic, dict)
        self.assertIsInstance(dic['updated_at'], str)
        self.assertIsInstance(dic['created_at'], str)

    # =======================================================

    def test_new(self):
        """Method to test new method"""
        b = BaseModel()
        key = "{}.{}".format(b.__class__.__name__, b.id)
        dic = storage.all()
        self.assertIn(key, dic)


if __name__ == '__main__':
    unittest.main()

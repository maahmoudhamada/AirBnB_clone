#!/usr/bin/python3
"""Test module fro BaseModel class"""

from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """Class to test BaseModel class"""

    def test_attributes(self):
        """Method to test BaseModel class attributes"""
        b = BaseModel()
        self.assertIsInstance(b.id, str)
        self.assertIsInstance(b.created_at, datetime)
        self.assertIsInstance(b.updated_at, datetime)

    def test_str(self):
        """Method to test BaseModel's str method"""
        b = BaseModel()
        st = b.__str__()
        out = "[{}] ({}) {}".format(b.__class__.__name__, b.id, b.__dict__)
        self.assertIsInstance(st, str)
        self.assertEqual(out, st)

    def test_save(self):
        """Method to test BaseModel's save method"""
        b = BaseModel()
        b.save()
        val1 = datetime.now()
        self.assertIsInstance(b.updated_at, datetime)
        self.asseertEqual(b.updated_at, val1)

    def test_to_dict(self):
        """Method to test BaseModel's to_dict method"""
        b = BaseModel()
        dic = b.to_dict()
        self.assertIsInstance(dic, dict)
        self.assertIsInstance(dic['updated_at'], str)
        self.assertIsInstance(dic['created_at'], str)

#!/usr/bin/python3
"""The Test module for FileStorage class"""


import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class FileStorageTests(unittest.TestCase):
    """Test class to test FileStorage Class"""

    def setUp(self):
        """Setup Method"""
        self.s = FileStorage()
        self.s._FileStorage__objects = {}
        try:
            os.remove(self.s._FileStorage__file_path)
        except FileNotFoundError:
            pass

    # =======================================================

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove(self.s._FileStorage__file_path)
        except FileNotFoundError:
            pass

    # =======================================================

    def test_attributes(self):
        """Test method for class attributes"""
        self.assertIsInstance(self.s._FileStorage__file_path, str)
        self.assertIsInstance(self.s._FileStorage__objects, dict)

    # =======================================================

    def test_all(self):
        """Test method for FileStorage's all() method"""
        self.assertIsInstance(self.s.all(), dict)
        self.assertEqual(self.s.all(), {})

    # =======================================================

    def test_new(self):
        """Test method for FileStorage's new() method"""
        b = BaseModel()
        self.s.new(b)
        key = "{}.{}".format(b.__class__.__name__, b.id)
        self.assertIsInstance(self.s.all()[key], BaseModel)
        self.assertEqual(self.s.all()[key], b)
        self.assertIn(key, self.s.all())

    # =======================================================

    def test_save(self):
        """Test method for FileStorage's save() method"""
        b = BaseModel()
        self.s.new(b)
        self.s.save()
        with open(self.s._FileStorage__file_path, "r", encoding="utf-8") as f:
            val = json.load(f)
        key = "{}.{}".format(b.__class__.__name__, b.id)
        self.assertIn(key, val)
        self.assertEqual(val[key]["__class__"], "BaseModel")
        self.assertEqual(val[key]["id"], b.id)

    # =======================================================

    def test_reload(self):
        """Test method for FileStorage's reload() method"""
        b = BaseModel()
        self.s.new(b)
        self.s.save()

        self.s._FileStorage__objects = {}
        self.s.reload()
        key = "{}.{}".format(b.__class__.__name__, b.id)
        self.assertIn(key, self.s.all())
        self.assertIsInstance(self.s.all()[key], BaseModel)
        self.assertEqual(self.s.all()[key].id, b.id)


if __name__ == "__main__":
    unittest.main()

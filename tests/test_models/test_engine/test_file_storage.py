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
        f = FileStorage()
        f._FileStorage__objects = {}
        try:
            os.remove(f._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_attributes(self):
        """Test method for class attributes"""
        f = FileStorage()
        self.assertIsInstance(f._FileStorage__file_path, str)
        self.assertIsInstance(f._FileStorage__objects, dict)

    def test_all(self):
        """Test method for FileStorage's all() method"""
        f = FileStorage()
        self.assertIsInstance(f.all(), dict)
        self.assertEqual(f.all(), {})

    def test_new(self):
        """Test method for FileStorage's new() method"""
        b = BaseModel()
        f = FileStorage()
        f.new(b)
        key = "{}.{}".format(b.__class__.__name__, b.id)
        self.assertIsInstance(f.all()[key], BaseModel)
        self.assertEqual(f.all()[key], b)
        self.assertIn(key, f.all())

    def test_save(self):
        """Test method for FileStorage's save() method"""
        f = FileStorage()
        f._FileStorage__objects = {}
        f.save()
        with open(f._FileStorage__file_path, "r+", encoding="utf-8") as f:
            val = f.read()
        self.assertEqual(val, '{}')
        self.assertIsInstance(val, str)

    def test_reload(self):
        """Test method for FileStorage's reload() method"""
        f = FileStorage()
        b = BaseModel()
        b.save()
        f.reload()
        key = "{}.{}".format(b.__class__.__name__, b.id)
        self.assertIn(key, f._FileStorage__objects)

        with self.assertRaises(TypeError):
            f.reload('test')

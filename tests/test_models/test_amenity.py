#!/usr/bin/python3
"""Test module for Amenity class"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class AmenityClassTest(unittest.TestCase):
    """Class to test Amenity class"""

    def setUp(self):
        """Setup Method"""
        self.a = Amenity()

    # =======================================================

    def test_initialization(self):
        """Method to test Amenity's class initialize"""
        self.assertIsInstance(self.a, Amenity)
        self.assertTrue(issubclass(type(self.a), BaseModel))

    # =======================================================

    def test_class_attributes(self):
        """Method to test Amenity's class attributes"""
        self.assertIsInstance(self.a.name, str)
        self.assertEqual(self.a.name, "")
        self.a.name = 'ALX'
        self.assertEqual(self.a.name, "ALX")


if __name__ == "__main__":
    unittest.main()

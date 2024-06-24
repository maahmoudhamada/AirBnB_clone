#!/usr/bin/python3
"""Test module for City class"""

import unittest
from models.base_model import BaseModel
from models.city import City


class CityClassTest(unittest.TestCase):
    """Class to test City class"""

    def setUp(self):
        """Setup Method"""
        self.c = City()

    # =======================================================

    def test_initialization(self):
        """Method to test City's class initialize"""
        self.assertIsInstance(self.c, City)
        self.assertTrue(issubclass(type(self.c), BaseModel))

    # =======================================================

    def test_class_attributes(self):
        """Method to test City's class attributes"""
        self.assertIsInstance(self.c.state_id, str)
        self.assertEqual(self.c.state_id, "")
        self.c.state_id = "123"
        self.assertEqual(self.c.state_id, "123")

        # --------------------------------------------

        self.assertIsInstance(self.c.name, str)
        self.assertEqual(self.c.name, "")
        self.c.name = 'ALX'
        self.assertEqual(self.c.name, "ALX")


if __name__ == '__main__':
    unittest.main()

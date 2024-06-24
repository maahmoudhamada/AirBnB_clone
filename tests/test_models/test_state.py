#!/usr/bin/python3
"""Test module for State class"""

import unittest
from models.base_model import BaseModel
from models.state import State


class StateClassTest(unittest.TestCase):
    """Class to test State class"""

    def setUp(self):
        """Setup Method"""
        self.s = State()

    # =======================================================

    def test_initialization(self):
        """Method to test State's class initialize"""
        self.assertIsInstance(self.s, State)
        self.assertTrue(issubclass(type(self.s), BaseModel))

    # =======================================================

    def test_class_attributes(self):
        """Method to test State's class attributes"""
        self.assertIsInstance(self.s.name, str)
        self.assertEqual(self.s.name, "")
        self.s.name = 'ALX'
        self.assertEqual(self.s.name, "ALX")


if __name__ == "__main__":
    unittest.main()

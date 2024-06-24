#!/usr/bin/python3
"""Test module for User class"""

import unittest
from models.base_model import BaseModel
from models.user import User


class UserClassTest(unittest.TestCase):
    """Class to test User class"""

    def setUp(self):
        """Setup Method"""
        self.u = User()

    def test_initialization(self):
        """Method to test User's class initialize"""
        self.assertIsInstance(self.u, User)
        self.assertTrue(issubclass(type(self.u), BaseModel))

    def test_class_attributes(self):
        """Method to test User's class attributes"""
        self.assertIsInstance(self.u.email, str)
        self.assertEqual(self.u.email, "")
        self.u.email = 'alx@se.com'
        self.assertEqual(self.u.email, "alx@se.com")

    # ---------------------------------------------------

        self.assertIsInstance(self.u.password, str)
        self.assertEqual(self.u.password, "")
        self.u.password = "1234"
        self.assertEqual(self.u.password, "1234")

    # ---------------------------------------------------

        self.assertIsInstance(self.u.first_name, str)
        self.assertEqual(self.u.first_name, "")
        self.u.first_name = "Mahmoud"
        self.assertEqual(self.u.first_name, "Mahmoud")

    # ---------------------------------------------------

        self.assertIsInstance(self.u.last_name, str)
        self.assertEqual(self.u.last_name, "")
        self.u.last_name = "Hamada"
        self.assertEqual(self.u.last_name, "Hamada")


if __name__ == "__main__":
    unittest.main()

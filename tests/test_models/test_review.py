#!/usr/bin/python3
"""Test module for Review class"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class ReviewClassTest(unittest.TestCase):
    """Class to test Review class"""

    def setUp(self):
        """Setup Method"""
        self.r = Review()

    # =======================================================

    def test_initialization(self):
        """Method to test Review's class initialize"""
        self.assertIsInstance(self.r, Review)
        self.assertTrue(issubclass(type(self.r), BaseModel))

    # =======================================================

    def test_class_attributes(self):
        """Method to test Review's class attributes"""
        self.assertIsInstance(self.r.place_id, str)
        self.assertEqual(self.r.place_id, "")
        self.r.place_id = '1234'
        self.assertEqual(self.r.place_id, "1234")

    # ---------------------------------------------------

        self.assertIsInstance(self.r.user_id, str)
        self.assertEqual(self.r.user_id, "")
        self.r.user_id = "1234"
        self.assertEqual(self.r.user_id, "1234")


if __name__ == "__main__":
    unittest.main()

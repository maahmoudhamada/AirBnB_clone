#!/usr/bin/python3
"""Test module for Place class"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class PlaceClassTest(unittest.TestCase):
    """Class to test Place class"""

    def setUp(self):
        """Setup Method"""
        self.p = Place()

    def test_initialization(self):
        """Method to test Place's class initialize"""
        self.assertIsInstance(self.p, Place)
        self.assertTrue(issubclass(type(self.p), BaseModel))

    # ==============================================================

    def test_class_attributes(self):
        """Method to test Place's class attributes"""

        self.assertIsInstance(self.p.city_id, str)
        self.assertEqual(self.p.city_id, "")
        self.p.city_id = "1234"
        self.assertEqual(self.p.city_id, "1234")

    # ------------------------------------------------------

        self.assertIsInstance(self.p.user_id, str)
        self.assertEqual(self.p.user_id, "")
        self.p.user_id = "1234"
        self.assertEqual(self.p.user_id, "1234")

    # ------------------------------------------------------

        self.assertIsInstance(self.p.name, str)
        self.assertEqual(self.p.name, "")
        self.p.name = 'ALX'
        self.assertEqual(self.p.name, "ALX")

    # ------------------------------------------------------
        self.assertIsInstance(self.p.description, str)
        self.assertEqual(self.p.description, "")
        self.p.description = "DESC"
        self.assertEqual(self.p.description, "DESC")

    # ------------------------------------------------------

        self.assertIsInstance(self.p.number_rooms, int)
        self.assertEqual(self.p.number_rooms, 0)
        self.p.number_rooms = 98
        self.assertEqual(self.p.number_rooms, 98)

    # ------------------------------------------------------

        self.assertIsInstance(self.p.number_bathrooms, int)
        self.assertEqual(self.p.number_bathrooms, 0)
        self.p.number_bathrooms = 98
        self.assertEqual(self.p.number_bathrooms, 98)

    # ------------------------------------------------------

        self.assertIsInstance(self.p.max_guest, int)
        self.assertEqual(self.p.max_guest, 0)
        self.p.max_guest = 98
        self.assertEqual(self.p.max_guest, 98)

    # ------------------------------------------------------

        self.assertIsInstance(self.p.price_by_night, int)
        self.assertEqual(self.p.price_by_night, 0)
        self.p.price_by_night = 98
        self.assertEqual(self.p.price_by_night, 98)

    # ------------------------------------------------------

        self.assertIsInstance(self.p.latitude, float)
        self.assertEqual(self.p.latitude, 0.0)
        self.p.latitude = 12.5
        self.assertEqual(self.p.latitude, 12.5)

    # ------------------------------------------------------

        self.assertIsInstance(self.p.longitude, float)
        self.assertEqual(self.p.longitude, 0.0)
        self.p.longitude = 12.5
        self.assertEqual(self.p.longitude, 12.5)

    # ------------------------------------------------------
        tst = ['val1', 'val2', 'val3']
        self.assertIsInstance(self.p.amenity_ids, list)
        self.assertEqual(self.p.amenity_ids, [])
        self.p.amenity_ids = tst
        self.assertEqual(self.p.amenity_ids, tst)


if __name__ == "__main__":
    unittest.main()

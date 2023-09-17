#!/usr/bin/python3
"""
<<<<<<< HEAD
Tests for Place Module
"""

import unittest
import pep8
from datetime import datetime
from models import storage
=======
Contains class TestPlace.
"""
import unittest
import os
import json
import uuid
import re
from datetime import datetime
import models
>>>>>>> 07a4d37cea5158a8bd015dd84f3532d91e1c264b
from models.place import Place


class TestPlace(unittest.TestCase):
<<<<<<< HEAD
    """Unit Tests"""

    def setUp(self):
        self.place = Place()

    def test_city_id(self):
        """
        1. tests if the city_id attribute of the
           Place object is an instance of the str class
        2. tests if the city_id attribute has the value of an empty string
        """
        self.assertIsInstance(self.place.city_id, str)
        self.assertEqual(self.place.city_id, "")

    def test_user_id(self):
        """
        1. tests if the user_id attribute of the
           Place object is an instance of the str class
        2. tests if the user_id attribute has the value of an empty string
        """
        self.assertIsInstance(self.place.user_id, str)
        self.assertEqual(self.place.user_id, "")

    def test_name(self):
        """
        1. test if the name attribute of the
           Place object is an instance of the str class
        2. test if the name attribute has the value of an empty string
        """
        self.assertIsInstance(self.place.name, str)
        self.assertEqual(self.place.name, "")

    def test_description(self):
        """
        1. test if the description attribute of the
           Place object is an instance of the str class
        2. test if the description attribute has the
           value of an empty string
        """
        self.assertIsInstance(self.place.description, str)
        self.assertEqual(self.place.description, "")

    def test_number_rooms(self):
        """
        1. test if the number_rooms attribute of the
           Place object is an instance of the int class
        2. test if the number_rooms attribute has the value of 0
        """
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms(self):
        """
        1. test if the number_bathrooms attribute of the
           Place object is an instance of the int class
        2. test if the number_bathrooms attribute has the value of 0
        """
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest(self):
        """
        1. test if the max_guest attribute of the
           Place object is an instance of the int class
        2. test if the max_guest attribute has the value of 0
        """
        self.assertIsInstance(self.place.max_guest, int)
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night(self):
        """
        1. test if the price_by_night attribute of the
           Place object is an instance of the int class
        2. test if the price_by_night attribute has the value of 0
        """
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude(self):
        """
        1. test if the latitude attribute of the
           Place object is an instance of the float class
        2. test if the latitude attribute has the value of 0.0
        """
        self.assertIsInstance(self.place.latitude, float)
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude(self):
        """
        1. test if the longitude attribute of the
           Place object is an instance of the float class
        2. test if the longitude attribute has the value of 0.0
        """
        self.assertIsInstance(self.place.longitude, float)
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids(self):
        """
        1. test if the amenity_ids attribute of the
           Place object is an instance of the list class
        2. test if the amenity_ids attribute has the value of an empty list
        """
        self.assertIsInstance(self.place.amenity_ids, list)
        self.assertEqual(self.place.amenity_ids, [])

    def test_place_pep8(self):
        """test if place.py is PEP8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

    def test_pep8(self):
        """test if this file is PEP8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")


if __name__ == "__main__":
=======
    """
    Tests class Place.
    """
    def test_inist(self):
        """
        Testing instances: city_id, user_id, name, description,
        number_rooms, number_bathrooms, max_guest, price_by_night,
        latitude, longitude, amenity_ids.
        """
        my_model = Place()
        self.assertEqual(type(my_model), Place)
        d = datetime.now().replace(microsecond=0)
        self.assertEqual(my_model.created_at.replace(microsecond=0), d)
        self.assertEqual(my_model.updated_at.replace(microsecond=0), d)
        self.assertEqual(my_model.city_id, "")
        self.assertEqual(my_model.user_id, "")
        self.assertEqual(my_model.name, "")
        self.assertEqual(my_model.description, "")
        self.assertEqual(my_model.number_rooms, 0)
        self.assertEqual(my_model.number_bathrooms, 0)
        self.assertEqual(my_model.max_guest, 0)
        self.assertEqual(my_model.price_by_night, 0)
        self.assertEqual(my_model.latitude, 0.0)
        self.assertEqual(my_model.longitude, 0.0)
        self.assertEqual(my_model.amenity_ids, [])
        self.assertTrue(type(my_model.id) is str)
        my_model.city_id = "City_id"
        my_model.user_id = "User_id"
        my_model.name = "Westlands"
        my_model.description = "Modern"
        my_model.number_rooms = 2
        my_model.number_bathrooms = 2
        my_model.max_guest = 2
        my_model.price_by_night = 100
        my_model.latitude = 3.4
        my_model.longitude = 4.5
        my_model.amenity_ids = "Amenity_id"
        self.assertEqual(my_model.city_id, "City_id")
        self.assertEqual(my_model.user_id, "User_id")
        self.assertEqual(my_model.name, "Westlands")
        self.assertEqual(my_model.description, "Modern")
        self.assertEqual(my_model.number_rooms, 2)
        self.assertEqual(my_model.number_bathrooms, 2)
        self.assertEqual(my_model.max_guest, 2)
        self.assertEqual(my_model.price_by_night, 100)
        self.assertEqual(my_model.latitude, 3.4)
        self.assertEqual(my_model.longitude, 4.5)
        self.assertEqual(my_model.amenity_ids, "Amenity_id")

    def test_str(self):
        """
        Testing str representation.
        """
        my_model = Place()
        rep = str(my_model)
        class_name = re.search("\\[.*\\]", rep).group(0)
        self_id = re.search("\\(.{36}\\)", rep).group(0)
        self_dict = re.search("\\{.*\\}", rep).group(0)
        self.assertEqual(class_name, "[Place]")
        self.assertTrue(len(self_id) == 38)
        inst_dict = my_model.__dict__
        self.assertEqual(str(inst_dict), self_dict)

    def test_str_not_empty(self):
        """
        Testing string that's not empty.
        """
        my_model = Place()
        my_model.name = "Westlands"
        rep = str(my_model)
        class_name = re.search("\\[.*\\]", rep).group(0)
        self_id = re.search("\\(.{36}\\)", rep).group(0)
        self_dict = re.search("\\{.*\\}", rep).group(0)
        self.assertEqual(class_name, "[Place]")
        self.assertTrue(len(self_id) == 38)
        inst_dict = my_model.__dict__
        self.assertEqual(str(inst_dict), self_dict)

    def test_save(self):
        """
        Testing updated_at.
        """
        my_model = Place()
        updated = my_model.updated_at
        my_model.save()
        self.assertNotEqual(updated, my_model.updated_at)

    def test_save_not(self):
        """
        Testing updated_at.
        """
        my_model = Place()
        updated = my_model.updated_at
        my_model.name = "Westlands"
        self.assertEqual(updated, my_model.updated_at)

    def test_to_dict(self):
        """
        Testing dict.
        """
        my_model = Place()
        my_model_json = my_model.__dict__.copy()
        my_model_json["__class__"] = "Place"
        my_model_json["created_at"] = my_model.created_at.isoformat()
        my_model_json["updated_at"] = my_model.updated_at.isoformat()
        from_js_dict = my_model.to_dict()
        self.assertDictEqual(my_model_json, from_js_dict)

    def test_kwargs(self):
        """
        Test for kwargs.
        """
        my_model = Place()
        my_model_json = my_model.__dict__.copy()
        my_model_json["created_at"] = my_model.created_at.isoformat()
        my_model_json["updated_at"] = my_model.updated_at.isoformat()
        my_new_model = Place(**my_model_json)
        self.assertTrue(type(my_new_model.id) is str)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)
        self.assertTrue(my_model is not my_new_model)

    def tearDown(self):
        """deallocating resources"""
        models.storage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except Exception:
            pass


if __name__ == '__main__':
>>>>>>> 07a4d37cea5158a8bd015dd84f3532d91e1c264b
    unittest.main()

#!/usr/bin/env python3
"""Defines unittests for user class that inherits from BaseModel"""

import unittest
from datetime import datetime
from time import sleep
import models
from models.amenity import Amenity

class TestAmenity_instantiation(unittest.TestCase):
    """tests instantiation of Amenity class"""

    def test_instance_type(self):
        """tests instantiation of Amenity class"""
        self.assertEqual(Amenity, type(Amenity()))
        
    def test_id_type(self):
        """tests id instantiation"""
        amenity_1 = Amenity()
        amenity_2 = Amenity()
        self.assertEqual(str, type(amenity_1.id))
        self.assertNotEqual(amenity_1.id,amenity_2.id)
    
    def test_instance_storage(self):
        """tests storage  of Amenity class instance"""
        self.assertIn(Amenity(), models.storage.all().values())
        
    def test_created_at_type(self):
        """tests created_at instantiation"""
        amenity_1 = Amenity()
        sleep(0.05)
        amenity_2 = Amenity()
        self.assertEqual(datetime, type(amenity_1.created_at))
        self.assertLess(amenity_1.created_at,amenity_2.created_at)

    def test_updated_at_type(self):
        """tests updated_at instantiation"""
        amenity_1 = Amenity()
        sleep(0.05)
        amenity_2 = Amenity()
        self.assertEqual(datetime, type(amenity_1.updated_at))
        self.assertLess(amenity_1.updated_at,amenity_2.updated_at)
        
    def test_name_instantiation(self):
        """tests name instantiation"""
        self.assertEqual(str, type(Amenity().name))
     
    def test_str_representation(self):
        """tests if the string representation of the class Amenity is correct"""
        amenity_1 = Amenity()
        date_today = datetime.today().strftime("%Y-%m-%d %H:%M:%S.%f")
        amenity_1.created_at = amenity_1.updated_at = date_today
        amenity_1.id = "12345"
        bmstr = amenity_1.__str__()
        expectedstr = "[Amenity] (12345) {{'id': '12345', 'created_at': '{}', 'updated_at': '{}', 'name': ''}}".format(date_today, date_today)
        self.assertEqual(bmstr, expectedstr)
        
    def test_instantiation_kwargs(self):
        """Test that instantiation of class Amenity with kwargs works"""
        date = datetime.today()
        date_iso = date.isoformat()
        amenity_1 = Amenity(id="12345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(amenity_1.id, "12345")
        self.assertEqual(amenity_1.created_at, date)
        self.assertEqual(amenity_1.updated_at, date)
        
    def test_instantiation_args_kwargs(self):
        """test that instantiation of class with argsdoesn't work while kwargs works"""
        date = datetime.today()
        date_iso = date.isoformat()
        amenity_1 = Amenity("1", id="12345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(amenity_1.id, "12345")
        self.assertEqual(amenity_1.created_at, date)
        self.assertEqual(amenity_1.updated_at, date)
        
    def test_instantiation_without_kwargs(self):
        """test that instantiation of class without kwargs None value won't work"""
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)
               
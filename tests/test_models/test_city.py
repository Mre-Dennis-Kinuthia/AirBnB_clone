#!/usr/bin/env python3
"""Defines unittests for user class that inherits from BaseModel"""

import unittest
from datetime import datetime
from time import sleep
import models
from models.city import City

class TestCity_instantiation(unittest.TestCase):
    """tests instantiation of City class"""

    def test_instance_type(self):
        """tests instantiation of User class"""
        self.assertEqual(City, type(City()))
        
    def test_id_type(self):
        """tests id instantiation"""
        city_1 = City()
        city_2 = City()
        self.assertEqual(str, type(city_1.id))
        self.assertNotEqual(city_1.id, city_2.id)
    
    def test_instance_storage(self):
        """tests storage  of City class instance"""
        self.assertIn(City(), models.storage.all().values())
        
    def test_created_at_type(self):
        """tests created_at instantiation"""
        city_1 = City()
        sleep(0.05)
        city_2 = City()
        self.assertEqual(datetime, type(city_1.created_at))
        self.assertLess(city_1.created_at, city_2.created_at)

    def test_updated_at_type(self):
        """tests updated_at instantiation"""
        city_1 = City()
        sleep(0.05)
        city_2 = City()
        self.assertEqual(datetime, type(city_1.updated_at))
        self.assertLess(city_1.updated_at, city_2.updated_at)
    
    def test_name_instantiation(self):
        """tests name instantiation"""
        self.assertEqual(str, type(City().name))
     
    def test_str_representation(self):
        """tests if the string representation of the class City is correct"""
        city_1 = City()
        date_today = datetime.today().strftime("%Y-%m-%d %H:%M:%S.%f")
        city_1.created_at =city_1.updated_at = date_today
        city_1.id = "12345"
        citystr =city_1.__str__()
        expectedstr = "[City] (12345) {{'id': '12345', 'created_at': '{}', 'updated_at': '{}', 'name': '', 'state_id': ''}}".format(date_today, date_today)
        self.assertEqual(citystr, expectedstr)
        
    def test_instantiation_kwargs(self):
        """Test that instantiation of class City with kwargs works"""
        date = datetime.today()
        date_iso = date.isoformat()
        city_1 = City(id="12345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(city_1.id, "12345")
        self.assertEqual(city_1.created_at, date)
        self.assertEqual(city_1.updated_at, date)
        
    def test_instantiation_args_kwargs(self):
        """test that instantiation of class with argsdoesn't work while kwargs works"""
        date = datetime.today()
        date_iso = date.isoformat()
        city_1 = City("1", id="12345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(city_1.id, "12345")
        self.assertEqual(city_1.created_at, date)
        self.assertEqual(city_1.updated_at, date)
        
    def test_instantiation_without_kwargs(self):
        """test that instantiation of class without kwargs None value won't work"""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

if __name__ == "__main__":
    unittest.main()
           
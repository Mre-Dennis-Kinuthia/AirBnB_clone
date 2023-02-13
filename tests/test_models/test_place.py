#!/usr/bin/env python3
"""Defines unittests for Place class that inherits from BaseModel"""

import unittest
from datetime import datetime
from time import sleep
import models
from models.place import Place

class TestPlace_instantiation(unittest.TestCase):
    """tests instantiation of Place class"""

    def test_instance_type(self):
        """tests instantiation of Place class"""
        self.assertEqual(Place, type(Place()))
        
    def test_id_type(self):
        """tests id instantiation"""
        place_1 = Place()
        place_2 = Place()
        self.assertEqual(str, type(place_1.id))
        self.assertNotEqual(place_1.id, place_2.id)
    
    def test_instance_storage(self):
        """tests storage  of Place class instance"""
        self.assertIn(Place(), models.storage.all().values())
        
    def test_created_at_type(self):
        """tests created_at instantiation"""
        place_1 = Place()
        sleep(0.05)
        place_2 = Place()
        self.assertEqual(datetime, type(place_1.created_at))
        self.assertLess(place_1.created_at, place_2.created_at)

    def test_updated_at_type(self):
        """tests updated_at instantiation"""
        place_1 = Place()
        sleep(0.05)
        place_2 = Place()
        self.assertEqual(datetime, type(place_1.updated_at))
        self.assertLess(place_1.updated_at, place_2.updated_at)
        
    def test_city_id_user_id_instantiation(self):
        """tests city_id and user_id instantiation"""
        self.assertEqual(str, type(Place().city_id))
        self.assertEqual(str, type(Place().user_id))
        
    def test_name_instantiation(self):
        """tests name instantiation"""
        self.assertEqual(str, type(Place().name))
    
    def test_description_instantiation(self):
        """tests description instantiation"""
        self.assertEqual(str, type(Place().description))
        
    def test_number_rooms_instantiation(self):
        """tests rooms instantiation"""
        self.assertEqual(int, type(Place().number_rooms))
        
    def test_bathrooms_instantiation(self):
        """tests bathrooms instantiation"""
        self.assertEqual(int, type(Place().number_bathrooms))
        
    def test_max_guest_instantiation(self):
        """tests max_guest instantiation"""
        self.assertEqual(int, type(Place().max_guest))
        
    def test_price_by_night_instantiation(self):
        """tests price_by_night instantiation"""
        self.assertEqual(int, type(Place().price_by_night))
        
    def test_latitude_instantiation(self):
        """tests latitude instantiation"""
        self.assertEqual(float, type(Place().latitude))
        
    def test_longitude_instantiation(self):
        """tests longitude instantiation"""
        self.assertEqual(float, type(Place().longitude))
        
    def test_amenity_ids_instantiation(self):
        """tests amenity_ids instantiation"""
        self.assertEqual(str, type(Place().amenity_ids)) 
     
    def test_str_representation(self):
        """tests if the string representation of the class Place is correct"""
        place_1 = Place()
        date_today = datetime.today().strftime("%Y-%m-%d %H:%M:%S.%f")
        place_1.created_at = place_1.updated_at = date_today
        place_1.id = "12345"
        placestr = place_1.__str__()
        expectedstr = "[Place] (12345) {{'id': '12345', 'created_at': '{}', 'updated_at': '{}', 'city_id': '', 'user_id': '', 'name': '', 'description': '', 'number_rooms': 0, 'number_bathrooms': 0, 'max_guest': 0, 'price_by_night': 0, 'latitude': 0.0, 'longitude': 0.0, 'amenity_ids': ''}}".format(date_today, date_today)
        self.assertEqual(placestr, expectedstr)
        
    def test_instantiation_kwargs(self):
        """Test that instantiation of class Place with kwargs works"""
        date = datetime.today()
        date_iso = date.isoformat()
        place_1 = Place(id="12345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(place_1.id, "12345")
        self.assertEqual(place_1.created_at, date)
        self.assertEqual(place_1.updated_at, date)
        
    def test_instantiation_args_kwargs(self):
        """test that instantiation of class with argsdoesn't work while kwargs works"""
        date = datetime.today()
        date_iso = date.isoformat()
        place_1 = Place("1", id="12345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(place_1.id, "12345")
        self.assertEqual(place_1.created_at, date)
        self.assertEqual(place_1.updated_at, date)
        
    def test_instantiation_without_kwargs(self):
        """test that instantiation of class without kwargs None value won't work"""
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Defines unittests for Review class that inherits from BaseModel"""

import unittest
from datetime import datetime
from time import sleep
import models
from models.review import Review

class TestReview_instantiation(unittest.TestCase):
    """tests instantiation of Review class"""

    def test_instance_type(self):
        """tests instantiation of Review class"""
        self.assertEqual(Review, type(Review()))
        
    def test_id_type(self):
        """tests id instantiation"""
        review_1 = Review()
        review_2 = Review()
        self.assertEqual(str, type(review_1.id))
        self.assertNotEqual(review_1.id, review_2.id)
    
    def test_instance_storage(self):
        """tests storage  of Review class instance"""
        self.assertIn(Review(), models.storage.all().values())
        
    def test_created_at_type(self):
        """tests created_at instantiation"""
        review_1 = Review()
        sleep(0.05)
        review_2 = Review()
        self.assertEqual(datetime, type(review_1.created_at))
        self.assertLess(review_1.created_at, review_2.created_at)

    def test_updated_at_type(self):
        """tests updated_at instantiation"""
        review_1 = Review()
        sleep(0.05)
        review_2 = Review()
        self.assertEqual(datetime, type(review_1.updated_at))
        self.assertLess(review_1.updated_at, review_2.updated_at)
        
    def test_email_password_instantiation(self):
        """tests email and password instantiation"""
        self.assertEqual(str, type(Review().place_id))
        self.assertEqual(str, type(Review().user_id))
        
    def test_name_instantiation(self):
        """tests name instantiation"""
        self.assertEqual(str, type(Review().text))
     
    def test_str_representation(self):
        """tests if the string representation of the class Review is correct"""
        review_1 = Review()
        date_today = datetime.today().strftime("%Y-%m-%d %H:%M:%S.%f")
        review_1.created_at = review_1.updated_at = date_today
        review_1.id = "12345"
        bmstr = review_1.__str__()
        expectedstr = "[Review] (12345) {{'id': '12345', 'created_at': '{}', 'updated_at': '{}', 'place_id': '', 'user_id': '', 'text': ''}}".format(date_today, date_today)
        self.assertEqual(bmstr, expectedstr)
        
    def test_instantiation_kwargs(self):
        """Test that instantiation of class Review with kwargs works"""
        date = datetime.today()
        date_iso = date.isoformat()
        review_1 = Review(id="12345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(review_1.id, "12345")
        self.assertEqual(review_1.created_at, date)
        self.assertEqual(review_1.updated_at, date)
        
    def test_instantiation_args_kwargs(self):
        """test that instantiation of class with argsdoesn't work while kwargs works"""
        date = datetime.today()
        date_iso = date.isoformat()
        review_1 = Review("1", id="12345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(review_1.id, "12345")
        self.assertEqual(review_1.created_at, date)
        self.assertEqual(review_1.updated_at, date)
        
    def test_instantiation_without_kwargs(self):
        """test that instantiation of class without kwargs None value won't work"""
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)
               
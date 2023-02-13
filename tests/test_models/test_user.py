#!/usr/bin/env python3
"""Defines unittests for user class that inherits from BaseModel"""

import unittest
from datetime import datetime
from time import sleep
import models
from models.user import User

class TestUser_instantiation(unittest.TestCase):
    """tests instantiation of User class"""

    def test_instance_type(self):
        """tests instantiation of User class"""
        self.assertEqual(User, type(User()))
        
    def test_id_type(self):
        """tests id instantiation"""
        user_1 = User()
        user_2 = User()
        self.assertEqual(str, type(user_1.id))
        self.assertNotEqual(user_1.id, user_2.id)
    
    def test_instance_storage(self):
        """tests storage  of User class instance"""
        self.assertIn(User(), models.storage.all().values())
        
    def test_created_at_type(self):
        """tests created_at instantiation"""
        user_1 = User()
        sleep(0.05)
        user_2 = User()
        self.assertEqual(datetime, type(user_1.created_at))
        self.assertLess(user_1.created_at, user_2.created_at)

    def test_updated_at_type(self):
        """tests updated_at instantiation"""
        user_1 = User()
        sleep(0.05)
        user_2 = User()
        self.assertEqual(datetime, type(user_1.updated_at))
        self.assertLess(user_1.updated_at, user_2.updated_at)
        
    def test_email_password_instantiation(self):
        """tests email and password instantiation"""
        self.assertEqual(str, type(User().email))
        self.assertEqual(str, type(User().password))
        
    def test_name_instantiation(self):
        """tests name instantiation"""
        self.assertEqual(str, type(User().first_name))
        self.assertEqual(str, type(User().last_name))
     
    def test_str_representation(self):
        """tests if the string representation of the class User is correct"""
        user_1 = User()
        date_today = datetime.today().strftime("%Y-%m-%d %H:%M:%S.%f")
        user_1.created_at = user_1.updated_at = date_today
        user_1.id = "12345"
        bmstr = user_1.__str__()
        expectedstr = "[User] (12345) {{'id': '12345', 'created_at': '{}', 'updated_at': '{}', 'email': '', 'password': '', 'first_name': '', 'last_name': ''}}".format(date_today, date_today)
        self.assertEqual(bmstr, expectedstr)
        
    def test_instantiation_kwargs(self):
        """Test that instantiation of class User with kwargs works"""
        date = datetime.today()
        date_iso = date.isoformat()
        user_1 = User(id="12345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(user_1.id, "12345")
        self.assertEqual(user_1.created_at, date)
        self.assertEqual(user_1.updated_at, date)
        
    def test_instantiation_args_kwargs(self):
        """test that instantiation of class with argsdoesn't work while kwargs works"""
        date = datetime.today()
        date_iso = date.isoformat()
        user_1 = User("1", id="12345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(user_1.id, "12345")
        self.assertEqual(user_1.created_at, date)
        self.assertEqual(user_1.updated_at, date)
        
    def test_instantiation_without_kwargs(self):
        """test that instantiation of class without kwargs None value won't work"""
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)
               

        

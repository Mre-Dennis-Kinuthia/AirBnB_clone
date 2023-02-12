#!/usr/bin/env python3
"""Unittests for BaseModel class"""

import unittest
import os
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """test for class instantiation"""

    def test_id(self):
        """tests if the id property is different with each instance"""
        base_model_1= BaseModel()
        base_model_2= BaseModel()
        self.assertNotEqual(base_model_1.id, base_model_2.id)
    
    def test_created_at(self):
        """tests if the created_at property is similar for instances created at the same time"""
        base_model_1= BaseModel()
        base_model_2= BaseModel()
        self.assertEqual(base_model_1.created_at, base_model_2.created_at)
        
    def test_updated_at(self):
        """tests if the updated_at property is similar for instances updated at the same time"""
        base_model_1= BaseModel()
        base_model_2= BaseModel()
        
        self.assertEqual(base_model_1.updated_at, base_model_2.updated_at)

    def test_created_at_different(self):
        """tests if the created_at property is different for instances created at different times"""
        base_model_1 = BaseModel()
        sleep(0.05)
        base_model_2 = BaseModel()
        self.assertLess(base_model_1.created_at, base_model_2.created_at)
        
    def test_updated_at_different(self):
        """tests if the updated_at property is different for instances updated at different times"""
        base_model_1 = BaseModel()
        sleep (0.05)
        base_model_2 = BaseModel()
        self.assertLess(base_model_1.updated_at, base_model_2.updated_at)
      
    def test_id_type(self):
        """tests if the id property is of type string"""
        base_model_1 = BaseModel()
        self.assertEqual(type(base_model_1.id), str)
        
    def test_created_at_type(self):
        """tests if the created_at property is of type datetime"""
        base_model_1 = BaseModel()
        self.assertEqual(type(base_model_1.created_at), datetime)
        
    def test_updated_at_type(self):
        """tests if the updated_at property is of type datetime"""
        base_model_1 = BaseModel()
        self.assertEqual(type(base_model_1.updated_at), datetime)
    
    def test_instance_of_class(self):
        """Test that instance of class is of type BaseModel"""
        base_model_1 = BaseModel()
        self.assertIsInstance(base_model_1, BaseModel)
        
    def test_str_representation(self):
        """tests if the string representation of the class is correct"""
        base_model_1 = BaseModel()
        date_today = datetime.today().strftime("%Y-%m-%d %H:%M:%S.%f")
        base_model_1.created_at = base_model_1.updated_at = date_today
        base_model_1.id = "12345"
        bmstr = base_model_1.__str__()
        expectedstr = "[BaseModel] (12345) {{'id': '12345', 'created_at': '{}', 'updated_at': '{}'}}".format(date_today, date_today)
        self.assertEqual(bmstr, expectedstr)
        
    def test_instantiation_kwargs(self):
        """Test that instantiation of class with kwargs works"""
        date = datetime.today()
        date_iso = date.isoformat()
        base_model_1 = BaseModel(id="12345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(base_model_1.id, "12345")
        self.assertEqual(base_model_1.created_at, date)
        self.assertEqual(base_model_1.updated_at, date)
        
    def test_instantiation_args_kwargs(self):
        """test that instantiation of class with argsdoesn't work while kwargs works"""
        date = datetime.today()
        date_iso = date.isoformat()
        base_model_1 = BaseModel("1", id="12345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(base_model_1.id, "12345")
        self.assertEqual(base_model_1.created_at, date)
        self.assertEqual(base_model_1.updated_at, date)
        
    def test_instantiation_without_kwargs(self):
        """test that instantiation of class without kwargs None value won't work"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)
            
class TestBaseModel_save(unittest.TestCase):
    """unittests for testing save method"""
    
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "testfile")
        except IOError:
            pass
        
    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("testfile", "file.json")
        except IOError:
            pass
        
    def test_save_one(self):
        """tests save method for first object"""
        base_model_1 = BaseModel()
        sleep(0.05)
        firt_updated = base_model_1.updated_at
        base_model_1.save()
        self.assertLess(first_updated, base_model_1.updated_at)
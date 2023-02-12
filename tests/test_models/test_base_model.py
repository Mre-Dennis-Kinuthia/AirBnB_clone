#!/usr/bin/env python3

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """test for class instantiation"""
    
    def setUp(self):
        self.base_model_1 = BaseModel()
        self.base_model_2 = BaseModel()
    
    def test_id(self):
        self.assertNotEqual(self.base_model_1.id, self.base_model_2.id)
        
    def test_created_at(self):
        self.assertEqual(self.base_model_1.created_at, self.base_model_2.created_at)
    def test_updated_at(self):
        self.assertEqual(self.base_model_1.updated_at, self.base_model_2.updated_at)


      

    
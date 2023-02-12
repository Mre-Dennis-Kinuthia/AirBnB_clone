#!/usr/bin/env python3
"""unittests for file storage of the basemodel class"""

import unittest
import os
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models. review import Review
from models. state import State


class TestFileStorage_instantiation(unittest.TestCase):
    """test instantiation of the FileStorage class"""

    def test_instance_type(self):
        """test instance type"""
        file_storage = FileStorage()
        self.assertIsInstance(file_storage, FileStorage)
        
    def test_instantiation(self):
        """test instantiation of the FileStorage class"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_instantiation_args(self):
        """test instantiation of the FileStorage class with arguments"""
        with self.assertRaises(TypeError):
            FileStorage(None, None)

    def test_file_path_attribute(self):
        """test file_path attribute for type and whether private attributes"""
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)
        
    def test_objects_attribute(self):
        """test objects attribute for type and whether private attributes"""
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)
    
    def test_storage_instance(self):
        """tests whether models.storage is a FileStorage instance"""
        self.assertIsInstance(models.storage, FileStorage)

class TestFileStorage_methods(unittest.TestCase):
    """Test FileStorage methods"""
    
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
        FileStorage._FileStorage__objects = {}
        
    def test_all(self):
        """tests the all method"""
        self.assertEqual(type(models.storage.all()), dict)
        
    def test_new(self):
        """tests the new method"""
        objects = [BaseModel(), User(), State(), Place(), Amenity(), Review()]
        for obj in objects:
            models.storage.new(obj)
            self.assertIn("{}.{}". format(type(obj).__name__, obj.id), models.storage.all().keys())
            self.assertIn(obj, models.storage.all().values())


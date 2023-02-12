#!/usr/bin/env python3
"""file contains class on FileStorage"""


import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
import json


class FileStorage:
    """Class that defines how to store instances of BaseModel"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """"save the object"""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, mode='w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file exists)"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r') as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                class_name = value.pop("__class__", None)
                if class_name is not None:
                    cls = eval(class_name)
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
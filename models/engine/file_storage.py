#!/usr/bin/env python3
import os
from models.base_model import BaseModel

import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)
                       
    """def reload(self):
         if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
        
    """
    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                class_name = value.pop("__class__", None)
                if class_name is not None:
                    cls = eval(class_name)
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj

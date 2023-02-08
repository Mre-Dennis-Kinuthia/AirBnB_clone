#!/usr/bin/python3
from models.base_model import BaseModel


class FileStorage:
    __file_path = ""
    __objects = {}
    
    def all(self):
        return self.__objects
    
    def new(self, obj):
        __objects.obj = BaseModel.id
        

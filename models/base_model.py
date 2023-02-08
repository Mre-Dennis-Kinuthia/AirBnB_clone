#!/usr/bin/env python3
""" date time module import
"""


from datetime import datetime
import uuid

class BaseModel:

    def __init__ (self, id, created_at, updated_at):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        
    def id(self):
         self.id = str(uuid.uuid4())
         return self.id
         
   

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()

    def __str__(self):
        """returns a string representation of a BaseModel class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        my_dict = (self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
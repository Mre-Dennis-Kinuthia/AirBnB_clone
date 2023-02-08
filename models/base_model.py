# pylint: disable=invalid-name
#!/usr/bin/env python3
""" date time module import
"""


from datetime import datetime
import uuid

class BaseModel:
    """ BaseModel class
    def __init__ (self, id, created_at, updated_at):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
    """
    def __init__ (self, *args, **kwargs):
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

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

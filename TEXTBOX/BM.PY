#!/usr/bin/env python3
""" date time module import
"""


from datetime import datetime
import uuid


class BaseModel:
    """ BaseModel class"""
    def __init__(self, *args, **kwargs):
        """ initial"""

        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """__str__: should print: [<class name>] (<self.id>) <self.__dict__"""
        
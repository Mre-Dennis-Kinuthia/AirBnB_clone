#!/usr/bin/env python
"""file containing Class Amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class Amenity inherits BaseModel """
    name = ''

    def __init__(self, *args, **kwargs):
        """ Initialize user """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")

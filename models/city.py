#!/usr/bin/env python
"""defines class City"""


from models.base_model import BaseModel


class City(BaseModel):
    """ Class City inherits Basemodel """
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """ Initialize user """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
        self.state_id = kwargs.get('state_id', "")

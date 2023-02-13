#!/usr/bin/env python
"""defines class State"""


from models.base_model import BaseModel

class State(BaseModel):
    """ class State inherits Basemodel """
    name = ''

    def __init__(self, *args, **kwargs):
        """ Constractor """
        super().__init__(*args, **kwargs)
        self.name = kwargs.pop('name', "")
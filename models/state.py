#!/usr/bin/env python

from models.base_model import BaseModel


class State(BaseModel):
    name = ''


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.pop('name',"")
#!/usr/bin/env python

from models.base_model import BaseModel


class Review(BaseModel):
    """ class Review inherits BaseModel"""
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """ Constractor """
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.pop('place_id', '')
        self.user_id = kwargs.pop('user_id', '')
        self.text = kwargs.pop('text', '')

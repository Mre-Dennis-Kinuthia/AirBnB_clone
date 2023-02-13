#!/usr/bin/env python3
"""Defines unittests for user class that inherits from BaseModel"""

import unittest
from datetime import datetime
from time import sleep
import models
from models.state import State

class TestState_instantiation(unittest.TestCase):
    """tests instantiation of state class"""

    def test_instance_type(self):
        """tests instantiation of User class"""
        self.assertEqual(State, type(State()))
        
    def test_id_type(self):
        """tests id instantiation"""
        state_1 = State()
        state_2 = State()
        self.assertEqual(str, type(state_1.id))
        self.assertNotEqual(state_1.id, state_2.id)
    
    def test_instance_storage(self):
        """tests storage  of State class instance"""
        self.assertIn(State(), models.storage.all().values())
        
    def test_created_at_type(self):
        """tests created_at instantiation"""
        state_1 = State()
        sleep(0.05)
        state_2 = State()
        self.assertEqual(datetime, type(state_1.created_at))
        self.assertLess(state_1.created_at, state_2.created_at)

    def test_updated_at_type(self):
        """tests updated_at instantiation"""
        state_1 = State()
        sleep(0.05)
        State_2 = State()
        self.assertEqual(datetime, type(state_1.updated_at))
        self.assertLess(state_1.updated_at, State_2.updated_at)
    
    def test_name_instantiation(self):
        """tests name instantiation"""
        self.assertEqual(str, type(State().name))
     
    def test_str_representation(self):
        """tests if the string representation of the class State is correct"""
        state_1 = State()
        date_today = datetime.today().strftime("%Y-%m-%d %H:%M:%S.%f")
        state_1.created_at = state_1.updated_at = date_today
        state_1.id = "12345"
        bmstr = state_1.__str__()
        expectedstr = "[State] (12345) {{'id': '12345', 'created_at': '{}', 'updated_at': '{}', 'name': ''}}".format(date_today, date_today)
        self.assertEqual(bmstr, expectedstr)
        
    def test_instantiation_kwargs(self):
        """Test that instantiation of class State with kwargs works"""
        date = datetime.today()
        date_iso = date.isoformat()
        state_1 = State(id="12345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(state_1.id, "12345")
        self.assertEqual(state_1.created_at, date)
        self.assertEqual(state_1.updated_at, date)
        
    def test_instantiation_args_kwargs(self):
        """test that instantiation of class with argsdoesn't work while kwargs works"""
        date = datetime.today()
        date_iso = date.isoformat()
        state_1 = State("1", id="12345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(state_1.id, "12345")
        self.assertEqual(state_1.created_at, date)
        self.assertEqual(state_1.updated_at, date)
        
    def test_instantiation_without_kwargs(self):
        """test that instantiation of class without kwargs None value won't work"""
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)
               
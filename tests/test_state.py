#!/usr/bin/python3
"""test module for state.py"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """tests for class state"""
    def setUp(self):
        self.state = State()
    
    def test_instance(self):
        """test state instance and inheritance"""
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)

    def test_state_attributes(self):
        """test class attributes"""
        self.assertEqual(self.state.name, "")

    def test_base_attributes(self):
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

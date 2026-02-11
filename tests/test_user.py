#!/usr/bin/python3
"""test module for user.py"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """tests for class user"""
    def setUp(self):
        self.user = User()
    
    def test_instance(self):
        """test user instance and inheritance"""
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user, BaseModel)

    def test_user_attributes(self):
        """test class attributes"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_base_attributes(self):
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

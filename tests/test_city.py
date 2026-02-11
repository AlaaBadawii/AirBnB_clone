#!/usr/bin/python3
"""test module for city.py"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """tests for class city"""
    def setUp(self):
        self.city = City()
    
    def test_instance(self):
        """test city instance and inheritance"""
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

    def test_city_attributes(self):
        """test class attributes"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_base_attributes(self):
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
#!/usr/bin/python3
"""test module for amenity.py"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """tests for class amenity"""
    def setUp(self):
        self.amenity = Amenity()
    
    def test_instance(self):
        """test amenity instance and inheritance"""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)

    def test_amenity_attributes(self):
        """test class attributes"""
        self.assertEqual(self.amenity.name, "")

    def test_base_attributes(self):
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
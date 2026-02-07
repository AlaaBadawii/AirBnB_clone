#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""
    def setUp(self):
        self.base = BaseModel()

    # class creation
    def test_BaseModel(self):
        """test class creation"""
        self.assertIsInstance(self.base, BaseModel)

    def test_BaseModel_id(self):
        """test id intilizing"""
        self.assertTrue(hasattr(self.base, "id"))

    def test_BaseModel_id_type(self):
        """test id type"""
        self.assertIsInstance(self.base.id, str)

    def test_BaseModel_id_not_empty(self):
        """test that the id is not empty"""
        self.assertNotEqual(self.base.id, "")

    def test_BaseModel_created_at(self):
        """test created_at intilizing"""
        self.assertTrue(hasattr(self.base, "created_at"))

    def test_BaseModel_created_at_type(self):
        """test created_at type"""
        self.assertIsInstance(self.base.created_at, datetime)

    def test_BaseModel_updated_at(self):
        """test updated_at intilizing"""
        self.assertTrue(hasattr(self.base, "updated_at"))

    def test_BaseModel_updated_at_type(self):
        """test updated_at type"""
        self.assertIsInstance(self.base.updated_at, datetime)

    # test init with kwargs
    def test_init_with_kwargs(self):
        """test init with kwargs"""
        base_dict = self.base.to_dict()
        new_base = BaseModel(**base_dict)
        self.assertEqual(self.base.id, new_base.id)

    def test_init_with_kwargs_created_at(self):
        """test that created_at is correctly set with kwargs"""
        base_dict = self.base.to_dict()
        new_base = BaseModel(**base_dict)
        self.assertEqual(self.base.created_at, new_base.created_at)

    def test_init_with_kwargs_updated_at(self):
        """test that updated_at is correctly set with kwargs"""
        base_dict = self.base.to_dict()
        new_base = BaseModel(**base_dict)
        self.assertEqual(self.base.updated_at, new_base.updated_at)

    def test_init_with_kwargs_class_in_dict(self):
        """test that __class__ in kwargs is ignored"""
        base_dict = self.base.to_dict()
        base_dict["__class__"] = "FakeClass"
        new_base = BaseModel(**base_dict)
        self.assertEqual(new_base.__class__, BaseModel)

    def test_init_with_kwargs_class_is_same(self):
        """test that class is the same when initialized with kwargs"""
        base_dict = self.base.to_dict()
        new_base = BaseModel(**base_dict)
        self.assertEqual(new_base.__class__, BaseModel)

    def test_init_kwargs_class_not_in_dict(self):
        """__class__ from kwargs should not be added as an attribute"""
        base_dict = self.base.to_dict()
        new_base = BaseModel(**base_dict)
        self.assertNotIn("__class__", new_base.__dict__)

    def test_init_with_kwargs_extra_keys(self):
        """test that extra keys in kwargs are set as attributes"""
        base_dict = self.base.to_dict()
        base_dict["extra_key"] = "extra_value"
        new_base = BaseModel(**base_dict)
        self.assertTrue(hasattr(new_base, "extra_key"))
        self.assertEqual(new_base.extra_key, "extra_value")

    def test_init_with_kwargs_no_kwargs(self):
        """test init with no kwargs creates new instance with new id"""
        new_base = BaseModel()
        self.assertNotEqual(self.base.id, new_base.id)
        self.assertNotEqual(self.base.created_at, new_base.created_at)
        self.assertNotEqual(self.base.updated_at, new_base.updated_at)

    def test_init_with_kwargs_no_kwargs_created_at(self):
        """test init with no kwargs creates new created_at"""
        new_base = BaseModel()
        self.assertNotEqual(self.base.created_at, new_base.created_at)

    def test_init_with_kwargs_no_kwargs_updated_at(self):
        """test init with no kwargs creates a new updated_at"""
        new_base = BaseModel()
        self.assertNotEqual(self.base.updated_at, new_base.updated_at)

    # to_dict method
    def test_to_dict_existence(self):
        """test existence of to dict method"""
        self.assertTrue(hasattr(self.base, "to_dict"))

    def test_to_dict_type(self):
        """test return type of to dict method"""
        self.assertIsInstance(self.base.to_dict(), dict)

    def test_to_dict_is_callable(self):
        self.assertTrue(callable(self.base.to_dict))

    def test_to_dict_return_values(self):
        """test expected output"""
        base_dict = self.base.to_dict()
        self.assertIn("created_at", base_dict)
        self.assertIn("updated_at", base_dict)
        self.assertIn("__class__", base_dict)

    def test_to_dict_contains_id(self):
        base_dict = self.base.to_dict()
        self.assertIn("id", base_dict)

    def test_to_dict_created_at_is_string(self):
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict["created_at"], str)

    def test_to_dict_updated_at_is_string(self):
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict["updated_at"], str)

    def test_to_dict_class_name(self):
        base_dict = self.base.to_dict()
        self.assertEqual(base_dict["__class__"], "BaseModel")

    # datetime attributes remain datetime after to_dict
    def test_created_at_remains_datetime(self):
        self.assertIsInstance(self.base.created_at, datetime)

    def test_updated_at_remains_datetime_after_to_dict(self):
        self.base.to_dict()
        self.assertIsInstance(self.base.updated_at, datetime)

    # save method
    def test_save_existence(self):
        """test save method existence"""
        self.assertTrue(hasattr(self.base, "save"))

    def test_save_is_callable(self):
        self.assertTrue(callable(self.base.save))

    def test_save_updates_updated_at(self):
        """test that updated_at updated"""
        old_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(self.base.updated_at, old_updated_at)

    # __str__ method
    def test_str_existence(self):
        "test __str__"
        self.assertTrue(hasattr(self.base, "__str__"))

    def test_str_return_type(self):
        """test return type of __str__"""
        self.assertIsInstance(self.base.__str__(), str)

    def test_str_expected_value(self):
        """test that we get the expected value"""
        expected_value = "[{}] ({}) {}".format(
            "BaseModel",
            self.base.id,
            self.base.__dict__
        )
        self.assertEqual(expected_value, self.base.__str__())

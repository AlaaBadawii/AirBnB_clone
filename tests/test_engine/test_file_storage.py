#!/usr/bin/python3
import os
import tempfile
import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models.base_model as base_model_module


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage class"""
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = os.path.join(self.temp_dir.name, "file.json")
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.storage._FileStorage__objects = {}
        self.original_storage = base_model_module.storage
        base_model_module.storage = self.storage

    def tearDown(self):
        base_model_module.storage = self.original_storage
        self.temp_dir.cleanup()

    def _make_base_model(self, obj_id="123"):
        now = datetime.utcnow().isoformat()
        return BaseModel(id=obj_id, created_at=now, updated_at=now)

    def test_all_returns_objects_dict(self):
        """all should return the storage dictionary"""
        self.assertIs(self.storage.all(), self.storage._FileStorage__objects)

    def test_new_adds_object_with_key(self):
        """new should store object with <class name>.id key"""
        obj = self._make_base_model("abc")
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertIs(self.storage.all()[key], obj)

    def test_save_creates_json_file(self):
        """save should serialize objects to the JSON file"""
        obj = self._make_base_model("save-id")
        self.storage.new(obj)
        self.storage.save()
        with open(self.file_path, "r", encoding="utf-8") as fp:
            data = fp.read()
        self.assertIn("BaseModel.save-id", data)
        self.assertIn('"__class__": "BaseModel"', data)

    def test_reload_restores_objects(self):
        """reload should restore objects from JSON file"""
        obj = self._make_base_model("reload-id")
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage._FileStorage__objects = {}
        new_storage.reload()
        key = "BaseModel.reload-id"
        self.assertIn(key, new_storage.all())
        self.assertEqual(new_storage.all()[key].id, "reload-id")

    def test_reload_missing_file_no_error(self):
        """reload should not error if file is missing"""
        missing_storage = FileStorage()
        missing_storage._FileStorage__file_path = os.path.join(
            self.temp_dir.name, "missing.json"
        )
        missing_storage._FileStorage__objects = {}
        missing_storage.reload()
        self.assertEqual(missing_storage.all(), {})

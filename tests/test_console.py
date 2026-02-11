#!/usr/bin/python3
"""test module for console.py"""
from email import message
from io import StringIO
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models import storage
import models.base_model as base_model_module
import tempfile
import os
import ast


class TestConsole(unittest.TestCase):
    """TestConsloe class"""
    def setUp(self):
        """set up for test create an isolated storage for tests
        using tempfile"""
        self.tempdir = tempfile.TemporaryDirectory()
        self.file_path = os.path.join(self.tempdir.name, "file.json")
        storage._FileStorage__file_path = self.file_path
        storage._FileStorage__objects = {}
        self.original_storage = base_model_module.storage
        base_model_module.storage = storage

    def tearDown(self):
        """clen everything after finish, and return backrefrences"""
        base_model_module.storage = self.original_storage
        self.tempdir.cleanup()

    def _helper(self, cmd):
        with patch('sys.stdout', new=StringIO()) as f:
            result = HBNBCommand().onecmd(cmd)
        return result, f.getvalue()

    def test_help(self):
        """tests for help cmd"""
        _, output = self._helper("help quit")
        self.assertIn("quit", output.lower())

    def test_quit_output(self):
        """tests for quit cmd"""
        result, output = self._helper("quit")

        self.assertEqual(output, '')
        self.assertEqual(result, True)

    def test_EOF(self):
        """tests EOF"""
        result, output = self._helper("EOF")

        self.assertEqual(output, '\n')
        self.assertEqual(result, True)

    def test_emptyline(self):
        _, output = self._helper("")
        self.assertEqual(output, '')

        _, output = self._helper("   ")
        self.assertEqual(output, '')

    # create
    def test_create_name_missing(self):
        """tests for create cmd"""
        _, message = self._helper("create")
        self.assertEqual(message.strip(), "** class name missing **")

    def test_create_wrong_class_name(self):
        """tests passing wrong class name"""
        _, message = self._helper("create FakeClass")
        self.assertEqual(message.strip(), "** class doesn't exist **")
    
    def test_create_with_correct_class_name(self):
        """tests passing a correct class name"""
        _, id = self._helper("create BaseModel")

        key = "BaseModel.{}".format(id.strip())
        self.assertIn(key, storage.all())

        obj = storage.all()[key]
        self.assertEqual(obj.__class__.__name__, "BaseModel")
    
    # show
    def test_show_name_missing(self):
        """test for missing name"""
        _, message = self._helper("show")
        self.assertEqual(message.strip(), "** class name missing **")
    
    def test_show_wrong_class(self):
        """test for class doesn't exist"""
        _, message = self._helper("show FakeClass")
        self.assertEqual(message.strip(), "** class doesn't exist **")
    
    def test_show_id_missing(self):
        """test for missing id"""
        _, message = self._helper("show BaseModel")
        self.assertEqual(message.strip(), "** instance id missing **")

    def test_wrong_id(self):
        """passing wrong id means no instance found"""
        _, message = self._helper("show BaseModel 187654")
        self.assertEqual(message.strip(), "** no instance found **")

    def test_show_with_correct_input(self):
        """testing existance of correct instance"""
        _, id = self._helper("create BaseModel")
        key = "BaseModel.{}".format(id.strip())
        _, message = self._helper(f"show BaseModel {id}")

        obj = storage.all()[key]
        
        self.assertEqual(message.strip(), str(obj))
        self.assertIn(obj.id, message)
        self.assertIn("BaseModel", message)

    # destroy
    def test_destroy_name_missing(self):
        """test for missing name"""
        _, message = self._helper("destroy")
        self.assertEqual(message.strip(), "** class name missing **")
    
    def test_destroy_wrong_class(self):
        """test for class doesn't exist"""
        _, message = self._helper("destroy FakeClass")
        self.assertEqual(message.strip(), "** class doesn't exist **")
    
    def test_destroy_id_missing(self):
        """test for missing id"""
        _, message = self._helper("destroy BaseModel")
        self.assertEqual(message.strip(), "** instance id missing **")

    def test_destroy_wrong_id(self):
        """passing wrong id means no instance found"""
        _, message = self._helper("destroy BaseModel 187654")
        self.assertEqual(message.strip(), "** no instance found **")
    
    def test_destroy_corret_input(self):
        """test for destory with correct data"""
        _, id = self._helper("create BaseModel")
        key = "BaseModel.{}".format(id.strip())
        
        self.assertIn(key, storage.all())
        self._helper(f"destroy BaseModel {id.strip()}")
        self.assertNotIn(key, storage.all())

    # all
    def test_all_invaild_class(self):
        """test if invaild class were pushed"""
        _, message = self._helper("all FakeClass")
        self.assertEqual(message.strip(), "** class doesn't exist **")
    
    def test_all_with_specific_class(self):
        """retrive specific instance objects"""
        self._helper("create BaseModel")
        self._helper("create User")
        self._helper("create BaseModel")
        self._helper("create User")
        self._helper("create BaseModel")

        _, message = self._helper("all BaseModel")
        list_objects = ast.literal_eval(message)

        objects = []
        for key, obj in storage.all().items():
            if key.split('.')[0] == "BaseModel":
                objects.append(str(obj))

        self.assertEqual(list_objects, objects)

    def test_all(self):
        """retrive all objects"""
        self._helper("create BaseModel")
        self._helper("create User")
        self._helper("create BaseModel")
        self._helper("create User")
        self._helper("create BaseModel")

        _, message = self._helper("all")
        list_objects = ast.literal_eval(message)

        result = []
        objs = storage.all()
        for _, obj in objs.items():
            result.append(str(obj))

        self.assertEqual(list_objects, result)

    # update
    def test_destroy_name_missing(self):
        """test for missing name"""
        _, message = self._helper("destroy")
        self.assertEqual(message.strip(), "** class name missing **")
    
    def test_update_wrong_class(self):
        """test for class doesn't exist"""
        _, message = self._helper("update FakeClass")
        self.assertEqual(message.strip(), "** class doesn't exist **")
    
    def test_update_id_missing(self):
        """test for missing id"""
        _, message = self._helper("update BaseModel")
        self.assertEqual(message.strip(), "** instance id missing **")

    def test_update_wrong_id(self):
        """passing wrong id means no instance found"""
        _, message = self._helper("update BaseModel 187654")
        self.assertEqual(message.strip(), "** no instance found **")
    
    def test_update_attr_name_missed(self):
        """test missed attribute name"""
        _, id = self._helper("create BaseModel")
        _, message = self._helper(f"update BaseModel {id}")
        self.assertEqual(message.strip(), "** attribute name missing **")
    
    def test_update_wrong_id(self):
        """passing wrong id means no instance found"""
        _, id = self._helper("create BaseModel")
        _, message = self._helper(f"update BaseModel {id} age")
        self.assertEqual(message.strip(), "** value missing **")

    def test_update_uneditable_attr(self):
        """test updating uneditable attrs"""
        _, id = self._helper("create BaseModel")
        _, output = self._helper(f"update BaseModel {id} id 10")

        self.assertEqual(output.strip(), "")

    def test_update_data_correct_and_complete(self):
        "tests update"
        _, id = self._helper("create BaseModel")
        self._helper(f"update BaseModel {id} age 22")

        key = f"BaseModel.{id.strip()}"
        obj = storage.all()[key]

        self.assertIn("age", str(obj))

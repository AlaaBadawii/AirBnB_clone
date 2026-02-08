#!/usr/bin/python3
"""class FileStorage module"""
import json


class FileStorage():
    """ class FileStorage that:
        serializes instances to a JSON file and
        deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"

        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}

        for k, obj in self.__objects.items():
            obj_dict[k] = obj.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as fp:
            json.dump(obj_dict, fp)

    def reload(self):
        """Deserializes the JSON file to __objects:

        Reload reads saved data from the JSON file, recreates each object
        as its original class, and stores them in __objects so all
        previously saved users are available in memory.
        """
        try:
            # Local import to avoid circular import
            from models.base_model import BaseModel
            self.classes = {"BaseModel": BaseModel}

            with open(self.__file_path, 'r', encoding='utf-8') as fp:
                obj_dict = json.load(fp)
            for k, v_dict in obj_dict.items():
                class_name = k.split(".")[0]
                cls = self.classes.get(class_name)
                if cls is None:
                    continue
                # create a new instance using saved attr
                new_obj = cls(**v_dict)
                # store the recreated obj in __objects
                self.__objects[k] = new_obj

        except FileNotFoundError:
            # If the JSON file doesn't exist yet, do nothing
            pass

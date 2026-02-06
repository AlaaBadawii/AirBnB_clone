#!/usr/bin/env python3
"""Defines the BaseModel class."""
import uuid
from datetime import datetime


class BaseModel():
    """Base class: defines all common attributes/methods"""
    def __init__(self):
        """ initilizie a new BaseModel instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """ save:
            updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        obj_dict = self.__dict__

        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()

        return obj_dict

    def __str__(self):
        """ __str__:
            prints [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

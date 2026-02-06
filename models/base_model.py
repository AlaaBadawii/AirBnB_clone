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
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        should print:
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__
        )

    def to_dict(self):
        """Public instance methods"""
        dict = {**self.__dict__}  # id created_at updated_at
        dict['__class__'] = type(self).__name__  # BaseModel
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()
        return dict

    def save(self):
        """Public instance methods"""
        self.updated_at = datetime.now()

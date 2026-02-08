#!/usr/bin/python3
"""Defines the BaseModel class."""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """Base class: defines all common attributes/methods"""
    def __init__(self, *args, **kwargs):
        """ initilizie a new BaseModel instance
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue

                if k == "updated_at" or k == "created_at":
                    v = datetime.fromisoformat(v)

                setattr(self, k, v)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

            # if it's a new instance store it at stoarge file
            storage.new(self)

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        obj_dict = self.__dict__.copy()

        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()

        return obj_dict

    def save(self):
        """ save:
            updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.utcnow()
        # save data
        storage.save()

    def __str__(self):
        """ __str__:
            prints [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

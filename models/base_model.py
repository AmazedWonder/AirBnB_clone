#!/usr/bin/python3
"""Base module"""

from models import storage
import uuid
from datetime import datetime


class BaseModel:
    """
    Base Model Class
    """
    def __init__(self, *args, **kwargs):
        if kwargs != {} and kwargs is not None:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                             kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def update_time(self):
        """
        update time
        """
        self.updated_at = datetime.now()

    def save(self):
        """
        save files in json
        """
        self.update_time()
        storage.save()

    def to_dict(self):
        """
        Creates a dictionary with object attributes
        adds a key for the class name used to create
        object from dictionary by checking class key
        """
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = type(self).__name__
        dict_obj['created_at'] = dict_obj["created_at"].isoformat()
        dict_obj['updated_at'] = dict_obj["updated_at"].isoformat()
        return dict_obj

    def __str__(self):
        """Returns the string representation
        of BaseModel instance.
        """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

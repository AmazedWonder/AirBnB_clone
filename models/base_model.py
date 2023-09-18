#!/usr/bin/python3
"""Base module"""

from models import storage
import uuid
import datetime


class BaseModel:
    """
    Base Model Class
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.datetime.strptime(value,
                                                       "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def update_time(self):
        """
        update time
        """
        self.updated_at = datetime.datetime.now()

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
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        dict_obj['__class__'] = self.__class__.__name__
        return dict_obj

    def __str__(self):
        """
        string representation
        """
        class_name = self.__class__.__name__
        id_obj = self.id
        dict_obj = str(self.__dict__)
        return f"[{class_name}] ({id_obj}) {dict_obj} "

    def __repr__(self):
        """
        Return string representation of BaseModel class
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

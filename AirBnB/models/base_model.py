#!/usr/bin/python3

from models import storage
import uuid
import datetime
# import json


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def update_time(self):
        self.updated_at = datetime.datetime.now()

    def save(self):
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


# # Specify the actual path to your JSON file
#     file_path = 'C:/Users/hp/PycharmProjects/pythonProject/AirBnB/models/file.json'
#
#     # Open the JSON file in read mode using a file object
#     with open(file_path, 'r') as file:
#         # Use the file object to load the JSON datar
#         data = json.load(file)
#
#     # Now you can work with the loaded JSON data
#     # For example, print the contents of the JSON file
#     print(data)

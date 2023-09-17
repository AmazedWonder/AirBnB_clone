#!/usr/bin/python3
"""Class named FileStorage that provides methods for managing
   objects and storing them in a JSON file
"""
import datetime
import json
import os


class FileStorage:
    """private class variable that represents the
       path to the JSON file where objects will be stored
       And private class variable that holds a dictionary of objects.
    """
    __file_path = "file.json"

    __objects = {}

    def all(self):
        """A method that returns all objects
        stored in the __objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """A method that adds a new object to the __objects dictionary.
           The object is stored with a key that combines the object's class
           name and its ID.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """A method that saves the objects in the __objects
           dictionary to the JSON file specified by __file_path.
        """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            dic = {key: val.to_dict() for key,
                   val in FileStorage.__objects.items()}
            json.dump(dic, file)

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review}

        return classes

    def reload(self):
        """reloads the objects from the JSON file specified
           by __file_path and updates the __objects dictionary.
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf8') as file:
                file_content = file.read()
                if not file_content:
                    loaded_objects = {}
                else:
                    loaded_objects = json.load(file_content)
            loaded_objects = {key: self.classes()[val["__class__"]](**val)
                              for key, val in loaded_objects.items()}
            FileStorage.__objects = loaded_objects
        except Exception as e:
            print(f"Error loading JSON file: {str(e)}")

    def attributes(self):
        """ returns a dictionary of valid
        attributes and their types for each class.
            The attributes include id, created_at,
            and updated_at for BaseModel;
            email, password, first_name, and
            last_name for User; name for State,
            City, and Amenity; and specific
            attributes for Place and Review.
        """
        attributes = {
            "BaseModel": {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime},
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "Last_name": str},
            "State": {
                "name": str},
            "City": {
                "state_id": str,
                "name": str},
            "Amenity": {
                "name": str},
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list},
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str},
        }
        return attributes

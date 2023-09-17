#!/usr/bin/python3
import unittest
import os
from models.user import User
from models.state import State
from models.city import City
from models.engine.file_storage import FileStorage
# from models.base_model import BaseModel
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review


class FileStorageTest(unittest.TestCase):
    def setUp(self):
        """used to set up the necessary objects"""
        self.storage = FileStorage()
        self.user = User()
        self.state = State()
        self.city = City()

    def tearDown(self):
        """used to clean up any artifacts created during the tests."""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """tests the all method of the FileStorage class by checking
           if the returned objects are of the correct type and if the
           objects are added correctly.
        """
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(len(objects), 0)

        self.storage.new(self.user)
        self.storage.new(self.state)
        self.storage.new(self.city)

        objects = self.storage.all()
        self.assertEqual(len(objects), 3)
        self.assertIn(f"User.{self.user.id}", objects)
        self.assertIn(f"State.{self.state.id}", objects)
        self.assertIn(f"City.{self.city.id}", objects)

    def test_save_reload(self):
        """tests the save and reload methods by creating new objects,
           saving them to a file, reloading the objects from the file,
           and checking if the reloaded objects match the original objects.
        """
        self.storage.new(self.user)
        self.storage.new(self.state)
        self.storage.new(self.city)

        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        objects = new_storage.all()
        self.assertEqual(len(objects), 3)
        self.assertIn(f"User.{self.user.id}", objects)
        self.assertIn(f"State.{self.state.id}", objects)
        self.assertIn(f"City.{self.city.id}", objects)

    def test_attributes(self):
        """tests the attributes method by checking if the returned attributes
           dictionary contains the expected keys and attributes for each class.
        """
        attributes = self.storage.attributes()
        self.assertIsInstance(attributes, dict)
        self.assertIn("BaseModel", attributes)
        self.assertIn("User", attributes)
        self.assertIn("State", attributes)
        self.assertIn("City", attributes)

        base_model_attrs = attributes["BaseModel"]
        self.assertIn("id", base_model_attrs)
        self.assertIn("created_at", base_model_attrs)
        self.assertIn("updated_at", base_model_attrs)

        user_attrs = attributes["User"]
        self.assertIn("email", user_attrs)
        self.assertIn("password", user_attrs)
        self.assertIn("first_name", user_attrs)
        self.assertIn("last_name", user_attrs)

        state_attrs = attributes["State"]
        self.assertIn("name", state_attrs)

        city_attrs = attributes["City"]
        self.assertIn("state_id", city_attrs)
        self.assertIn("name", city_attrs)


if __name__ == '__main__':
    unittest.main()






# import unittest
# import os
# import models
#
# from models.engine.file_storage import FileStorage
# from models.base_model import BaseModel
# from models.user import User
# from models.amenity import Amenity
# from models.state import State
# from models.city import City
# from models.place import Place
# from models.review import Review
#
#
# class TestFileStorage(unittest.TestCase):
#     def setUp(self):
#         self.b = BaseModel()
#         self.u = User()
#         self.a = Amenity()
#         self.s = State()
#         self.c = City()
#         self.p = Place()
#         self.r = Review()
#         self.storage = FileStorage()
#         self.storage.save()
#         if os.path.exits("file.json"):
#             pass
#         else:
#             os.mknod("file.json")
#
#     def tearDown(self):
#         del self.b
#         del self.u
#         del self.a
#         del self.s
#         del self.c
#         del self.p
#         del self.r
#         del self.storage
#         if os.path.exits("file.json"):
#             os.remove("file.json")
#
#     def test_all(self):
#         val = self.storage.all()
#         self.asserIsNotNone(val)
#         self.assertEqual(type(val), dict)
#
#     def test_new(self):
#         val = self.storage.all()
#         self.u.name = "Neima"
#         self.u.id = "2121"
#         val2 = self.storage.new(self.u)
#         key = "{}.{}".format(self.u.__class__.__name__, self.u.id)
#         self.assertIsNotNone(val[key])
#
#
# if __name__ == "__main__":
#     unittest.main()

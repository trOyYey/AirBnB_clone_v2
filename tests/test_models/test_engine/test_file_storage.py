#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):

    def setUp(self):
        self.file_storage = FileStorage()
        self.base_model = BaseModel()
        self.user = User()
        self.place = Place()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.review = Review()

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_new_object_added_to_objects(self):
        self.file_storage.new(self.base_model)
        self.assertIn(f"BaseModel.{self.base_model.id}",
                      self.file_storage.all())

    def test_save_method_creates_file(self):
        self.file_storage.new(self.base_model)
        self.file_storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            data = f.read()
            self.assertTrue(data.strip())

    def test_all_method_returns_dict(self):
        result = self.file_storage.all()
        self.assertIsInstance(result, dict)

    def test_all_method_returns_filtered_dict(self):
        self.file_storage.new(self.base_model)
        self.file_storage.new(self.user)
        self.file_storage.new(self.place)
        result = self.file_storage.all(User)
        self.assertIn("User.{}".format(self.user.id), result)
        self.assertNotIn("BaseModel.{}".format(self.base_model.id), result)

    def test_delete_method_removes_object(self):
        self.file_storage.new(self.base_model)
        self.file_storage.new(self.user)
        self.file_storage.delete(self.base_model)
        self.assertNotIn("BaseModel.{}".format(self.base_model.id),
                         self.file_storage.all())

    def test_reload_method_loads_data(self):
        self.file_storage.new(self.base_model)
        self.file_storage.save()
        new_file_storage = FileStorage()
        new_file_storage.reload()
        result = new_file_storage.all()
        self.assertIn("BaseModel.{}".format(self.base_model.id), result)

    def test_reload_method_handles_nonexistent_file(self):
        self.file_storage.reload()


if __name__ == '__main__':
    unittest.main()

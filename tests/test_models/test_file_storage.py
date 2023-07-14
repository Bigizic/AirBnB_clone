#!/usr/bin/python3
"""A uniitest moule for FileStorage class

This module contains test for:
    1. if the file is a .json extension
    2. if the new() creates the key for the dict and sets it in objects
        with the created key. Key should be in a specific format
    3. if the save() sucessfully serialize the objects and saves to the
        json file path
    4. if reload succesffuly reloads the objects from the json file and
        if it reloads it in the correct format
"""
import unittest


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import json


class Test_file_storage_foundations(unittest.TestCase):
    """File storage tests
    """

    # test if the file being created is a .json file
    def test_correct_file_extension(self):
        m_s = FileStorage()
        self.assertEqual(m_s._FileStorage__file_path.endswith('.json'), True)

    # test if the new() method returns the objects in the correct format
    def test_new_methods(self):
        my_store = FileStorage()
        obj = BaseModel()
        my_store.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertEqual(key in my_store._FileStorage__objects, True)
        self.assertEqual(my_store._FileStorage__objects[key], obj)

    # test if the save() serialzies the objects and saves it to the json
        # file path
    def test_save_method(self):
        my_store = FileStorage()
        obj = BaseModel()
        my_store.new(obj)
        my_store.save()

        # Opens the file for reading 
        with open(my_store._FileStorage__file_path, "r") as open_file:
            data = open_file.read()
            # check if the data saved in the file path is not empty
             # returns truw as it's not equal to empty object
            self.assertNotEqual(data, "")

    # test if the reload() sucessfully reloads from the file path and
        # sets the __objects to the data it was able to read from the
        # file
    def test_reload_method(self):
        my_store = FileStorage()
        obj = BaseModel()
        my_store.new(obj)
        my_store.save()
        my_store.reload()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertEqual(key in my_store._FileStorage__objects, True)
        self.assertEqual(
                my_store._FileStorage__objects[key].__class__.__name__,\
                        "BaseModel")

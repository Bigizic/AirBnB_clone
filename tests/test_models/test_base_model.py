#!/usr/bin/python3
"""Unittest module for base class

This module contains test for:
    1. if the id returns a valid string and if the id type is a string
    2. if the created at returns the correct format
    3. if the updated_at returns the correct format
    4. if str prints the correct string format
    5. if to_dict returns a dictionary containing all keys/values of
        __dict__ of the instance
    6. if *args is being used or not
"""
import unittest


from models.base_model import BaseModel
from datetime import datetime


class Test_base_model_foundations(unittest.TestCase):
    """Foundations test i.e easier tests cases
    """

    # test if the id is of str (string) type
    def test_valid_id_type(self):
        id_value = BaseModel()
        self.assertIsInstance(id_value.id, str, None)

    # test if created_at is datetime type before a call to the to_dict()
    def test_createdat_type(self):
        created_at_value = BaseModel()
        self.assertIsInstance(created_at_value.created_at, datetime, None)

    # test if updated_at is datetime type before a call to the to_dict()
    def test_updatedat_type(self):
        updated_at_value = BaseModel()
        self.assertIsInstance(updated_at_value.updated_at, datetime, None)

    # test if updated_at is str type after making a call to the to_dict()
    def test_update_at_type_to_dict(self):
        updated = BaseModel()
        val = updated.to_dict()
        self.assertIsInstance(val['updated_at'], str, None)

    # test if created_at is str type after making a call to the to_dict()
    def test_created_at_type_to_dict(self):
        created = BaseModel()
        val = created.to_dict()
        self.assertIsInstance(val['created_at'], str, None)

    # test if updated_at returns the correct format for the date.time
    def test_updated_at_correct_format(self):
        base_model = BaseModel()
        u_str = base_model.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        u_format = self.validate_datetime_format(u_str)
        self.assertTrue(u_format, "invalid format")

    # test if created_at returns the correct format for the date.time
    def test_created_at_correct_fromat(self):
        base_model = BaseModel()
        c_str = base_model.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        c_format = self.validate_datetime_format(c_str)
        self.assertTrue(c_format, "invalid format")

    # validates created_at and updated_at date.time formats
    def validate_datetime_format(self, datetime_str):
        try:
            datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%f")
            return True
        except ValueError:
            return False

    def test_str_correct_fromat(self):
        my_model = BaseModel()
        dct = str(my_model.__dict__)
        cla = my_model.__class__.__name__
        expected = "[{}] ({}) {}" .format(cla, my_model.id, dct)
        self.assertEqual(str(my_model), expected, None)

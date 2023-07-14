#!/usr/bin/python3
"""Unittest module for state class
This module contains test for:
1.Test the type of the id is string.
2.Test the type of name is string.
3.Test two states have different created at.
4.Test two states have different updated at.
5.Test two states have different id.
6.Test the type of the created at is datetime.
7.Test the type of the updated at is datetime.
"""
import unittest
from models.state import State
from datetime import datetime


class Test_State_foundation(unittest.TestCase):
    """Foundation tests easiest test cases"""

    def test_id_type(self):
        self.assertEqual(str, type(State().id))

    def test_name_type(self):
        self.assertEqual(str, type(State().name))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_two_states_with_different_ids(self):
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)

    def test_two_states_with_different_created_at(self):
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.created_at, s2.created_at)

    def test_two_states_with_diff_updated_at(self):
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.updated_at, s2.updated_at)

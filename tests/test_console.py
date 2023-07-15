#!/usr/bin/python3
"""A unittest module for command line intepreter

This test module contain tests for:
    1. if the do_quit() succesfully exit the program
    2. if the do_EOF() succesfully exit the program
    3. if the emptyline() doesn't execute anything
    4. if the do_create() creates a new instance of the Class given
        4a. if the do_create() raises a msg while trying to create
            a class that doesn't exist in the program
        4b. if the do_create() raises a msg when the command is entered
            without any class name
        4c. if the do_create() receives an infinity number as the arg and
            if it sucessfully raise a msg when given infinity number

    5. if the do_show() prints the string representation of an instance
        based on the class name and the id

        5a. if the do_show() raises a msg when it's called alone, without
            a class name
        5b. if the do_show() raises a msg when a class that doesn't exist
            is called along the show command
        5c. if the do_show() raises a msg when a class that exist is only
            passed as the argument but no id
        5d. if the do_show() raises a msg when a class that exist is
            passed along side an id that doesn't exist

    6. if the do_destory() deletes an instance based on the class name and
        id, also save the changes into the Json file

        6a. if the do_destroy() raises a msg when it's called alone,
            without a class name
        6b. if the do_destroy() raises a msg when a class that doesn't
            exist is called along the command
        6c. if the do_destroy() raises a msg when a class that exist is
            only passed as the argument but no id
        6d. if the do_destroy() raises a msg when a class that exist is
            passed along side an id that doesn't exist

    7. if the do_all() prints all string representation of all instances
        based or not on the class name

        7a. if the do_all() prints all instances when the do_all() doesn't
            receive any argument along it
        7b. if the do_all() prints only instances of the class name when
            the do_all() is passed along side a class name
        7c. if the do_all() raises a msg when a class name that doesn't
            exist is passed along side the all() command.

    8. if the do_update() updates an instance based on the class name
        and id by adding or updating attribute

        8a. if the do_update() raises a msg whem there's no argument
            passed along side it's command
        8b. if the do_update() raises a msg when the class name passed
            along side the the do_update() doesn't exist
        8c. if the do_update() raises a msg when a class that exist is
            passed along side the do_update() but the next argument
            after the class name is empty
        8d. if the do_update() raises a msg when a class name that exist
            and an id is passed along the class name, if the id doesn't
            exist but it begins a digit is prints "no instance found"
            if the id doesn't exist but it begins with a string
            it prints "attribute name missing" if the id exist it prints
            "attribute name missing" to indicate it needs an attribute

        8e. if the do_update() raises a msg when the class name exist and
            id exist and the attribute name is not a dict, i.e it has
            no value only key
        8f. if the attribute name passed to the do_update() is in:
            id, created_at, or updated_at, it shouldn't do anything

        8g. A check if the attribute passed to the do_update() has a
        value and it's been added to that particular instance
        8h. A check if the attribute passed to the do_update() has a value
            and it's beiong updated, that means the value only gets
            updated, because the object already contain the key

ALL TESTS WOULD BE TESTED WITH INFINITY AND DIFFERENT TYPES AS ARGUMENTS
ALONGSIDE COMMANDS
"""

from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from console import HBNBCommand
from unittest.mock import patch
from models.place import Place
from models.state import State
from models.city import City
from models.user import User
from models import storage
from io import StringIO
import unittest
import json
import cmd


class Test_console(unittest.TestCase):
    """Test foundations
        @path('sys.stdout', new_callable=StringIO) is used to capture the
        output printed to the standard output during the execution of each
        command
    """
    @patch('sys.stdout', new_callable=StringIO)
    # test case if do_quit succesfully exit the program
    def test_quit_command(self, mock_stdout):
        console = HBNBCommand()
        self.assertTrue(console.do_quit(""))
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    # test case if do_EOF successfulyy exit the program
    def test_eof_command(self, mock_stdout):
        console = HBNBCommand()
        self.assertTrue(console.do_EOF(""))
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    #test case if the emptyline() doesn't execute anything
    def test_emptyline_command(self, mock_stdout):
        console = HBNBCommand()
        self.assertFalse(console.emptyline(), "")
        self.assertFalse(console.emptyline(), None)

    @patch('sys.stdout', new_callable=StringIO)
    # test if do_create creates a new instance of allclasses
    def test_create_command(self, mock_stdout):
        console = HBNBCommand()
        classes = [BaseModel, User, Place, City, State, Amenity, Review]
        for model_class in classes:
            class_name = model_class.__name__
            console.do_create(class_name)
            created_instance = console.created_model
            self.assertIsInstance(created_instance, model_class)

    @patch('sys.stdout', new_callable=StringIO)
    # test if do_create raises a msg while trying to create a class that
    # doesn't exist
    def test_create_class_not_exist(self, mock_stdout):
        console = HBNBCommand()
        classes = ["Hello", None, 3, 3.142, float('inf'), -float('inf'),
                    True, False]
        expected = "** class doesn't exist **\n"
        for model_cls in classes:
            console.do_create(str(model_cls))
            self.assertEqual(mock_stdout.getvalue(), expected)
            # ensure that mock_stdout buffer is reset to it's intial state
            # before the next iteration of the loop
            mock_stdout.seek(0)
            mock_stdout.truncate(0)

    @patch('sys.stdout', new_callable=StringIO)
    # test if do_create raises a msg when the command is entered
    # without any class name
    def test_create_class_name_missing(self, mock_stdout):
        console = HBNBCommand()
        expected = "** class name missing **\n"
        console.do_create("")
        self.assertEqual(mock_stdout.getvalue(), expected)


    @patch('sys.stdout', new_callable=StringIO)
    # test if the do_show() prints the string representation of an
    # instance based on the class name and the id
    def test_show_command(self, mock_stdout):
        console = HBNBCommand()
        classes = [BaseModel, User, Place, City, State, Amenity, Review]
        for model_class in classes:
            class_name = model_class.__name__
            console.do_create(class_name)
            created_id = mock_stdout.getvalue().strip()
            mock_stdout.seek(0)
            mock_stdout.truncate(0)

            # call do_show
            arg = "{} {}".format(class_name, created_id)
            console.do_show(arg)
            dct = console.created_model.__dict__
            expected = "[{}] ({}) {}" .format(class_name, created_id, dct)
            self.assertEqual(mock_stdout.getvalue().strip(), expected)
            mock_stdout.seek(0)
            mock_stdout.truncate(0)

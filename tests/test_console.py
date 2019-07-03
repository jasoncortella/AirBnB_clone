#!/usr/bin/python3
""" unittest for console """

import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import models
import os
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class test_console_help_messages(unittest.TestCase):
    """ define unittest for testing the help command within hbnb console """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_only_help(self):
        check = "Documented commands (type help <topic>):\n"
        check += "========================================\n"
        check += "EOF  all  create  destroy  help  quit  show  update"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
        self.assertEqual(check, output.getvalue().strip())

    def test_help_quit(self):
        check = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
        self.assertEqual(check, output.getvalue().strip())

    def test_help_create(self):
        check = 'create a new class instance, saves it to JSON, print its id'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
        self.assertEqual(check, output.getvalue().strip())

    def test_help_EOF(self):
        check = "EOF command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
        self.assertEqual(check, output.getvalue().strip())

    def test_help_show(self):
        check = "show command to print the str representation of an instance"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
        self.assertEqual(check, output.getvalue().strip())

    def test_help_destroy(self):
        check = "destroy command to delete instance based on class name and id"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
        self.assertEqual(check, output.getvalue().strip())

    def test_help_all(self):
        check = "all command to print all string representations of instances"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
        self.assertEqual(check, output.getvalue().strip())

    def test_help_update(self):
        check = "update command to update an instance based on the class name"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
        self.assertEqual(check, output.getvalue().strip())

    def test_help_invalid(self):
        check = "*** No help on invalid"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help invalid"))
        self.assertEqual(check, output.getvalue().strip())

class test_console_create_command(unittest.TestCase):
    """ define unittest for testing the hbnb console create command """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_create_only(self):
        check = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
        self.assertEqual(check, output.getvalue().strip())

    def test_create_invalid(self):
        check = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create invalid"))
        self.assertEqual(check, output.getvalue().strip())

    def test_create_BaseModel(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn("BaseModel", output.getvalue().strip())

    def test_create_User(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn("User", output.getvalue().strip())

    def test_create_State(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn("State", output.getvalue().strip())

    def test_create_City(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn("City", output.getvalue().strip())

    def test_create_Place(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn("Place", output.getvalue().strip())

    def test_create_Amenity(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn("Amenity", output.getvalue().strip())

    def test_create_Review(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn("Review", output.getvalue().strip())

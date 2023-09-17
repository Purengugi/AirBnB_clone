<<<<<<< HEAD
#!/usr/bin/python3
"""Defines unittests for console.py.

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
=======
ontains class TestConsole.
>>>>>>> 07a4d37cea5158a8bd015dd84f3532d91e1c264b
"""
import os
import sys
import unittest
<<<<<<< HEAD
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help messages of the HBNB command interpreter."""

    def test_help_quit(self):
        h = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_create(self):
        h = ("Usage: create <class>\n        "
             "Create a new class instance and print its id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_EOF(self):
        h = "EOF signal to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_show(self):
        h = ("Usage: show <class> <id> or <class>.show(<id>)\n        "
             "Display the string representation of a class instance of"
             " a given id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_destroy(self):
        h = ("Usage: destroy <class> <id> or <class>.destroy(<id>)\n        "
             "Delete a class instance of a given id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_all(self):
        h = ("Usage: all or all <class> or <class>.all()\n        "
             "Display string representations of all instances of a given class"
             ".\n        If no class is specified, displays all instantiated "
             "objects.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_count(self):
        h = ("Usage: count <class> or <class>.count()\n        "
             "Retrieve the number of instances of a given class.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_update(self):
        h = ("Usage: update <class> <id> <attribute_name> <attribute_value> or"
             "\n       <class>.update(<id>, <attribute_name>, <attribute_value"
             ">) or\n       <class>.update(<id>, <dictionary>)\n        "
             "Update a class instance of a given id by adding or updating\n   "
             "     a given attribute key/value pair or dictionary.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help(self):
        h = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(h, output.getvalue().strip())


class TestHBNBCommand_exit(unittest.TestCase):
    """Unittests for testing exiting from the HBNB command interpreter."""

    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommand_create(unittest.TestCase):
    """Unittests for testing create from the HBNB command interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}
=======
import cmd
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import os
import json


class TestHBNBCommand(unittest.TestCase):
    """
    Contains tests for console.
    """
    def setUp(self):
        """allocating resources"""
        models.storage._FileStorage__objects = {}

    def test_do_create_Base(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "BaseModel"
            HBNBCommand().onecmd(f"create {cls_name}")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_Base2(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "BaseModel"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_User(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "User"
            HBNBCommand().onecmd(f"create {cls_name}")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_User2(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "User"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_Amen(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Amenity"
            HBNBCommand().onecmd(f"create {cls_name}")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_Amen2(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Amenity"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_City(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "City"
            HBNBCommand().onecmd(f"create {cls_name}")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_City2(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "City"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_Place(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Place"
            HBNBCommand().onecmd(f"create {cls_name}")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_Place2(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Place"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_Review(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Review"
            HBNBCommand().onecmd(f"create {cls_name}")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_Review2(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Review"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_State(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "State"
            HBNBCommand().onecmd(f"create {cls_name}")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_State2(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "State"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_arg1(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f1:
            HBNBCommand().onecmd(f"create")
            output1 = f1.getvalue().strip()
            expected_msg1 = "** class name missing **"
            self.assertEqual(expected_msg1, output1)

    def test_do_create_arg2(self):
        with patch('sys.stdout', new=StringIO()) as f2:
            cls_name = "MyModel"
            HBNBCommand().onecmd(f"create {cls_name}")
            output2 = f2.getvalue().strip()
            expected_msg2 = "** class doesn't exist **"
            self.assertEqual(expected_msg2, output2)

    def test_do_count_empty(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "User"
            HBNBCommand().onecmd(f"count {cls_name}")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            self.assertEqual(expected_count, int(output))

    def test_do_count_Base(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "BaseModel"
            HBNBCommand().onecmd(f"create {cls_name}")
            HBNBCommand().onecmd(f"count {cls_name}")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_Base2(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "User"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            HBNBCommand().onecmd(f"{cls_name}.count()")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_User(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "User"
            HBNBCommand().onecmd(f"create {cls_name}")
            HBNBCommand().onecmd(f"count {cls_name}")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_User2(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "User"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            HBNBCommand().onecmd(f"{cls_name}.count()")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_Amen(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Amenity"
            HBNBCommand().onecmd(f"create {cls_name}")
            HBNBCommand().onecmd(f"count {cls_name}")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_Amen2(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Amenity"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            HBNBCommand().onecmd(f"{cls_name}.count()")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_City(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "City"
            HBNBCommand().onecmd(f"create {cls_name}")
            HBNBCommand().onecmd(f"count {cls_name}")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_City2(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "City"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            HBNBCommand().onecmd(f"{cls_name}.count()")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_Place(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Place"
            HBNBCommand().onecmd(f"create {cls_name}")
            HBNBCommand().onecmd(f"count {cls_name}")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_Place2(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Place"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            HBNBCommand().onecmd(f"{cls_name}.count()")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_Review(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Review"
            HBNBCommand().onecmd(f"create {cls_name}")
            HBNBCommand().onecmd(f"count {cls_name}")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_Review2(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Review"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            HBNBCommand().onecmd(f"{cls_name}.count()")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_State(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "State"
            HBNBCommand().onecmd(f"create {cls_name}")
            HBNBCommand().onecmd(f"count {cls_name}")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_State2(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "State"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            HBNBCommand().onecmd(f"{cls_name}.count()")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_show_empty(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "City"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"show {cls_name} {cls_id}")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_arg1(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f1:
            HBNBCommand().onecmd(f"show")
            output1 = f1.getvalue().strip()
            expected_msg1 = "** class name missing **"
            self.assertEqual(expected_msg1, output1)

    def test_do_show_arg2(self):
        """test do_show"""
        with patch('sys.stdout', new=StringIO()) as f2:
            cls_name = "MyModel"
            HBNBCommand().onecmd(f"show {cls_name}")
            dictionary = models.storage.all()
            output2 = f2.getvalue().strip()
            expected_msg2 = "** class doesn't exist **"
            self.assertEqual(expected_msg2, output2)

    def test_do_show_arg3(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f3:
            cls_name = "Amenity"
            HBNBCommand().onecmd(f"show {cls_name}")
            dictionary = models.storage.all()
            output3 = f3.getvalue().strip()
            expected_msg3 = "** instance id missing **"
            self.assertEqual(expected_msg3, output3)

    def test_do_show_arg4(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f4:
            cls_name = "Place"
            HBNBCommand().onecmd(f"show {cls_name} My_First_Model")
            output4 = f4.getvalue().strip()
            expected_msg4 = "** no instance found **"
            self.assertEqual(expected_msg4, output4)

    def test_do_show_Base(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "BaseModel"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"create {cls_name}")
                HBNBCommand().onecmd(f"show {cls_name} {cls_id}")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_Base2(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            dictionary = models.storage.all()
            cls_name = "BaseModel"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"{cls_name}.create()")
                HBNBCommand().onecmd(f"{cls_name}.show({cls_id})")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_User(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "User"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"create {cls_name}")
                HBNBCommand().onecmd(f"show {cls_name} {cls_id}")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_User2(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "User"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"{cls_name}.create()")
                HBNBCommand().onecmd(f"{cls_name}.show({cls_id})")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_Amen(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "Amenity"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"create {cls_name}")
                HBNBCommand().onecmd(f"show {cls_name} {cls_id}")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_Amen2(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "Amenity"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"{cls_name}.create()")
                HBNBCommand().onecmd(f"{cls_name}.show({cls_id})")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_City(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "City"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"create {cls_name}")
                HBNBCommand().onecmd(f"show {cls_name} {cls_id}")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_City2(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "City"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"{cls_name}.create()")
                HBNBCommand().onecmd(f"{cls_name}.show({cls_id})")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_Place(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "Place"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"create {cls_name}")
                HBNBCommand().onecmd(f"show {cls_name} {cls_id}")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_Place2(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "Place"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"{cls_name}.create()")
                HBNBCommand().onecmd(f"{cls_name}.show({cls_id})")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_Review(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "Review"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"create {cls_name}")
                HBNBCommand().onecmd(f"show {cls_name} {cls_id}")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_Review2(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "Review"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"{cls_name}.create()")
                HBNBCommand().onecmd(f"{cls_name}.show({cls_id})")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_State(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "State"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"create {cls_name}")
                HBNBCommand().onecmd(f"show {cls_name} {cls_id}")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_State2(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "State"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} str({value})"
                HBNBCommand().onecmd(f"{cls_name}.create()")
                HBNBCommand().onecmd(f"{cls_name}.show({cls_id})")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_destroy_Base(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "BaseModel"
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "BaseModel"
            HBNBCommand().onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_Base2(self):
        """test destroy"""
        id = ""
        cls_name = "BaseModel"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls_name}.destroy({id})")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_User(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "User"
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "User"
            HBNBCommand().onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_User2(self):
        """test destroy"""
        id = ""
        cls_name = "User"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls_name}.destroy({id})")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_Amen(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Amenity"
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Amenity"
            HBNBCommand().onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_Amen2(self):
        """test destroy"""
        id = ""
        cls_name = "Amenity"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls_name}.destroy({id})")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_City(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "City"
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "City"
            HBNBCommand().onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_City2(self):
        """test destroy"""
        id = ""
        cls_name = "City"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls_name}.destroy({id})")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_Place(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Place"
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Place"
            HBNBCommand().onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_Place2(self):
        """test destroy"""
        id = ""
        cls_name = "Place"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls_name}.destroy({id})")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_Review(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Review"
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Review"
            HBNBCommand().onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_Review2(self):
        """test destroy"""
        id = ""
        cls_name = "BaseModel"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls_name}.destroy({id})")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_State(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "State"
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "State"
            HBNBCommand().onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_State2(self):
        """test destroy"""
        id = ""
        cls_name = "BaseModel"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls_name}.destroy({id})")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_arg1_miss(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class name missing **")

    def test_do_destroy_arg1_miss2(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f".destroy()")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class name missing **")

    def test_do_destroy_arg1_incorrect(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy hi")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class doesn't exist **")

    def test_do_destroy_arg1_incorrect2(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"hi.destroy()")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class doesn't exist **")

    def test_do_destroy_arg2_miss(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** instance id missing **")

    def test_do_destroy_arg2_miss2(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(obj.precmd(f"BaseModel.destroy()"))
            output = f.getvalue().strip()
            self.assertEqual(output,  "** instance id missing **")

    def test_do_destroy_arg2_incorrect(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel 123")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** no instance found **")

    def test_do_destroy_arg2_incorrect2(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.destroy(123)")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** no instance found **")

    def test_do_all(self):
        """test all"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all")
            output = f.getvalue().strip()
            self.assertEqual(output,  "[]")
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "State"
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"State.{id}"]) + '"]'
            self.assertEqual(rep,  output)

    def test_do_all_Base(self):
        """test all"""
        id = ""
        cls1_name = "BaseModel"
        cls2_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls1_name}.all()")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)

    def test_do_all_User(self):
        """test all"""
        id = ""
        cls1_name = "User"
        cls2_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls1_name}.all()")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)

    def test_do_all_Amen(self):
        """test all"""
        id = ""
        cls1_name = "Amenity"
        cls2_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls1_name}.all()")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)

    def test_do_all_City(self):
        """test all"""
        id = ""
        cls1_name = "City"
        cls2_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls1_name}.all()")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)

    def test_do_all_Place(self):
        """test all"""
        id = ""
        cls1_name = "Place"
        cls2_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls1_name}.all()")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)

    def test_do_all_Review(self):
        """test all"""
        id = ""
        cls1_name = "Review"
        cls2_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls1_name}.all()")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)

    def test_do_all_State(self):
        """test all"""
        id = ""
        cls1_name = "State"
        cls2_name = "User"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls1_name}.all()")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)

    def test_do_all_Err(self):
        """test all"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all No")
            output = f.getvalue().strip()
            self.assertEqual("** class doesn't exist **", output)

    def test_do_update_Base(self):
        """test update"""
        id = ""
        cls1_name = "BaseModel"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} name "mariam"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mariam")

    def test_do_update_Base2(self):
        """test update"""
        id = ""
        cls1_name = "BaseModel"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, name, "mar")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mar")

    def test_do_update_Base3(self):
        """test update"""
        id = ""
        cls1_name = "BaseModel"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            att_val = {"name": "mariam ibrahim"}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(att_val)})')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mariam ibrahim")

    def test_do_update_Base4(self):
        """test update"""
        id = ""
        cls1_name = "BaseModel"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            att_val = {"name": 'mariam ibrahim'}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(att_val)})')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mariam ibrahim")

    def test_do_update_User(self):
        """test update"""
        id = ""
        cls1_name = "User"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} first_name "mar"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].first_name, "mar")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} password "mar"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].password, "mar")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} last_name "ma"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].last_name, "ma")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} email "mar"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].email, "mar")

    def test_do_update_User2(self):
        """test update"""
        id = ""
        cls1_name = "User"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, first_name, m)')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].first_name, "m")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, last_name, r)')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].last_name, "r")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, email, i)')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].email, "i")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, password, m)')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].password, "m")

    def test_do_update_User3(self):
        """test update"""
        id = ""
        cls1_name = "User"
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand()
            obj.onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            att_val = {"first_name": "mariam", "last_name": "nimo",
                       "email": "lol", "password": "hi"}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(att_val)})')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].first_name, "mariam")
            self.assertEqual(dictionary[key].last_name, "nimo")
            self.assertEqual(dictionary[key].email, "lol")
            self.assertEqual(dictionary[key].password, "hi")

    def test_do_update_Amen(self):
        """test update"""
        id = ""
        cls1_name = "Amenity"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} name "mam"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mam")

    def test_do_update_Amen2(self):
        """test update"""
        id = ""
        cls1_name = "Amenity"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, name, m)')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "m")

    def test_do_update_Amen3(self):
        """test update"""
        id = ""
        cls1_name = "Amenity"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            att_val = {"name": "mariam ibrahim"}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(att_val)})')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mariam ibrahim")

    def test_do_update_City(self):
        """test update"""
        id = ""
        cls1_name = "City"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} name "mar"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mar")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} state_id "989"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].state_id, "989")

    def test_do_update_City2(self):
        """test update"""
        id = ""
        cls1_name = "City"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, name, m)')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "m")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, state_id "99")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].state_id, "99")

    def test_do_update_City3(self):
        """test update"""
        id = ""
        cls1_name = "City"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            att_val = {"name": "mariam ibrahim", "state_id": "989"}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(att_val)})')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mariam ibrahim")
            self.assertEqual(dictionary[key].state_id, "989")

    def test_do_update_Place(self):
        """test update"""
        id = ""
        cls1_name = "Place"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} city_id "mar"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].city_id, "mar")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} user_id "mar"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].user_id, "mar")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} name "mar"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mar")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} description "mar"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].description, "mar")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} number_rooms "7"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].number_rooms, 7)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} number_rooms "7.5"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].number_rooms, 7)
            atr = "number_bathrooms"
            HBNBCommand().onecmd(f'update {cls1_name} {id} {atr} "7"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].number_bathrooms, 7)
        with patch('sys.stdout', new=StringIO()) as f:
            atr = "number_bathrooms"
            HBNBCommand().onecmd(f'update {cls1_name} {id} {atr} "7.5"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].number_bathrooms, 7)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} max_guest "7"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].max_guest, 7)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} max_guest "7.5"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].max_guest, 7)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} price_by_night "7"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].price_by_night, 7)
        with patch('sys.stdout', new=StringIO()) as f:
            atr = "price_by_night"
            HBNBCommand().onecmd(f'update {cls1_name} {id} {atr} "7.5"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].price_by_night, 7)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} latitude "7"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].latitude, 7.0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} longitude "7.5"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].longitude, 7.5)

    def test_do_update_Place2(self):
        """test update"""
        id = ""
        cls1_name = "Place"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, city_id "mar")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].city_id, "mar")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, user_id "m")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].user_id, "m")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, name "mariam")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mariam")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, description, m)')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].description, "m")
        with patch('sys.stdout', new=StringIO()) as f:
            atr = "number_rooms"
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {atr}, "2")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].number_rooms, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            atr = "number_bathrooms"
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {atr}, "2")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].number_bathrooms, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, max_guest, "2")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].max_guest, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            atr = "price_by_night"
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {atr}, "2")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].price_by_night, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            atr = "latitude"
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {atr}, "2.3")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].latitude, 2.3)
        with patch('sys.stdout', new=StringIO()) as f:
            atr = "longitude"
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {atr}, "2.3")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].longitude, 2.3)

    def test_do_update_Place3(self):
        """test update"""
        id = ""
        cls1_name = "Place"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            att_val = {"city_id": "mariam ibrahim", "user_id": "nimo mohamed",
                       "name": "lol", "description": "hi"}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(att_val)})')
            att_val = {"number_rooms": "9", "number_bathrooms": "2",
                       "max_guest": "3", "price_by_night": "10.6"}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(att_val)})')
            att_val = {"latitude": "9.5", "longitude": "2.4"}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(att_val)})')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].city_id, "mariam ibrahim")
            self.assertEqual(dictionary[key].user_id, "nimo mohamed")
            self.assertEqual(dictionary[key].name, "lol")
            self.assertEqual(dictionary[key].description, "hi")
            self.assertEqual(dictionary[key].number_rooms, 9)
            self.assertEqual(dictionary[key].number_bathrooms, 2)
            self.assertEqual(dictionary[key].max_guest, 3)
            self.assertEqual(dictionary[key].price_by_night, 10)
            self.assertEqual(dictionary[key].latitude, 9.5)
            self.assertEqual(dictionary[key].longitude, 2.4)

    def test_do_update_Review(self):
        """test update"""
        id = ""
        cls1_name = "Review"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} place_id "mari"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].place_id, "mari")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} user_id "989" e p')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].user_id, "989")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} text "hhhh" extr')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].text, "hhhh")

    def test_do_update_Review2(self):
        """test update"""
        id = ""
        cls1_name = "Review"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, place_id, m)')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].place_id, "m")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, user_id, "9")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].user_id, "9")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, text, "999")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].text, "999")

    def test_do_update_Review3(self):
        """test update"""
        id = ""
        cls1_name = "Review"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            atr_val = {"place_id": "mariam ibrahim", "user_id": "989",
                       "text": "hhhh"}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(atr_val)})')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].place_id, "mariam ibrahim")
            self.assertEqual(dictionary[key].user_id, "989")
            self.assertEqual(dictionary[key].text, "hhhh")

    def test_do_update_State(self):
        """test update"""
        id = ""
        cls1_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} name "mari" extra')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mari")

    def test_do_update_State2(self):
        """test update"""
        id = ""
        cls1_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, name, "mar")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mar")

    def test_do_update_State3(self):
        """test update"""
        id = ""
        cls1_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            att_val = {"name": "mariam ibrahim"}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(att_val)})')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mariam ibrahim")

    def test_do_update_arg1_miss(self):
        """test update"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class name missing **")

    def test_do_update_arg1_miss2(self):
        """test update"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f".update()")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class name missing **")

    def test_do_update_arg1_incorrect(self):
        """test update"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update hi")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class doesn't exist **")

    def test_do_update_arg1_incorrect2(self):
        """test update"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"hi.update()")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class doesn't exist **")

    def test_do_update_arg2_miss(self):
        """test update"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** instance id missing **")

    def test_do_update_arg2_miss2(self):
        """test update"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.update()")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** instance id missing **")

    def test_do_update_arg2_incorrect(self):
        """test update"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel 123")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** no instance found **")

    def test_do_update_arg2_incorrect2(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.update(123)")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** no instance found **")

    def test_do_update_arg3_miss(self):
        """test update"""
        id = ""
        cls1_name = "Review"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Review {id}")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** attribute name missing **")

    def test_do_update_arg3_miss2(self):
        """test update"""
        id = ""
        cls1_name = "Review"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.update({id})")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** attribute name missing **")

    def test_do_update_arg4_miss(self):
        """test update"""
        id = ""
        cls1_name = "Review"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Review {id} hi")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** value missing **")

    def test_do_update_arg4_miss2(self):
        """test update"""
        id = ""
        cls1_name = "Review"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.update({id}, hi)")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** value missing **")

    def test_invalid(self):
        """test invalid"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"crea")
            output = f.getvalue().strip()
            self.assertEqual(output,  "*** Unknown syntax: crea")
>>>>>>> 07a4d37cea5158a8bd015dd84f3532d91e1c264b

    @classmethod
    def tearDown(self):
<<<<<<< HEAD
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_create_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_invalid_syntax(self):
        correct = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())
        correct = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "User.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "State.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "City.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Place.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Review.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())


class TestHBNBCommand_show(unittest.TestCase):
    """Unittests for testing show from the HBNB command interpreter"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_show_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.show()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_missing_id_space_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show State"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show City"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Amenity"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Place"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Review"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_missing_id_dot_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.show()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_no_instance_found_space_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show State 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show City 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Amenity 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Place 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Review 1"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_no_instance_found_dot_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "show BaseModel {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(testID)]
            command = "show User {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(testID)]
            command = "show State {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(testID)]
            command = "show Place {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(testID)]
            command = "show City {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "show Amenity {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(testID)]
            command = "show Review {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

    def test_show_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "BaseModel.show({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(testID)]
            command = "User.show({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(testID)]
            command = "State.show({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(testID)]
            command = "Place.show({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(testID)]
            command = "City.show({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "Amenity.show({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(testID)]
            command = "Review.show({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())


class TestHBNBCommand_destroy(unittest.TestCase):
    """Unittests for testing destroy from the HBNB command interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        storage.reload()

    def test_destroy_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".destroy()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_id_missing_space_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy State"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy City"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Place"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Review"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_id_missing_dot_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_invalid_id_space_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy State 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy City 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Place 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Review 1"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_invalid_id_dot_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "destroy BaseModel {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(testID)]
            command = "show User {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(testID)]
            command = "show State {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(testID)]
            command = "show Place {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(testID)]
            command = "show City {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "show Amenity {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(testID)]
            command = "show Review {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

    def test_destroy_objects_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "BaseModel.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(testID)]
            command = "User.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(testID)]
            command = "State.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(testID)]
            command = "Place.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(testID)]
            command = "City.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "Amenity.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(testID)]
            command = "Review.destory({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())


class TestHBNBCommand_all(unittest.TestCase):
    """Unittests for testing all of the HBNB command interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_all_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.all()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_all_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    def test_all_objects_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    def test_all_single_object_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all City"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

    def test_all_single_object_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())


class TestHBNBCommand_update(unittest.TestCase):
    """Unittests for testing update from the HBNB command interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_update_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".update()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.update()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_id_space_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update State"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update City"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Amenity"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Place"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Review"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_id_dot_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.update()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.update()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.update()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.update()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.update()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.update()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.update()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_invalid_id_space_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update State 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update City 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Amenity 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Place 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Review 1"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_invalid_id_dot_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_name_space_notation(self):
        correct = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testId = output.getvalue().strip()
            testCmd = "update BaseModel {}".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testId = output.getvalue().strip()
            testCmd = "update User {}".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testId = output.getvalue().strip()
            testCmd = "update State {}".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testId = output.getvalue().strip()
            testCmd = "update City {}".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testId = output.getvalue().strip()
            testCmd = "update Amenity {}".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testId = output.getvalue().strip()
            testCmd = "update Place {}".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_name_dot_notation(self):
        correct = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testId = output.getvalue().strip()
            testCmd = "BaseModel.update({})".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testId = output.getvalue().strip()
            testCmd = "User.update({})".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testId = output.getvalue().strip()
            testCmd = "State.update({})".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testId = output.getvalue().strip()
            testCmd = "City.update({})".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testId = output.getvalue().strip()
            testCmd = "Amenity.update({})".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testId = output.getvalue().strip()
            testCmd = "Place.update({})".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_value_space_notation(self):
        correct = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            testId = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            testCmd = "update BaseModel {} attr_name".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            testId = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            testCmd = "update User {} attr_name".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            testId = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            testCmd = "update State {} attr_name".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            testId = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            testCmd = "update City {} attr_name".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            testId = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            testCmd = "update Amenity {} attr_name".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            testCmd = "update Place {} attr_name".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            testId = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            testCmd = "update Review {} attr_name".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_value_dot_notation(self):
        correct = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            testId = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            testCmd = "BaseModel.update({}, attr_name)".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            testId = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            testCmd = "User.update({}, attr_name)".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            testId = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            testCmd = "State.update({}, attr_name)".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            testId = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            testCmd = "City.update({}, attr_name)".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            testId = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            testCmd = "Amenity.update({}, attr_name)".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            testCmd = "Place.update({}, attr_name)".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            testId = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            testCmd = "Review.update({}, attr_name)".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_valid_string_attr_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            testId = output.getvalue().strip()
        testCmd = "update BaseModel {} attr_name 'attr_value'".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["BaseModel.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            testId = output.getvalue().strip()
        testCmd = "update User {} attr_name 'attr_value'".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["User.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            testId = output.getvalue().strip()
        testCmd = "update State {} attr_name 'attr_value'".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["State.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            testId = output.getvalue().strip()
        testCmd = "update City {} attr_name 'attr_value'".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["City.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "update Place {} attr_name 'attr_value'".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            testId = output.getvalue().strip()
        testCmd = "update Amenity {} attr_name 'attr_value'".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Amenity.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            testId = output.getvalue().strip()
        testCmd = "update Review {} attr_name 'attr_value'".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Review.{}".format(testId)].__dict__
        self.assertTrue("attr_value", test_dict["attr_name"])

    def test_update_valid_string_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            tId = output.getvalue().strip()
        testCmd = "BaseModel.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["BaseModel.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            tId = output.getvalue().strip()
        testCmd = "User.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["User.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            tId = output.getvalue().strip()
        testCmd = "State.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["State.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            tId = output.getvalue().strip()
        testCmd = "City.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["City.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            tId = output.getvalue().strip()
        testCmd = "Place.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            tId = output.getvalue().strip()
        testCmd = "Amenity.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Amenity.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            tId = output.getvalue().strip()
        testCmd = "Review.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Review.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_int_attr_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "update Place {} max_guest 98".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_int_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            tId = output.getvalue().strip()
        testCmd = "Place.update({}, max_guest, 98)".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(tId)].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_float_attr_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "update Place {} latitude 7.2".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(7.2, test_dict["latitude"])

    def test_update_valid_float_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            tId = output.getvalue().strip()
        testCmd = "Place.update({}, latitude, 7.2)".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(tId)].__dict__
        self.assertEqual(7.2, test_dict["latitude"])

    def test_update_valid_dictionary_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            testId = output.getvalue().strip()
        testCmd = "update BaseModel {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["BaseModel.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            testId = output.getvalue().strip()
        testCmd = "update User {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["User.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            testId = output.getvalue().strip()
        testCmd = "update State {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["State.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            testId = output.getvalue().strip()
        testCmd = "update City {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["City.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "update Place {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            testId = output.getvalue().strip()
        testCmd = "update Amenity {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Amenity.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            testId = output.getvalue().strip()
        testCmd = "update Review {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Review.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_dictionary_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            testId = output.getvalue().strip()
        testCmd = "BaseModel.update({}".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["BaseModel.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            testId = output.getvalue().strip()
        testCmd = "User.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["User.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            testId = output.getvalue().strip()
        testCmd = "State.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["State.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            testId = output.getvalue().strip()
        testCmd = "City.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["City.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "Place.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            testId = output.getvalue().strip()
        testCmd = "Amenity.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Amenity.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            testId = output.getvalue().strip()
        testCmd = "Review.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Review.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_dictionary_with_int_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "update Place {} ".format(testId)
        testCmd += "{'max_guest': 98})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_dictionary_with_int_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "Place.update({}, ".format(testId)
        testCmd += "{'max_guest': 98})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_dictionary_with_float_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "update Place {} ".format(testId)
        testCmd += "{'latitude': 9.8})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(9.8, test_dict["latitude"])

    def test_update_valid_dictionary_with_float_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "Place.update({}, ".format(testId)
        testCmd += "{'latitude': 9.8})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(9.8, test_dict["latitude"])


class TestHBNBCommand_count(unittest.TestCase):
    """Unittests for testing count method of HBNB comand interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_count_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.count()"))
            self.assertEqual("0", output.getvalue().strip())

    def test_count_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("1", output.getvalue().strip())


if __name__ == "__main__":
=======
        """deallocating resources"""
        models.storage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except Exception:
            pass


if __name__ == '__main__':
>>>>>>> 07a4d37cea5158a8bd015dd84f3532d91e1c264b
    unittest.main()

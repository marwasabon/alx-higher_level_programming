#!/usr/bin/python3
import unittest
from models.base import Base
from models.InvalidClass import InvalidClass
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
        """
        Test that all files.
        """
 
        def test_to_json_string(self):
                """
                Test the to_json_string method.
                """
            # Test with an empty list
                list_dictionaries = []
                json_string = Base.to_json_string(list_dictionaries)
                self.assertEqual(json_string, "[]")
        
            # Test with a non-empty list
                list_dictionaries = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
                json_string = Base.to_json_string(list_dictionaries)
                expected_json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
                self.assertEqual(json_string, expected_json_string)
                
        def test_save_to_file(self):
                """
                Test the save_to_file method.
                """
                # Test with an empty list
                list_objs = []
                Base.save_to_file(list_objs)
                with open("Base.json", "r") as file:
                    json_string = file.read()
                    self.assertEqual(json_string, "[]")
        
                # Test with a non-empty list
                list_objs = [Base(1), Base(2)]
                Base.save_to_file(list_objs)
                with open("Base.json", "r") as file:
                    json_string = file.read()
                    expected_json_string = '[{"id": 1}, {"id": 2}]'
                    self.assertEqual(json_string, expected_json_string)

        def test_from_json_string(self):
                """
                Test the from_json_string method.
                """
                # Test with an empty string
                json_string = ""
                list_dictionaries = Base.from_json_string(json_string)
                self.assertEqual(list_dictionaries, [])
        
                # Test with a non-empty string
                json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
                list_dictionaries = Base.from_json_string(json_string)
                expected_list_dictionaries = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
                self.assertEqual(list_dictionaries, expected_list_dictionaries)
        

        def test_create_rectangle(self):
                """
                Test the create method.
                """
                dictionary = {"width": 5, "height": 10}
                expected_instance = Rectangle(5, 10)
                actual_instance = Rectangle.create(**dictionary)
                self.assertEqual(actual_instance.__class__, expected_instance.__class__)
                self.assertEqual(actual_instance.width, expected_instance.width)
                self.assertEqual(actual_instance.height, expected_instance.height)
        
        def test_create_square(self):
                """
                Test the create method.
                """
                dictionary = {"size": 7}
                expected_instance = Square(7)
                actual_instance = Square.create(**dictionary)
                self.assertEqual(actual_instance.__class__, expected_instance.__class__)
                self.assertEqual(actual_instance.width, expected_instance.width)

        def test_create_invalid_class(self):
                """
                Test the create method.
                """                
                dictionary = {"width": 5, "height": 10}
                with self.assertRaises(ValueError):
                    actual_instance = InvalidClass.create(**dictionary)

        def test_load_from_file(self):
                """
                Test the load_from_file method.
                """
                # Test with an existing file
                list_objs = [Base(1), Base(2)]
                Base.save_to_file(list_objs)
                instances = Base.load_from_file()
                self.assertEqual(len(instances), 2)
                self.assertEqual(instances[0].id, 1)
                self.assertEqual(instances[1].id, 2)
        
                # Test with a non-existing file
                instances = Base.load_from_file()
                self.assertEqual(instances, [])
        
if __name__ == "__main__":
        unittest.main()

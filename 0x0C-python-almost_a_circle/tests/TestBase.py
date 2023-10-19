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
                
        def save_to_file(cls, list_objs):
                """
                Test the save_to_file method.
                """
                filename = cls.__name__ + ".json"
                if list_objs is None:
                        list_objs = []
                json_dict = [obj.to_dictionary() for obj in list_objs]
                json_str = cls.to_json_string(json_dict)
                with open(filename, 'w') as file:
                        file.write(json_str)

        def test_from_json_string(self):
                """
                Test the from_json_string method.
                """
                # Test with valid JSON string
                json_string = '[1, 2, 3]'
                expected_result = [1, 2, 3]
                actual_result = Base.from_json_string(json_string)
                self.assertEqual(actual_result, expected_result)
                
                # Test with invalid JSON string
                json_string = 'invalid json'
                expected_result = []
                actual_result = Base.from_json_string(json_string)
                self.assertEqual(actual_result, expected_result)
                
                # Test with empty JSON string
                json_string = ''
                expected_result = []
                actual_result = Base.from_json_string(json_string)
                self.assertEqual(actual_result, expected_result)
                
                # Test with None input
                json_string = None
                expected_result = []
                actual_result = Base.from_json_string(json_string)
                self.assertEqual(actual_result, expected_result)
        

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
                    actual_instance = Base.create(**dictionary)

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

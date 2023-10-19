#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
        """
        Test that all files.
        """
 
        def test_to_json_string(self):
                this
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
        
if __name__ == "main":
        unittest.main()

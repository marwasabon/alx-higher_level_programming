import unittest
import pep8
from models.base import Base


class TestBase(unittest.TestCase):
        """
        Test that all files.
        """
    def test_pep8_conformance(self):
        """
        Test that all files.
        """
        style = pep8.StyleGuide()
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0)

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

    def test_create(self):
        """
        Test the create method.
        """
        # Test with a Rectangle
        rectangle_dict = {'id': 1, 'width': 2, 'height': 3}
        rectangle = Base.create(**rectangle_dict)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 3)

        # Test with a Square
        square_dict = {'id': 2, 'size': 4}
        square = Base.create(**square_dict)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 4)

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

 



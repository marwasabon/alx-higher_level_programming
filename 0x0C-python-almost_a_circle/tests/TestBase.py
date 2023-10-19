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
        
        def test_base_auto_id(self):
                '''this 1'''
                b1 = Base()
                b2 = Base()
                self.assertEqual(b1.id, 1)
                self.assertEqual(b2.id, 2)

        def test_base_auto_id_plus_one(self):
                b1 = Base()
                b2 = Base()
                b3 = Base()
                self.assertEqual(b1.id, 1)
                self.assertEqual(b2.id, 2)
                self.assertEqual(b3.id, 3)

        def test_base_pass_id(self):
                b = Base(89)
                self.assertEqual(b.id, 89)

        def test_to_json_string_none(self):
                self.assertEqual(Base.to_json_string(None), "[]")

        def test_to_json_string_empty(self):
                self.assertEqual(Base.to_json_string([]), "[]")

        def test_to_json_string_with_data(self):
                data = [{'id': 12}]
                self.assertEqual(Base.to_json_string(data), '[{"id": 12}]')

        def test_from_json_string_none(self):
                self.assertEqual(Base.from_json_string(None), [])

        def test_from_json_string_empty(self):
                self.assertEqual(Base.from_json_string("[]"), [])

        def test_from_json_string_with_data(self):
                data = '[{"id": 89}]'
                self.assertEqual(Base.from_json_string(data), [{'id': 89}])
        
        def test_rectangle_create(self):
                r = Rectangle(1, 2)
                self.assertIsInstance(r, Rectangle)

        def test_rectangle_create_with_three_params(self):
                r = Rectangle(1, 2, 3)
                self.assertIsInstance(r, Rectangle)

        def test_rectangle_create_with_four_params(self):
                r = Rectangle(1, 2, 3, 4)
                self.assertIsInstance(r, Rectangle)

        def test_rectangle_create_with_string_as_width(self):
                with self.assertRaises(TypeError):
                        r = Rectangle("1", 2)

        def test_rectangle_create_with_string_as_height(self):
                with self.assertRaises(TypeError):
                        r = Rectangle(1, "2")

        def test_rectangle_create_with_string_as_x(self):
                with self.assertRaises(TypeError):
                        r = Rectangle(1, 2, "3")

        def test_rectangle_create_with_string_as_y(self):
                with self.assertRaises(TypeError):
                        r = Rectangle(1, 2, 3, "4")

        def test_rectangle_create_with_extra_param(self):
                with self.assertRaises(TypeError):
                        r = Rectangle(1, 2, 3, 4, 5)

        def test_rectangle_negative_width(self):
                with self.assertRaises(ValueError):
                        r = Rectangle(-1, 2)

        def test_rectangle_negative_height(self):
                with self.assertRaises(ValueError):
                        r = Rectangle(1, -2)

        def test_rectangle_zero_width(self):
                with self.assertRaises(ValueError):
                        r = Rectangle(0, 2)

        def test_rectangle_zero_height(self):
                with self.assertRaises(ValueError):
                        r = Rectangle(1, 0)
                        
        def test_rectangle_negative_x(self):
                with self.assertRaises(ValueError):
                        r = Rectangle(1, 2, -3)

        def test_rectangle_negative_y(self):
                with self.assertRaises(ValueError):
                        r = Rectangle(1, 2, 3, -4)
        
        def test_rectangle_area(self):
                r = Rectangle(3, 4)
                self.assertEqual(r.area(), 12)

        def test_rectangle_str(self):
                r = Rectangle(3, 4, 1, 2)
                self.assertEqual(str(r), "[Rectangle] (1) 1/2 - 3/4")

        def test_rectangle_display_no_xy(self):
                expected_output = "###\n###\n###\n###\n"
                r = Rectangle(3, 4)
                with patch('sys.stdout', new=StringIO()) as fake_out:
                        r.display()
                        self.assertEqual(fake_out.getvalue(), expected_output)

        def test_rectangle_display_no_y(self):
                expected_output = "\n\n  ##\n  ##\n  ##\n  ##\n"
                r = Rectangle(2, 4, 2)
                with patch('sys.stdout', new=StringIO()) as fake_out:
                        r.display()
                        self.assertEqual(fake_out.getvalue(), expected_output)

        def test_rectangle_display(self):
                expected_output = " ###\n ###\n ###\n"
                r = Rectangle(3, 3, 1, 0)
                with patch('sys.stdout', new=StringIO()) as fake_out:
                    r.display()
                    self.assertEqual(fake_out.getvalue(), expected_output)

        def test_rectangle_to_dictionary(self):
                r = Rectangle(1, 2, 3, 4, 5)
                expected_output = {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1}
                self.assertEqual(r.to_dictionary(), expected_output)

        def test_rectangle_update(self):
                r = Rectangle(1, 2)
                r.update(89)
                self.assertEqual(r.id, 89)

        def test_rectangle_update_with_width(self):
                r = Rectangle(1, 2)
                r.update(89, 1)
                self.assertEqual(r.width, 1)

        def test_rectangle_update_with_width_and_height(self):
                r = Rectangle(1, 2)
                r.update(89, 1, 2)
                self.assertEqual(r.height, 2)

        def test_rectangle_update_with_width_height_x(self):
                r = Rectangle(1, 2)
                r.update(89, 1, 2, 3)
                self.assertEqual(r.x, 3)

        def test_rectangle_update_with_width_height_x_y(self):
                r = Rectangle(1, 2)
                r.update(89, 1, 2, 3, 4)
                self.assertEqual(r.y, 4)

        def test_rectangle_update_with_dict(self):
                r = Rectangle(1, 2)
                r.update(**{'id': 89})
                self.assertEqual(r.id, 89)

        def test_rectangle_update_with_dict_width(self):
                r = Rectangle(1, 2)
                r.update(**{'id': 89, 'width': 1})
                self.assertEqual(r.width, 1)

        def test_rectangle_update_with_dict_width_height(self):
                r = Rectangle(1, 2)
                r.update(**{'id': 89, 'width': 1, 'height': 2})
                self.assertEqual(r.height, 2)

        def test_rectangle_update_with_dict_width_height_x(self):
                r = Rectangle(1, 2)
                r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
                self.assertEqual(r.x, 3)

        def test_rectangle_update_with_dict_width_height_x_y(self):
                r = Rectangle(1, 2)
                r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
                self.assertEqual(r.y, 4)

        def test_rectangle_create_from_dict(self):
                r = Rectangle.create(**{'id': 89})
                self.assertEqual(r.id, 89)

        def test_rectangle_create_from_dict_width(self):
                r = Rectangle.create(**{'id': 89, 'width': 1})
                self.assertEqual(r.width, 1)

        def test_rectangle_create_from_dict_width_height(self):
                r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
                self.assertEqual(r.height, 2)

        def test_rectangle_create_from_dict_width_height_x(self):
                r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
                self.assertEqual(r.x, 3)

        def test_rectangle_create_from_dict_width_height_x_y(self):
                r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
                self.assertEqual(r.y, 4)

        def test_rectangle_save_to_file_none(self):
                Rectangle.save_to_file(None)
                with open("Rectangle.json", "r") as file:
                        self.assertEqual(file.read(), "[]")

        def test_rectangle_save_to_file_empty(self):
                Rectangle.save_to_file([])
                with open("Rectangle.json", "r") as file:
                        self.assertEqual(file.read(), "[]")

        def test_rectangle_save_to_file_with_data(self):
                r = Rectangle(1, 2)
                Rectangle.save_to_file([r])
                with open("Rectangle.json", "r") as file:
                        self.assertEqual(file.read(), '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]')

        def test_rectangle_load_from_file_not_exist(self):
                self.assertEqual(Rectangle.load_from_file(), [])

        def test_rectangle_load_from_file_exists(self):
                r = Rectangle(1, 2)
                Rectangle.save_to_file([r])
                rectangles = Rectangle.load_from_file()
                self.assertIsInstance(rectangles[0], Rectangle)

        def test_square_create(self):
                s = Square(1)
                self.assertIsInstance(s, Square)

        def test_square_create_with_two_params(self):
                s = Square(1, 2)
                self.assertIsInstance(s, Square)

        def test_square_create_with_three_params(self):
                s = Square(1, 2, 3)
                self.assertIsInstance(s, Square)

        def test_square_create_with_string_as_size(self):
                with self.assertRaises(TypeError):
                        s = Square("1")

        def test_square_create_with_string_as_x(self):
                with self.assertRaises(TypeError):
                        s = Square(1, "2")

        def test_square_create_with_string_as_y(self):
                with self.assertRaises(TypeError):
                        s = Square(1, 2, "3")

        def test_square_create_with_extra_param(self):
                with self.assertRaises(TypeError):
                        s = Square(1, 2, 3, 4)

        def test_square_negative_size(self):
                with self.assertRaises(ValueError):
                        s = Square(-1)

        def test_square_negative_x(self):
                with self.assertRaises(ValueError):
                        s = Square(1, -2)

        def test_square_negative_y(self):
                with self.assertRaises(ValueError):
                        s = Square(1, 2, -3)

        def test_square_zero_size(self):
                with self.assertRaises(ValueError):
                        s = Square(0)

        def test_square_str(self):
                s = Square(3, 4, 5)
                self.assertEqual(str(s), "[Square] (1) 4/5 - 3")

        def test_square_to_dictionary(self):
                s = Square(1, 2, 3, 4)
                expected_output = {'x': 2, 'y': 3, 'id': 4, 'size': 1}
                self.assertEqual(s.to_dictionary(), expected_output)

        def test_square_update(self):
                s = Square(1)
                s.update(89)
                self.assertEqual(s.id, 89)

        def test_square_update_with_size(self):
                s = Square(1)
                s.update(89, 2)
                self.assertEqual(s.size, 2)

        def test_square_update_with_size_x(self):
                s = Square(1)
                s.update(89, 2, 3)
                self.assertEqual(s.x, 3)

        def test_square_update_with_size_x_y(self):
                s = Square(1)
                s.update(89, 2, 3, 4)
                self.assertEqual(s.y, 4)

        def test_square_update_with_dict(self):
                s = Square(1)
                s.update(**{'id': 89})
                self.assertEqual(s.id, 89)

        def test_square_update_with_dict_size(self):
                s = Square(1)
                s.update(**{'id': 89, 'size': 2})
                self.assertEqual(s.size, 2)

        def test_square_update_with_dict_size_x(self):
                s = Square(1)
                s.update(**{'id': 89, 'size': 2, 'x': 3})
                self.assertEqual(s.x, 3)

        def test_square_update_with_dict_size_x_y(self):
                s = Square(1)
                s.update(**{'id': 89, 'size': 2, 'x': 3, 'y': 4})
                self.assertEqual(s.y, 4)

        def test_square_create_from_dict(self):
                s = Square.create(**{'id': 89})
                self.assertEqual(s.id, 89)

        def test_square_create_from_dict_size(self):
                s = Square.create(**{'id': 89, 'size': 1})
                self.assertEqual(s.size, 1)

        def test_square_create_from_dict_size_x(self):
                s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
                self.assertEqual(s.x, 2)

        def test_square_create_from_dict_size_x_y(self):
                s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
                self.assertEqual(s.y, 3)

        def test_square_save_to_file_none(self):
                Square.save_to_file(None)
                with open("Square.json", "r") as file:
                    self.assertEqual(file.read(), "[]")

        def test_square_save_to_file_empty(self):
                Square.save_to_file([])
                with open("Square.json", "r") as file:
                    self.assertEqual(file.read(), "[]")

        def test_square_save_to_file_with_data(self):
                s = Square(1)
                Square.save_to_file([s])
                with open("Square.json", "r") as file:
                    self.assertEqual(file.read(), '[{"id": 1, "size": 1, "x": 0, "y": 0}]')

        def test_square_load_from_file_not_exist(self):
                self.assertEqual(Square.load_from_file(), [])

        def test_square_load_from_file_exists(self):
                s = Square(1)
                Square.save_to_file([s])
                squares = Square.load_from_file()
                self.assertIsInstance(squares[0], Square)
 
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

        def test_load_from_file(self):
                """
                Test the load_from_file method.
                """
                # Test with an existing file
                # Test with an existing file
                list_objs = [Rectangle(1, 2), Rectangle(3, 4)]
                Rectangle.save_to_file(list_objs)
                instances = Rectangle.load_from_file()
                self.assertEqual(len(instances), 2)
                self.assertIsInstance(instances[0], Rectangle)
                self.assertIsInstance(instances[1], Rectangle)
        
if __name__ == "__main__":
        unittest.main()

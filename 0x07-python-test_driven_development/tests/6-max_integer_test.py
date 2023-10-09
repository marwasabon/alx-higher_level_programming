#!/usr/bin/python3

"""
This is a Python script that defines add_integer(a, b)
"""
import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This is the test file for  say_my_name:
    Prints "My name is <first name> <last name>".
    """

    def test_max_integer(self):
        """
        This is the test file for  say_my_name:
        Prints "My name is <first name> <last name>".
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 1]), 1)

    def test_max_integer_exceptions(self):
        """
        This is the test file for  say_my_name:
        Prints "My name is <first name> <last name>".
        """
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])
            max_integer(12345)


if __name__ == '__main__':

    unittest.main()

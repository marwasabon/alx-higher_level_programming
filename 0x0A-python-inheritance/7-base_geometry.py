#!/usr/bin/python3
"""
This is a Python script that defines a class named mylist..

"""


class BaseGeometry:

    """
    A base class for geometrical shapes.
    """

    def area(self):

        """
        Calculates the area of the shape.
        This method is not implemented in the base class.
        Raises:
        Exception: "area() is not implemented"
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.
        Args:
        name (str): The name of the value, used in error messages.
        value (int): The value to validate.
        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

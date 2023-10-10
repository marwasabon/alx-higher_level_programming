#!/usr/bin/python3
"""
This is a Python script that defines a class named mylist..

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """
    A base class for geometrical shapes.
    """
    def __init__(self, width, height):
        """
        Initializes a new instance of the Rectangle class.
        Args:width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is not greater than 0.
        """
        self.integer_validator("width", width)

        self.integer_validator("height", height)

        self.__width = width

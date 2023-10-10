#!/usr/bin/python3
"""
This is a Python script that defines a class named mylist..

"""


class Square(Rectangle):

    """
    A base class for geometrical shapes.
    """
    def __init__(self, size):
        """
        Initializes a new instance of the Rectangle class.
        Args:width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is not greater than 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):

        """
        Calculates the area of the rectangle.
        Returns:
        int: The area of the rectangle.
        """
        return self.__size ** 2

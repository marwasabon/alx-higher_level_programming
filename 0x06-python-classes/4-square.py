#!/usr/bin/python3
"""
This is a Python script that defines a class named Square.

"""


class Square:
    """This class represents a square.
    Initializes a new instance of the Square class.
    Parameters:
    size (int): The size of the square. Defaults to 0.
    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.
    """
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
        This method calculates the area of a square.
        Attributes:size (int): The size of the square.
        @return: The area of the square.
        '''
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

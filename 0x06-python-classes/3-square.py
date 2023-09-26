#!/usr/bin/python3
'''
This is a Python script that defines a class named Square.

'''


class Square:
    """
        Represents a square shape.

    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.
        Parameters:
        size (int): The size of the square. Defaults to 0.
        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
        This method calculates the area of a square.
        @return: The area of the square.
        '''
        return self.__size ** 2

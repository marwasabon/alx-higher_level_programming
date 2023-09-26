#!/usr/bin/python3
'''
This is a Python script that defines a class named Square.

'''


class Square:
    """
    This is a class called Square.

    Attributes:
    - __size (int): The size of the square.

    Methods:
    - __init__(self, size=0): Initializes the Square object with a given size.
    - area(self): Calculates and returns the area of the square.
    - size(self): Getter method that returns the size of the square.
    - size(self, value): Setter method that sets the size of the square.
    - my_print(self): Prints a visual representation of the square using '#'.
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

    def my_print(self):
        '''
        - my_print(self):
        Prints a visual representation of the square using '#'.
        '''

        if self.__size == 0:

            print()

            return

        for i in range(self.__size):

            print("#" * self.__size)

#!/usr/bin/python3
'''
This is a Python script that defines a class named Square.

'''


class Square:
    """
    Represents a square shape.

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.
        Parameters:
        size (int): The size of the square. Defaults to 0.
        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

        """
        self.size = size

        self.position = position

    @property
    def size(self):
        """
         Get and set the current size of the square.
         """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get & set the current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be 2 positive integers")
        self.__position = value

    def area(self):
        '''
        This method calculates the area of a square.
        @return: The area of the square.
         '''
        return self.__size * self.__size

    def my_print(self):
        '''
        my_print(self):
        Prints a visual representation of the square using '#'.
        '''

        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    if self.__position[0]:
                        print("_", end="")
                    else:
                        print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()

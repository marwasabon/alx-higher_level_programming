#!/usr/bin/python3
"""
This is a Python script that defines a class named Square.

"""


class Rectangle:
    """
    This is a Python script that defines a class named Rectangle.
    """
    """
    This is Rectangle class. Idoesnt do anything

    Attributes:None

    Methods:None

    """
    '''what is qrong here pls'''

    widthType = "The width must be an integer."

    widthValue = "The width must >=0"

    heightType = "The height must be an integer."

    heightValue = "The height must be >=0"

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.
        Parameters:
        width (int): The width of the Rectangle. Defaults to 0.
        height (int): The height of the Rectangle defualts to 0.
        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if not isinstance(width, int):
            raise TypeError(self.widthType)
        if width < 0:
            raise ValueError(self.widthValue)
        if not isinstance(height, int):
            raise TypeError(self.heightType)
        if height < 0:
            raise ValueError(self.heightValue)
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Get and set the current size of the square.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Get and set the current size of the square.

        """
        if not isinstance(value, int):
            raise TypeError(self.widthType)

        if value < 0:

            raise ValueError(self.widthValue)
        self.__width = value

    @property
    def height(self):
        """
        Get and set the current size of the square.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Get and set the current size of the square.
        """
        if not isinstance(value, int):

            raise TypeError(self.heightType)
        if value < 0:

            raise ValueError(self.heightValue)
        self.__height = value

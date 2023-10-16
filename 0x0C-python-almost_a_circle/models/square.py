#!/usr/bin/python3
'''
This is a Python script that defines
a Square class that inherits from the Base class.
'''


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class represents a Square.
    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
        id (int): The id of the rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the top-left corner of the rectangle.
            y (int): The y-coordinate of the top-left corner of the rectangle.
            id (int): The id of the rectangle.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for size.
        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for size.
        Args:
            value (int): The size of the square.
        Raises:
            ValueError: If value is not a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("width must be an integer greater than 0")
        self.width = value
        self.height = value

    def __str__(self):
        '''
        returns [Square] (<id>) <x>/<y> - <width>/<height>
        '''
        return ("[Square] ({}) {}/{}"

                " - {}".format(self.id, self.x, self.y, self.width))

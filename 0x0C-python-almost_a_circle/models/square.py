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

    def __str__(self):
        '''
        returns [Square] (<id>) <x>/<y> - <width>/<height>
        '''
        return ("[Square] ({}) {}/{}"

                " - {}".format(self.id, self.x, self.y, self.width))

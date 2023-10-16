#!/usr/bin/python3
'''
This is a Python script that defines
a Rectangle class that inherits from the Base class.
'''


from models.base import Base


class Rectangle(Base):
    """
    This class represents a rectangle.
    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
        id (int): The id of the rectangle.
    """
    def __init__(self, width, height, x=0, y=0):
        """
        Initializes a Rectangle object.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the top-left corner of the rectangle.
            y (int): The y-coordinate of the top-left corner of the rectangle.
            id (int): The id of the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def update(self, *args, **kwargs):
        '''
        assigns a key/value argument to attributes
        '''
        if args:
            self.width = args[0]
            self.height = args[1]
        else:
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']

 
    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        '''
        returns the area value of the Rectangle instance.
        '''
        return self.width * self.height

    def __str__(self):
        '''
        returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        '''
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "

                f"{self.width}/{self.height}")

    def display(self):
        '''
        prints in stdout the Rectangle instance
        with the character # - you don’t need to handle x and y here.
        '''
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.i
        Args:
            value (int): The width of the rectangle.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.
        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        Args:
            value (int): The height of the rectangle.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        Gets the x-coordinate of the top-left corner of the rectangle.
        Returns:
            int: The x-coordinate of the top-left corner of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x-coordinate of the top-left corner of the rectangle.
        Args:
            value (int): The x-coordinate
            of the top-left corner of the rectangle.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        Gets the y-coordinate of the top-left corner of the rectangle.
        Returns:
            int: The y-coordinate of the top-left corner of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y-coordinate of the top-left corner of the rectangle.
        Args:
            value (int): The y-coordinate
            of the top-left corner of the rectangle.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

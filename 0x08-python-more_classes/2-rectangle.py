#!/usr/bin/python3
""" 2. Area and Perimeter """


class Rectangle:
    """ Creating a class called Rectangle that defines a rectangle. """
    def __init__(self, width=0, height=0):
        """ Using the __init__ method.
        Args:
            width: private instance method for width of Rectangle
            height: private instance method for height of Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Using a private instance method.
        Note:
            Returns the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Using a private instance method.
        Note:
            Adding value validation
        Args:
            value: private instance attribute for width
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Using a private instance method.
        Note:
            Returns the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Using a private instance method.
        Note:
            Adding value validation
        Args:
            value: private instance attribute for height
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Using public instance method.
        Note:
            Area = wh
        Returns: the current rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Using public instance method.
        Note:
            Area = 2w + 2h
        Returns: the current rectangle perimeter
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

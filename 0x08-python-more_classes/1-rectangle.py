#!/usr/bin/python3
""" 1. Real definition of a rectangle """


class Rectangle:
    """ Creating a class called Rectangle that defines a rectangle. """
    def __init__(self, width=0, height=0):
        """ Using the __init__ method.
        Args:
            width: private instance method for width of Rectangle
            height: private instance method for height of Rectangle
        """
        self.width = width
        self.height. = height

    @property
    def width(self):
        """ Using a private instance method.
        Note:
            Returns the width
        """
        return self.__width

    @size.setter
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

    @size.setter
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

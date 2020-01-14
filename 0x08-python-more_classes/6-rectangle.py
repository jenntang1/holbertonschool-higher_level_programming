#!/usr/bin/python3
""" 6. How many instances """


class Rectangle:
    """ Creating a class called Rectangle that defines a rectangle.
    Note:
        Includes a public class attribute called number_of_instances
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Using the __init__ method.
        Args:
            width: private instance method for width of Rectangle
            height: private instance method for height of Rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Using a private instance method.
        Returns:
            The width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Using a private instance method.
        Note:
            Adding value validation
            Account for if width is not an integer
            Account for if width is a negative integer
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
        Returns:
            The height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Using a private instance method.
        Note:
            Adding value validation
            Account for if height is not an integer
            Account for if height is a negative integer
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
        Returns:
            The current rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Using public instance method.
        Note:
            Area = 2w + 2h
        Returns:
            If width or height is 0, return 0
            If width or height is not 0, return rectangluar perimeter
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """ Using __str__ method for string representation of object.
        Note:
            Account for if width or height is 0
        Returns:
            If width or height is 0, return empty string
            If width or height is not 0, return rectangle made of #
        """
        printed_rect = ""
        if self.__width is 0 or self.__height is 0:
            return ""
        else:
            for size in range(self.__height):
                printed_rect += ("#") * (self.__width) + ('\n')
            return printed_rect[:-1]

    def __repr__(self):
        """ Using __repr__ method for string representation of object.
        Returns:
            Printable representation of the rectangle
        """
        return "Rectangle(%d, %d)" % (self.__width, self.__height)

    def __del__(self):
        """ Using __del__ method to destroy an instance..
        Note:
            Prints the message "Bye rectangle..."
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

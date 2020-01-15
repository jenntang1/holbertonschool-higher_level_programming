#!/usr/bin/python3
""" 9. A square is a rectangle """


class Rectangle:
    """ Creating a class called Rectangle that defines a rectangle.
    Note:
        Includes a public class attribute called number_of_instances
        Includes a public class attribute called print_symbol
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Using the __init__ method.
        Args:
            width: private instance method for width of Rectangle
            height: private instance method for height of Rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1
        type(self).print_symbol

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
        Args:
            value: private instance attribute for width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is a negative integer
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
        Args:
            value: private instance attribute for height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is a negative integer
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
        Returns:
            If width or height is 0, return empty string
            If width or height is not 0, return rectangle made of #
        """
        printed_rect = ""
        if self.__width is 0 or self.__height is 0:
            return ""
        else:
            for size in range(self.__height):
                printed_rect += (str(self.print_symbol)) \
                        * (self.__width) + ('\n')
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Using static method (independent of class & instances).
        Args:
            rect_1: instance of Rectangle
            rect_2: instance of Rectangle
        Returns:
            If both rectangles have the same area, return rect_1
            If not, returns the bigger rectangle based on area
        Raises:
            TypeError: if rect_1 is not an instance of Rectangle
            TypeError: if rect_2 is not an instance of Rectangle
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() is rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Using class method (uses class as its first arg).
        Args:
            cls: class Rectangle
            size: size of a square
        Returns:
            A new Rectangle instance where width = height = size
        """
        cls.width = cls.height = size
        return cls(cls.width, cls.height)

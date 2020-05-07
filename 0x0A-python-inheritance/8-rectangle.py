#!/usr/bin/python3
""" 8. Rectangle """


class BaseGeometry:
    """ Creating a class called BaseGeometry. """

    def area(self):
        """ Creating a public instance method.
        Raises:
            Exception: if there's no area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Creating a public instance method.
        Note:
            Validates a value
        Args:
            name: always a string
            value: an integer type
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if isinstance(name, str) is False:
            raise TypeError("{} must be an integer".format(name))
        if isinstance(value, int) is False:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Creating a subclass called Rectangle that inherits
    from class BaseGeometry.
    """

    def __init__(self, width, height):
        """ Using the __init__ method.
        Note:
            Args are validated by the integer_validator method
        Args:
            width: private attribute that's a positive integer
            height: private attribute that's a positive integer
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

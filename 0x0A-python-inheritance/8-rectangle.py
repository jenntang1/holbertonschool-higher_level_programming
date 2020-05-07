#!/usr/bin/python3
""" 8. Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

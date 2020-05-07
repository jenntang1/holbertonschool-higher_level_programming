#!/usr/bin/python3
""" 10. Square #1"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Creating a multi-level subclass called Square that inherits
    from subclass Rectangle.
    """

    def __init__(self, size):
        """ Using the __init__ method.
        Note:
            Size is validated by the integer_validator method
        Args:
            size: private attribute that's a positive integer
        """
        self.integer_validator("size", size)
        self.__size = size

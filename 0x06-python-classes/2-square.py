#!/usr/bin/python3
"""2. Size validation """


class Square:
    """Creating a class called Square that defines a square. """
    def __init__(self, size=0):
        """Using the __init__ method.
        Note:
            Account for if size is not an integer
            Account for if size is a negative integer
        Args:
            size: private instance attribute for my_square
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

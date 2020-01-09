#!/usr/bin/python3
"""1. Square with size """


class Square:
    """Creating a class called Square that defines a square. """
    def __init__(my_square, size='0'):
        """Using the __init__ method.
        Args:
            size: private instance attribute for my_square
        """
        my_square.__size = size

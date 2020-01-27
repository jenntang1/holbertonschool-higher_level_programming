#!/usr/bin/python3
"""
10. And now, the Square!
11. Square size
12. Square update
14. Square instance to dictionary representation

Importing Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Creating a subclass called Square.
    Args:
        Rectangle: parentclass
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Using __init__ method.
        Args:
            size: assigned to width and height
            x: inherited attribute
            y: inherited attribute
            id: inherited attribute
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Using __str__ method.
        Returns:
            String representation of the Square
        """
        class_name = Square.__name__
        return("[{}] ({}) {}/{} - {}".format(class_name,
                                             self.id,
                                             self.x,
                                             self.y,
                                             self.size))

    @property
    def size(self):
        """ Creating public getter.
        Returns:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Creatng public setter.
        Args:
            value: validation for width and height
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than or equal to 0
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

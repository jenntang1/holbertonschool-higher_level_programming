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
        return self.width

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
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Creating public instance method.
        Note:
            Assigns a key/value argument to the attributes
        Args:
            *args: id, width, height, x, y in this order
            **kwargs: id, width, height, x, y in no order
        """
        if (len(args) > 0) and (args is not None):
            for post, arg in enumerate(args):
                if post is 0:
                    self.id = arg
                if post is 1:
                    self.size = arg
                if post is 2:
                    self.x = arg
                if post is 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Creating a public method.
        Returns:
            dictionary representation of a Square
        """
        new_dict = {"id": self.id,
                    "size": self.size,
                    "x": self.x,
                    "y": self.y}
        return new_dict

#!/usr/bin/python3
"""
2. First Rectangle
3. Validate attributes
4. Area first
5. Display #0
6. __str__
7. Display #1
8. Update #0
9. Update #1

Importing base class
"""
from models.base import Base


class Rectangle(Base):
    """ Creating a subclass called Rectangle.
    Note:
        Inherits id and __nb__objects from Base
    Args:
        Base: superclass
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Using __init__ method.
        Note:
            Inherited id from superclass
        Args:
            width: private instance attribute
            height: private instance attribute
            x: private instance attribute
            y: private instance attribute
       """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Creating a private instance method.
        Returns:
            width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Creating a private instance method.
        Args:
            value: private instance attribute
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than or equal to 0
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Creating a private instance method.
        Returns:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Creating a private instance method.
        Args:
            value: private instance attribute
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than or equal to 0
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Creating a private instance method.
        Returns:
            x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ Creating a private instance method.
        Args:
            value: private instance attribute
        Raises:
            TypeError: if x is not an integer
            ValueError: if x is less than 0
        """
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Creating a private instance method.
        Returns:
            y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ Creating a private instance method.
        Args:
            value: private instance method
        Raises:
            TypeError: if y is not an integer
            ValueError: if y is less than 0
        """
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Creating a public instance method.
        Returns:
            Area value of the class, Rectangle
        """
        return self.width * self.height

    def display(self):
        """ Creating a public instance method.
        Note:
            Prints to stdout the Rectangle using #
        """
        for no_post in range(self.y):
            print()
        for row in range(self.height):
            for post in range(self.x):
                print(" ", end="")
            for col in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ Using __str__ method.
        Returns:
            String representation of the Rectangle
        """
        return("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height))

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
                    self.width = arg
                if post is 2:
                    self.height = arg
                if post is 3:
                    self.x = arg
                if post is 4:
                    self.y = arg
        else:
            self.id = kwargs.get("id", self.id)
            self.width = kwargs.get("width", self.width)
            self.height = kwargs.get("height", self.height)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

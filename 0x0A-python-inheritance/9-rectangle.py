#!/usr/bin/python3
""" 9. Full rectangle """


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

    def area(self):
        """ Implementing the area method.
        Returns:
            The area of the Rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """ Using the __str__ method.
        Returns:
            Description of the Rectangle
        """
        class_name = type(self).__name__
        return("[{}] {}/{}".format(class_name, self.__width, self.__height))

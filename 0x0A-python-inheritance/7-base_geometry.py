#!/usr/bin/python3
""" 7. Integer validator """


class BaseGeometry:
    """ Creating a class called BaseGeometry. """
    pass

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

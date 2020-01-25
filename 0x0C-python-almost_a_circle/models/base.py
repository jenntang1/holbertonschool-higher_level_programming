#!/usr/bin/python3
""" 1. Base class """


class Base:
    """ Creating a base class.
    Note:
        This will manage the id attribute in all other
        classes and avoid duplicating the same code.
    Attributes:
        __nb_objects: private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Using __init__ method.
        Note:
            If id is not None, assign id.
            If id is None, increment __nb_objects and
            assign new value to id.
        Args:
            id: public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

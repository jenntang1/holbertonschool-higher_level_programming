#!/usr/bin/python3
""" 3. Same class or inherit from """


def is_kind_of_class(obj, a_class):
    """ Creating a function that identifies an object's instance.
    Args:
        obj: the object
        a_class: the specified class
    Returns:
        True: if the object is an instance of the class
        False: if the object is not an instance of the class
    """
    return issubclass(type(obj), a_class)

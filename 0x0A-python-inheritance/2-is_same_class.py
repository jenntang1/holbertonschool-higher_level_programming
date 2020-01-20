#!/usr/bin/python3
""" 2. Exact same object """


def is_same_class(obj, a_class):
    """ Creating a function that identifies an object's instance.
    Note:
        Whether an object is an exact instance of a specified class
    Args:
        obj: the object
        a_class: the specified class
    Returns:
        True: if the object is exactly an instance of the class
        False: if the object is not an instance of the class
    """
    return issubclass(a_class, type(obj))

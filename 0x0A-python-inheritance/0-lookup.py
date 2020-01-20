#!/usr/bin/python3
""" 0. Lookup """


def lookup(obj):
    """ Function that returns the list of available
    attributes and methods of an object.
    Args:
        obj: the object
    Returns:
        A list of attributes and methods
    """
    return dir(obj)

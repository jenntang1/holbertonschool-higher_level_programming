#!/usr/bin/python3
""" 4. Only sub class of """


def inherits_from(obj, a_class):
    """ Creating a function that identifies an object's instance.
    Note:
        Whether an object is an instance of a class that inherited
        (directly or indirectly) from a specified class
    Args:
        obj: the object
        a_class: the specified class
    Returns:
        True: if the object is an instance of the class
        False: if the object is not an instance of the class
    """
    if isinstance(obj, a_class) is True:
        if type(obj) is not a_class:
            return True
    else:
        return False

#!/usr/bin/python3
""" 10. Class to JSON """


def class_to_json(obj):
    """ Creating function that returns the dictionary description
    with simple data structure for JSON serialization of an object.
    Note:
        All attributes of obj are serializable such as being
        a list, dict, str, int or bool
    Args:
        obj: instance of a class
    Returns:
        Dictionary description
    """
    return obj.__dict__

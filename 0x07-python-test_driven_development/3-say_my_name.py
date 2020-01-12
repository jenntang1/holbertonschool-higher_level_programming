#!/usr/bin/python3
""" 2. Say my name """


def say_my_name(first_name, last_name=""):
    """ Function that prints My name is <first name> <last name>.
    Args:
        first_name: string
        last_name: string
    Returns:
        nothing
    Raises:
        TypeError: if not a string
    Doctest Examples:
        see dir: /tests/3-say_my_name.txt
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))

#!/usr/bin/python3
""" 1. My list """


class MyList(list):
    """ Creating a subclass that inherits from list.
    Args:
        list: superclass
    """
    def print_sorted(self):
        """ Creating a public instance method. """
        print(sorted(self))

#!/usr/bin/python3
""" 1. My list """


class MyList(list):
    """ Creating a subclass that inherits from list.
    Args:
        list: superclass
    """
    def print_sorted(self):
        """ Creating a public instance method.
        Note:
            Prints a sorted list
        """
        new_list = self.copy()
        new_list.sort()
        print(new_list)

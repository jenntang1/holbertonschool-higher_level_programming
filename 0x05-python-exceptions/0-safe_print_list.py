#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for elements in range(x):
        try:
            print("{:d}".format(my_list[elements]), end="")
        except IndexError:
            print()
            return elements
    print()
    return x

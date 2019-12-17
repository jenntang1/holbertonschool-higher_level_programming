#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reverse = my_list[::-1]
    if my_list:
        for element in reverse:
            print("{:d}".format(element))

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    for current in my_list:
        if idx < 0:
            return my_list
        elif idx > len(my_list):
            return my_list
        elif current == idx:
            newer_list = my_list[:]
            newer_list[current] = element
            return newer_list

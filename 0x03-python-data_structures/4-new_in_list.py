#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    elif my_list:
        newer_list = my_list[:]
        newer_list[idx] = element
        return newer_list

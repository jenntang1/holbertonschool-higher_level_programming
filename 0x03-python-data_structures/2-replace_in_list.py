#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if my_list:
        for current in my_list:
            if idx < 0:
                return my_list
            elif idx > len(my_list):
                return my_list
            elif current == idx:
                my_list[current] = element
                return my_list
    else:
        return my_list

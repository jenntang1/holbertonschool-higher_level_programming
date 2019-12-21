#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, value2 in list(a_dictionary.items()):
        if value is value2:
            a_dictionary.pop(key)
    return a_dictionary

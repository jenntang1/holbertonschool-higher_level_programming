#!/usr/bin/python3
""" 7. Save Object to a file """


def save_to_json_file(my_obj, filename):
    """ Creating a function that writes an object to
    a text file, using JSON representation.
    Note:
        The with statement opens, reads and closes a file
    Args:
        my_obj: object to be written
        filename: name of text file
    """
    import json
    with open(filename, 'w') as file_obj:
        encoded = json.dumps(my_obj)
        file_obj.write(encoded)

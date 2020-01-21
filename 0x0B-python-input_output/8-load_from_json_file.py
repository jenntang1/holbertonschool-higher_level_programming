#!/usr/bin/python3
""" 8. Create object from a JSON file """


def load_from_json_file(filename):
    """ Creating a function that creates an object from a
    JSON file.
    Note:
        The with statement opens, reads and closes a file
    Args:
        filename: name of JSON file
    """
    import json
    with open(filename, 'r') as file_obj:
        decoded = json.load(file_obj)
        return(decoded)

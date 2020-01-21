#!/usr/bin/python3
""" 6. From JSON string to Object """


def from_json_string(my_str):
    """ Creating a function that returns an object
    represented by a JSON string.
    Args:
        my_str: string to decode from JSON
    Returns:
        Decoded object
    """
    import json
    decoded = json.loads(my_str)
    return(decoded)

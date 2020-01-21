#!/usr/bin/python3
""" 5. To JSON string """


def to_json_string(my_obj):
    """ Creating a function that returns the JSON
    representation of an object.
    Note:
        The with keyword first opens the file.
        Next, reads from it and finally, closes it.
    Args:
        my_obj: string to encode to JSON
    Returns:
        JSON representation
    """
    import json
    encoded = json.dumps(my_obj)
    return(encoded)

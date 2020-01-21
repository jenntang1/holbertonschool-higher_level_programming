#!/usr/bin/python3
""" 4. Append to a file """


def append_write(filename="", text=""):
    """ Creating a function that appends a string to the end
    of a text file and returns the number of characters added.
    Note:
        The with keyword first opens the file.
        Next, reads from it and finally, closes it.
    Args:
        filename: name of text file
        text: string to be appended
    Returns:
        Number of characters appended
    """
    with open(filename, 'a') as file_obj:
        return(file_obj.write(text))

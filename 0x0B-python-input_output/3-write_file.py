#!/usr/bin/python3
""" 3. Write to a file """


def write_file(filename="", text=""):
    """ Creating a function that writes a string to a text file
    and returns the number of characters written.
    Note:
        The with keyword opens, reads and closes a file
    Args:
        filename: name of text file
        text: string to be written
    Returns:
        Number of characters written
    """
    with open(filename, 'w') as file_obj:
        return(file_obj.write(text))

#!/usr/bin/python3
""" 1. Number of lines """


def number_of_lines(filename=""):
    """ Creating a function that returns the number of lines
    of a text file.
    Note:
        The with statement opens, reads and closes a file
    Args:
        filename: name of text file
    Returns:
        Number of lines of text file
    """
    text_count = 0
    with open(filename) as file_obj:
        for text_line in file_obj:
            text_count += 1
        return(text_count)

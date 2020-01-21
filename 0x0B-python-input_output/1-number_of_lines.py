#!/usr/bin/python3
def number_of_lines(filename=""):
    """ Creating a function that returns the number of lines
    of a text file.
    Note:
        First, open file and then, read from it
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

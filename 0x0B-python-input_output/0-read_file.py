#!/usr/bin/python3
""" 0. Read file """


def read_file(filename=""):
    """ Creating a function that reads a text file and
    prints to stdout.
    Note:
        The with keyword opens, reads and closes a file
    Args:
        filename: name of text file
    """
    text_content = ""
    with open(filename) as file_obj:
        for text_line in file_obj.readlines():
            text_content += text_line
        print("{}".format(text_content))

#!/usr/bin/python3
""" 2. Read n lines """


def read_lines(filename="", nb_lines=0):
    """ Creating a function that reads n lines of
    a text file and prints to stdout.
    Note:
        The with statement opens, reads and closes a file
    Args:
        filename: name of text file
        nb_lines: number of lines to read
    """
    text_count = 0
    text_content = ""
    with open(filename, 'r') as file_obj:
        for text_line in file_obj:
            text_count += 1
        if nb_lines <= 0 or nb_lines >= text_count:
            text_content = file_obj.read()
            print("{}".format(text_content))

#!/usr/bin/python3
""" 2. Read n lines """


def read_lines(filename="", nb_lines=0):
    """ Creating a function that reads n lines of
    a text file and prints to stdout.
    Note:
        The with statement opens, reads and closes a file.
        Reads entire file:
            if nb_lines is lower or equal to 0
            if nb_lines is greater or equal to total lines
    Args:
        filename: name of text file
        nb_lines: number of lines to read
    """
    text_content = ""
    with open(filename, 'r') as file_obj:
        if nb_lines <= 0:
            text_content = file_obj.read()
            print("{}".format(text_content), end="")
        else:
            for text_line in range(nb_lines):
                text_content = file_obj.readline()
                print("{}".format(text_content), end="")

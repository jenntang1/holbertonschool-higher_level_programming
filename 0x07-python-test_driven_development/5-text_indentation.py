#!/usr/bin/python3
""" 4. Text indentation """


def text_indentation(text):
    """ Function that prints a text with 2 new lines after
        each special characters: ., ? and :.
    Args:
        text: string to be printed
    Returns:
        nothing
    Raises:
        TypeError: if text is not a string
    Doctest Examples:
        see dir: /tests/5-text_indentation.txt
    """
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    special = ".?:"
    for letter in text:
        match = False
        for symbol in special:
            if symbol in letter:
                match = True
                print("{:s}".format(symbol))
                print()
                break
        if not match:
            print("{:s}".format(letter), end="")

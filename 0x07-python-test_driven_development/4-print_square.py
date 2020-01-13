#!/usr/bin/python3
""" 3. Print square """


def print_square(size):
    """ Function that prints a square with #.
    Args:
        size: length of the square given as an integer
    Returns:
        nothing
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is not 0 or an positive integer
    Doctest Examples:
        see dir: /tests/4-print_square.txt
    """
    if isinstance(size, float) is True:
        raise TypeError("size must be an integer")
    if (isinstance(size, float) is True) and (size < 0):
        raise TypeError("size must be an integer")
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()

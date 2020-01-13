#!/usr/bin/python3
""" 1. Divide a matrix """


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix.
    Args:
        matrix: 2d array of the same size
        div: divisor
    Returns:
        new matrix with elements rounded to 2 decimal places
    Raises:
        ZeroDivisionError: if div is zero
        TypeError: if div is not an int or float
        TypeError: if lists in matrix are not the same size
        TypeError: if elements in matrix is not an int or float
    Doctest Examples:
        see dir: /tests/2-matrix_divided.txt
    """
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for lists in matrix:
        if isinstance(lists, list) is False:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(lists) is 0:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(lists) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have "
                            "the same size")
        for elmts in lists:
            if isinstance(elmts, (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    return [[round(elmts/div, 2) for elmts in lists] for lists in matrix]

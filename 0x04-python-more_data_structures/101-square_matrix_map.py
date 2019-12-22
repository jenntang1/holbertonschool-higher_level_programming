#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda matrix: list(map(lambda e: e**2, matrix)), matrix))

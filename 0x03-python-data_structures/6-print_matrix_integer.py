#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in range(len(matrix)):
        for index in matrix[element]:
            if element != len(matrix):
                print("{:d} ".format(index))

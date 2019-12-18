#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in range(len(matrix)):
        for index in range(len(matrix[element])):
            print("{:d}".format(matrix[element][index]), end="")
            if (index != (len(matrix[element]) - 1)):
                print(end=" ")
        print("")

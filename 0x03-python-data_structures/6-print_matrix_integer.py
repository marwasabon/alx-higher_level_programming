#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    str = " "
    for row in range(len(matrix)):
        for co in range(len(matrix[row])):
            print("{:d}".format(matrix[row][co]), end="")
            if co != len(matrix[row]) - 1:
                print(" ", end="")
        print()

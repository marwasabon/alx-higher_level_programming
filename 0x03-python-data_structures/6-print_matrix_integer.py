#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    str = " "
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))

#!/usr/bin/python3
def square(x):
    return x * x

def square_matrix_simple(matrix=[]):
    new_list = [row[:] for row in matrix]

    for i in range(len(new_list)):
        new_list[i] = list(map(square, new_list[i]))

    return new_list

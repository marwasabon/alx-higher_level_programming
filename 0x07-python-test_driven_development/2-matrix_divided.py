#!/usr/bin/python3
"""
This is a Python script that defines add_integer(a, b)
"""

def matrix_divided(matrix, div):
    """
    matrix_divided:
    Returns divides all elements of a matrix.
    """
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix) or \
            not all(isinstance(el, (int, float)) for row in matrix 
                    for el in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(el / div, 2) for el in row] for row in matrix]

#!/usr/bin/python3
"""
This is a Python script that defines add_integer(a, b)
"""

def print_square(size):
    """
    matrix_divided:
    Returns divides all elements of a matrix.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)

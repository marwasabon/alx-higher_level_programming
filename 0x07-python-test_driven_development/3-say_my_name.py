#!/usr/bin/python3
"""
This is a Python script that defines add_integer(a, b)
"""

def say_my_name(first_name, last_name=""):
    """
    matrix_divided:
    Returns divides all elements of a matrix.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")

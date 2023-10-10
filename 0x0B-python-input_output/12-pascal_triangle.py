#!/usr/bin/python3
"""
This is a Python script..

"""


def pascal_triangle(n):
    '''
    Create a function def pascal_triangle(n): that returns
    a list of lists of integers representing the Pascal’s triangle of n:
    '''

    if n <= 0:
        return []

    triangle = [[1]]

    if n == 1:
        return triangle

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

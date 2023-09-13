#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix[i][j] ** 2)
            result.append(row)

        return result

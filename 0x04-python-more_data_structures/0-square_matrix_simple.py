#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    n_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for k in range(rows):
        for m in range(cols):
            n_matrix[k][m] = matrix[i][j] ** 2

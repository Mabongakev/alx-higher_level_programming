#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    f_matrix = [row[:] for row in matrix]
    for idx, row in enumerate(new_matrix):
        for idx2, col in enumerate(new_matrix):
            f_matrix[idx][idx2] = row[idx2] ** 2
    return f_matrix

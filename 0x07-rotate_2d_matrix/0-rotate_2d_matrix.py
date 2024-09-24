#!/usr/bin/python3
"""
contains the rotate_2d_matrix function
"""


def rotate_2d_matrix(matrix):
    """
    rotates a 2d matrix 90 degrees clockwise in-place
    """
    if not matrix:
        return

    if type(matrix) is not list:
        return

    matrix_len = len(matrix)
    if matrix_len < 2:
        return

    start = True
    n = 0
    for row in matrix:
        if type(row) is not list:
            return
        if start:
            n = len(row)
            if n == 0:
                return
            if n != matrix_len:
                return
            start = False
        else:
            if n != len(row):
                return

    matrix_copy = [row[:] for row in matrix]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = matrix_copy[n - 1 - j][i]

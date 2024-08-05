#!/usr/bin/python3
"""module for pascal's triangle function"""


def pascal_triangle(n):
    """a function that returns a list of lists of integers
       representing the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    my_triangle = []
    for row in range(n):
        if row == 0:
            my_triangle.append([1])
            continue
        elif row == 1:
            my_triangle.append([1, 1])
            continue
        tri = [1]
        for i in range(1, row):
            tri.append(my_triangle[row - 1][i - 1] + my_triangle[row - 1][i])
        tri.append(1)
        my_triangle.append(tri)

    return my_triangle

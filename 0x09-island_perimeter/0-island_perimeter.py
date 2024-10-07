#!/usr/bin/python3
"""
contains the island_perimeter function
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid.
    Grid is a list of list of integers:
        - 0 represents water
        - 1 represents land
        - Each cell is square, with a side length of 1
        - Cells are connected horizontally/vertically (not diagonally).
        - grid is rectangular, with its width and height not exceeding 100
    """
    if not grid:
        return None

    if not isinstance(grid, list):
        return None

    grid_len = len(grid)
    row_len = None
    if grid_len > 0:
        row_len = len(grid[0])

    for row in grid:
        if not isinstance(row, list):
            return None
        if len(row) != row_len:
            return None

    perimeter = 0
    i = 0
    while i < grid_len:
        j = 0
        while j < row_len:
            if grid[i][j] == 1:
                if i and grid[i - 1][j] == 0:
                    perimeter += 1
                if i + 1 < grid_len and grid[i + 1][j] == 0:
                    perimeter += 1
                if j and grid[i][j - 1] == 0:
                    perimeter += 1
                if j + 1 < row_len and grid[i][j + 1] == 0:
                    perimeter += 1
            j += 1
        i += 1

    return perimeter

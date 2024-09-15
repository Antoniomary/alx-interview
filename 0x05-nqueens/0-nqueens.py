#!/usr/bin/python3
"""
a program that places N non-attacking queens
on an N×N chessboard
"""
from sys import argv, exit


def find_n_queens_solution(board, col, n):
    """finds a possible solution for N x N chessboard
    """
    if col >= n:
        print_board(board, n)
        return

    for row in range(n):
        if check_safety(board, row, col, n):
            board[row][col] = 1
            find_n_queens_solution(board, col + 1, n)
            board[row][col] = 0

    return


def check_safety(board, row, col, n):
    """checks if a queen can be placed safely on board
    """
    for i in range(col):
        if board[row][i]:
            return False

    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row + 1, n), range(col - 1, -1, -1)):
        if board[i][j]:
            return False

    return True


def print_board(board, n):
    """prints chessboard
    """
    result = []

    for i in range(n):
        for j in range(n):
            if board[i][j]:
                result.append([i, j])

    print(result)


def main():
    """entry point
    """
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    n = argv[1]

    try:
        n = int(n)
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    find_n_queens_solution(board, 0, n)


main()

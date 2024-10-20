#!/usr/bin/python3
"""contains isWinner function"""


dp = [-1] * (10000 + 1)


def sieve_of_eratosthenes(n):
    """
    finds all prime numbers below and inclusive of n
    """
    if n < 2:
        return []

    arr = [1] * (n + 1)
    arr[0], arr[1] = 0, 0

    primes = []
    for i in range(2, n + 1):
        if arr[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                arr[j] = 0

    return primes


def isWinner(x, nums):
    """
    determines the winner of prime game
    where x is the number of rounds and nums is an array of n
    """
    if x < 1 or not nums or x != len(nums):
        return None

    score_board = [0, 0]  # index 0 for Maria, 1 for Ben
    for n in nums:
        game_play = 0  # starts at zero
        if dp[n] == -1:
            dp[n] = len(sieve_of_eratosthenes(n))
        game_play = dp[n]  # result is out

        if game_play % 2 == 0:
            score_board[1] += 1
        else:
            score_board[0] += 1

    if score_board[0] > score_board[1]:
        return "Maria"
    elif score_board[1] > score_board[0]:
        return "Ben"

    return None

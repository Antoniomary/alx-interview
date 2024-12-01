#!/usr/bin/python3
"""
contains the makeChange function
"""


def makeChange(coins, total):
    """finds the fewest number of coins needed to meet a given amount
       Return: fewest number of coins needed to meet total.
               If total is 0 or less, returns 0.
               If total cannot be met by any number of coins, return -1
    """
    if total <= 0:
        return 0

    # Removes duplicate coins and sorts coins in descending order
    coins = sorted(set(coins), reverse=True)

    change = 0
    for coin in coins:
        if total <= 0:
            break
        change += total // coin
        total %= coin

    if total != 0:
        return -1

    return change

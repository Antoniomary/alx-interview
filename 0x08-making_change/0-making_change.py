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

    if not coins:
        return 0

    # Removes duplicate coins and sorts coins in descending order
    coins = sorted(set(coins), reverse=True)

    # Initialize array to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)

    # No coins needed to make total of 0
    dp[0] = 0

    # Build the dp array
    for coin in coins:
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

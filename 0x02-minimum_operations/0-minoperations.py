#!/usr/bin/python3
"""contains the minOperations function"""
import math


def minOperations(n):
    """returns an int that corresponds to the fewest number of operations
       needed to result in exactly n H characters.
    """
    if n <= 1:
        return 0

    num_of_operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            num_of_operations += factor
            n //= factor
        factor += 1

    return num_of_operations

#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n_s = [4, 12, 21, 0, 1, 2147483640, 972, 19170307]

for n in n_s:
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

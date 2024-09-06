#!/usr/bin/python3
"""contains validUTF8 function"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding.
       Returns True if data is a valid UTF-8 encoding, else False
    """
    masks = [0b10000000,
             0b11100000,
             0b11110000,
             0b11111000]
    n_bytes = 0
    for n in data:
        if n_bytes == 0:
            if n & masks[0] == 0b00000000:
                continue
            elif n & masks[2] == 0b11100000:
                n_bytes = 2
            elif n & masks[3] == 0b11110000:
                n_bytes = 3
        else:
            if not (n & masks[1] == 0b10000000):
                return False
            n_bytes -= 1

    return True

#!/usr/bin/python3
"""contains validUTF8 function"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding.
       Returns True if data is a valid UTF-8 encoding, else False
    """
    for each in data:
        if each > 128:
            return False

    return True

#!/usr/bin/python3
"""contains validUTF8 function"""


def get_byte(n):
    """gets the last 8 bits in a number
    """
    if n >> 8 >= 1:
        return n & 0xffff

    return n


def check_for_bin_10(byte):
    """checks if byte starts with 10.
       Returns True if it does, else False
    """
    return byte >> 6 == 2


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding.
       Returns True if data is a valid UTF-8 encoding, else False
    """
    n = 0xFFFF

    for each in data:
        if each <= 0xffff:
            if not ((each >> 7) == 0):
                return False
        elif each <= 0xffffffff:
            for i in range(2):
                each = get_byte(each)
                if i == 0:
                    if not check_for_bin_10(each):
                        return False
                else:
                    if not ((each >> 5) == 0b110):
                        return False
        elif each <= 0xffffffffffff:
            for i in range(3):
                each = get_byte(each)
                if i != 2:
                    if not check_for_bin_10(each):
                        return False
                else:
                    if not ((each >> 5) == 0b1110):
                        return False
        elif each <= 0xffffffffffffffff:
            for i in range(4):
                each = get_byte(each)
                if i != 3:
                    if not check_for_bin_10(each):
                        return False
                else:
                    if not ((each >> 5) == 0b11110):
                        return False
        else:
            return False

    return True

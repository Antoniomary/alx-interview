#!/usr/bin/python3
"""contains validUTF8 function"""


def get_bytes(n):
    """returns a list of the bits in a number from
       least significant to most significant
    """
    all_bytes = []

    if n > 0xffffffff:
        return []

    for i in range(4):
        all_bytes.append(n & 0xff)
        if n >> 8 == 0:
            break
        n >>= 8

    return all_bytes


def check_for_bin_10(byte):
    """checks if byte starts with 10.
       Returns True if it does, else False
    """
    return byte >> 6 == 2


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding.
       Returns True if data is a valid UTF-8 encoding, else False
    """
    if not data:
        return False

    for each in data:
        all_bytes = get_bytes(each)
        len_all_bytes = len(all_bytes)
        if len_all_bytes == 1:
            if not ((all_bytes[0] >> 7) == 0):
                return False
        elif len_all_bytes == 2:
            if not ((check_for_bin_10(all_bytes[0]) and
                    (all_bytes[1] >> 5) == 0b110)):
                return False
        elif len_all_bytes == 3:
            if not (check_for_bin_10(all_bytes[0]) and
                    check_for_bin_10(all_bytes[1]) and
                    (all_bytes[2] >> 4) == 0b1110):
                return False
        elif len_all_bytes == 4:
            if not (check_for_bin_10(all_bytes[0]) and
                    check_for_bin_10(all_bytes[1]) and
                    check_for_bin_10(all_bytes[2]) and
                    (all_bytes[3] >> 3) == 0b11110):
                return False
        else:
            return False

    return True

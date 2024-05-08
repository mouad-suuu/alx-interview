#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    Args:
        data (list): A list of integers representing bytes.
    Returns:
        bool: True if the data represents a valid UTF-8 encoding, else False.
    """
    skip = 0
    n = len(data)
    for i in range(n):
        if skip > 0:
            skip -= 1
            continue
        if data[i] < 0 or data[i] > 255:
            return False
        if data[i] & 0b11110000 == 0b11110000:
            span = 4
        elif data[i] & 0b11100000 == 0b11100000:
            span = 3
        elif data[i] & 0b11000000 == 0b11000000:
            span = 2
        elif data[i] & 0b10000000 == 0b00000000:
            continue
        else:
            return False
        if i + span > n:
            return False
        for j in range(1, span):
            if data[i + j] & 0b11000000 != 0b10000000:
                return False
        skip = span - 1
    return True

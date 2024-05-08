#!/usr/bin/env python3
"""Least Frequently Used caching module.
"""


def validUTF8(data):
    """
    Validate if a list of integers represents a valid UTF-8 encoding.
    Args:
    data (list): A list of integers where each
    integer represents one byte of data.
    Returns:
    bool: True if the list represents valid UTF-8 encoding, False otherwise.
    """
    n_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        mask = 1 << 7
        if n_bytes == 0:
            while mask & num:
                n_bytes += 1
                mask = mask >> 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1
    return n_bytes == 0

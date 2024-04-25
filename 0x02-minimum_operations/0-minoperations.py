#!/usr/bin/python3
"""
minOperations function
"""


def minOperations(n):
    if n <= 1:
        return 0
    operations = 0
    factor = 2
    current_n = n
    while current_n > 1:
        while current_n % factor == 0:
            operations += factor
            current_n //= factor
        factor += 1
    # If after all possible factors, current_n is still greater than 1,
    # it means n is prime and we need n operations (1 copy and n-1 pastes)
    if current_n > 1:
        return n
    return operations

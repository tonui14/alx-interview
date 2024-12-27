#!/usr/bin/python3
"""
Module to calculate the min no of operations to achieve exactly n H characters
using only 'Copy All' and 'Paste' operations.
"""


def minOperations(n):
    """
    Calculates fewest no of operations needed to have exactly n H characters.
    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The min no of operations to reach exactly n 'H' characters,
        or 0 if it is impossible to achieve.
    """
    if n <= 1:
        return 0
    operations = 0
    factor = 2
    # Find all factors of n and add to the operation count
    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
            factor += 1
            # If n is still greater than 1, it's a prime factor
            if n > 1:
                operations += n
                return operations

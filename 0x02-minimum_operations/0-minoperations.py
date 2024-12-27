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
    # Start with 1 'H'
    current = 1

    # Iterate over possible divisors of n
    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            n //= i

    return operations

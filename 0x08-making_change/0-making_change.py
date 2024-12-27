#!/usr/bin/python3
"""
Module to det the fewest no of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determines the minimum number of coins to make up the given total.
    Args:
        coins (list): A list of coin denominations.
        total (int): The total amount to be achieved.
    Returns:
        int: The min no of coins needed, or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    coins = sorted(coins, reverse=True)  # Sort coins in descending order
    count = 0

    for coin in coins:
        if total <= 0:
            break
        num = total // coin
        count += num
        total -= num * coin

    if total != 0:
        return -1
    return count

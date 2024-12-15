#!/usr/bin/python3
"""
Prime Game: Determines the winner of multiple rounds of the game
"""

def is_prime(num):
    """
    Check if a number is prime.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
    """
    Determine who is the winner of the most rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of n values for each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben"), or None if it's a tie.
    """
    if not nums or x < 1:
        return None

    # Precompute prime numbers up to the maximum number in nums
    max_n = max(nums)
    is_prime_list = [False, False] + [True] * (max_n - 1)
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime_list[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime_list[j] = False

    # Precompute the number of primes up to each index
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if is_prime_list[i] else 0)

    # Initialize scores
    maria_wins = 0
    ben_wins = 0

    # Process each round
    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None


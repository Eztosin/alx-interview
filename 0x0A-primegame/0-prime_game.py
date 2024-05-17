#!/usr/bin/python3
"""
A Prime Game Module
"""


def is_prime(num):
    """
    Checks if a given number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Determines the winner of each game.

    Args:
        x (int): Number of rounds.
        nums (List[int]): Array of n for each round.

    Returns:
        str: Name of the player with the most wins.
             If the winner cannot be determined, returns None.
    """
    def count_primes(n):
        return sum(1 for i in range(1, n + 1) if is_prime(i))

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        num_primes = count_primes(n)
        if num_primes % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

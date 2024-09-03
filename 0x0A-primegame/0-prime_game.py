#!/usr/bin/python3
"""0-prime_game Module"""


def isWinner(x, nums):
    """Function determines the winner of the game
    Args:
        x: int, the number of points Maria has
        nums: list, the list of numbers Maria and Ben choose from
    Returns:
        str, the name of the winner or None if no winner
    """
    if x <= 0 or not nums:
        return None

    def sieve_of_eratosthenes(max_n):
        """Function to determine all primes up to the maximum number in nums
        Args:
            max_n: int, the maximum number in the list of numbers
        Returns:
            list, a list of booleans indicating whether a number is prime
        """
        primes = [True] * (max_n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(max_n**0.5) + 1):
            if primes[i]:
                for multiple in range(i*i, max_n + 1, i):
                    primes[multiple] = False
        return primes

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(primes[2:n + 1])

        if prime_count % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

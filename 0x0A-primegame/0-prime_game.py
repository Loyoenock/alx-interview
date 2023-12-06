#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(rounds, numbers):
    """rounds - number of rounds
    numbers - list of numbers
    """
    if rounds <= 0 or numbers is None:
        return None
    if rounds != len(numbers):
        return None

    ben = 0
    maria = 0

    sieve = [1 for _ in range(sorted(numbers)[-1] + 1)]
    sieve[0], sieve[1] = 0, 0
    for i in range(2, len(sieve)):
        remove_multiples(sieve, i)

    for num in numbers:
        if sum(sieve[0:num + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def remove_multiples(lst, x):
    """removes multiples
    of primes
    """
    for i in range(2, len(lst)):
        try:
            lst[i * x] = 0
        except (ValueError, IndexError):
            break

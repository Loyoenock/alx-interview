#!/usr/bin/python3

""" Defines the makeChange function"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet the given total.
    If the total is 0 or less, return 0.
    If the total cannot be met by any combination of the
    provided coins, return -1.
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if total == 0:
            return change
    return -1

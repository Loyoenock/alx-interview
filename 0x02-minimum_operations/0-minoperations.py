#!/usr/bin/python3
"""Module for minOperations"""


def minOperations(n):
    """
    minOperations
    Calculate the minimum number of operations required to obtain 'n' 'H' characters.
    """
    # All outputs should be at least 2 characters: (min, Copy All => Paste)
    if n < 2:
        return 0

    ops, root = 0, 2
    while root <= n:
        # If 'n' is evenly divisible by 'root'
        if n % root == 0:
            # The total even divisions by 'root' contribute to the total operations
            ops += root
            # Update 'n' to the remainder after division
            n = n // root
            # Decrease 'root' to find remaining smaller values that evenly divide 'n'
            root -= 1
        # Increment 'root' until it evenly divides 'n'
        root += 1

    return ops

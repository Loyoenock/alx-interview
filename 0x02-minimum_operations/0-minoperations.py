#!/usr/bin/python3
"""Module for minOperations"""


def minOperations(n):
    """
    minOperations
    Calculate the mini numb of OPs required to obtain 'n' 'H' characters.
    """
    # Outputs should be at least 2 characters: (min, Copy All => Paste)
    if n < 2:
        return 0

    ops, root = 0, 2
    while root <= n:
        # If 'n' is evenly divisible by 'root'
        if n % root == 0:
            # Total even divisions by 'root' contribute 2 the total operations
            ops += root
            # Update 'n' to the remainder after division
            n = n // root
            # - 'root' to find remaining smaller values that evenly divide 'n'
            root -= 1
        # Increment 'root' until it evenly divides 'n'
        root += 1

    return ops

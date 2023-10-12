#!/usr/bin/python3

def minOperations(n):
    """
    Calculate the minimum number of operations required to obtain 'n' 'H' characters.
    """
    # All outputs should be at least 2 characters: (min, Copy All => Paste)
    if n < 2:
        return 0

    operations, divisor = 0, 2

    while divisor <= n:
        # If 'n' is evenly divisible by 'divisor'
        if n % divisor == 0:
            # The total even divisions by 'divisor' contribute to the total operations
            operations += divisor
            # Update 'n' to the remainder after division
            n = n // divisor
            # Decrease 'divisor' to find remaining smaller values that evenly divide 'n'
            divisor -= 1

        # Increment 'divisor' until it evenly divides 'n'
        divisor += 1

    return operations

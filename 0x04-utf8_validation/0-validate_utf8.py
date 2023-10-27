#!/usr/bin/python3

"""
This script defines a function 'validUTF8' which checks
if a given data set is a valid UTF-8 encoding.
"""

def validUTF8(data):
    """
    Determines whether the provided data represents
    a valid UTF-8 encoding.
    """
    # Initialize a variable to track the number of expected bytes.
    number_bytes = 0

    # Define bit masks to check the leading bits of bytes.
    mask_1 = 1 << 7
    mask_2 = 1 << 6

    # Iterate through the input data.
    for i in data:

        # Initialize a mask for the leading bit of the current byte.
        mask_byte = 1 << 7

        if number_bytes == 0:

            # Count the number of leading 1s to determine byte length.
            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            # Validate byte length.
            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            # Check if the byte starts with '10' as per UTF-8 rules.
            if not (i & mask_1 and not (i & mask_2)):
                return False

        number_bytes -= 1

    # If the number of bytes is zero at the end, it's valid UTF-8.
    if number_bytes == 0:


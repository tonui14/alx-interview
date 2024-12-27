#!/usr/bin/python3
"""
Module to validate if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks for checking the leading bits of a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Only consider the least significant 8 bits of each integer
        byte &= 0xFF

        if num_bytes == 0:
            # Check how many leading 1s in the current byte
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # If no leading 1s, it's a 1-byte character
            if num_bytes == 0:
                continue

            # UTF-8 characters can only be 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte is a continuation byte (10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes left to process
        num_bytes -= 1

    # If num_bytes is not zero, we have an incomplete UTF-8 character
    return num_bytes == 0

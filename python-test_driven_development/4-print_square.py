#!/usr/bin/python3
"""
This function prints a square with the character #.
"""


def print_square(size):
    """Check to make sure the square is integer"""
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        """Iterate through size number and prints square(#)"""
        for i in range(size):
            print("#" * size)

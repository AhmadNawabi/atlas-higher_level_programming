#!/usr/bin/python3
"""This module contains tests for atlas-higher level programming"""


def add_integer(a, b=98):
    """check if two value are integers or float
     and return their sum as integer"""
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return int(a) + int(b)
    elif not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    else:
        raise TypeError('b must be an integer')

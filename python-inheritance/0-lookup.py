#!/usr/bin/python3
"""
This module provides a function for looking up attributes and methods of objects.
"""


def lookup(obj):
    """
    Return a list of attributes and methods available of the given object.
    """
    return (dir(obj))

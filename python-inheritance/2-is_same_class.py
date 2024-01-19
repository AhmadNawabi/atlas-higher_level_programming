#!/usr/bin/python3
"""This class take an object and
check if it is a subclass of another class
"""


def is_same_class(obj, a_class):
    """the is_same_class function
    checks if the class of the given
    object is equal to the specified
    class and returns True
    if they are the same,
    and False otherwise."""
    if obj.__class__ == a_class:
        return True
    else:
        return False

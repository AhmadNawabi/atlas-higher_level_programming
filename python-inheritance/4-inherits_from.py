#!/usr/bin/python3
"""
This is class checks if object
inherit from BaseClass
"""


def inherits_from(obj, a_class):
    """
    Checks if object inherits from a_class
    otherwise returns False
    """
    return (issubclass(type(obj), a_class)
            and type(obj) is not a_class)

#!/usr/bin/python3
"""
This module provides a function for looking up attributes and methods of objects.
"""

def lookup(obj):
    """
    Return a list of attributes and methods of the given object.

    Parameters:
    - obj: Any object for which to retrieve attributes and methods.

    Returns:
    A list of strings representing the attributes and methods of the object.
    The list includes only public attributes and methods, excluding internal
    methods that start with '__'.

    Example:
     class ExampleClass:
         def __init__(self, name):
             self.name = name

         def greet(self):
             print(f"Hello, {self.name}!")

    instance = ExampleClass("John")
    lookup(instance)
    ['greet', 'name']
    """
    return dir(obj)

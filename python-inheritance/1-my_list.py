#!/usr/bin/python3
"""
This class is used to sort a list
"""


class MyList(list):
    """define a print_sorted """
    def print_sorted(self):
        """print the sorted list"""
        print(sorted(self))

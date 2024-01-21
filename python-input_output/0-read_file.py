#!/usr/bin/python3
"""
Defines a text file-reading function.
"""


def read_file(filename=""):
    """Using with statement to make sure
    the file is closed automatic"""
    with open(filename, encoding="utf-8") as file:
        print(file.read())

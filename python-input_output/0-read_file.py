#!/usr/bin/python3
"""function that reads a text file (UTF8)
 and prints it to stdout"""


def read_file(filename=""):
    """Using with statement to make sure
    the file is closed automatic"""
    with open(filename, encoding="utf-8") as file:
        print(file.read())

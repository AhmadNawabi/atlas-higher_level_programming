#!/usr/bin/python3
"""
This function appends a string at the end of a text
"""


def append_write(filename="", text=""):
    """Used to append a string at the end of a text"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)

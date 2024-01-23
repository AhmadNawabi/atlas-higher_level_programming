#!/usr/bin/python3
"""Defines a text file-writing function."""


def write_file(filename="", text=""):
    """Writes content to the file named text."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)

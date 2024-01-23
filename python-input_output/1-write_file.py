#!/usr/bin/python3
"""Defines a text file-writing function."""


def write_file(filename="", text=""):
    """Writes content to the file named filename."""
    with open(filename, "w", encoding="utf-8") as file:
        print(len(text), file=file, end="")

#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle
"""Defines Square class that inherits from Rectangle"""


class Square(Rectangle):
    """Initioalize size of Square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

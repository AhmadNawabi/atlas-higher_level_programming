#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle
"""Defines Square class that inherits from Rectangle"""


class Square(Rectangle):
    """Initializes a Square size"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    """Defines and returns the size of the square"""
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

#!/usr/bin/python3
"""This class represents a rectangular"""


class Rectangle:
    """Initialize a rectangular object"""
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not width >= 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not height >= 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle
            and make sure the width is greater than 0
            and the value is integer.
        """
        try:
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if not value >= 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        except Exception as e:
            print(e)

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle and make sure the
        height is greater than 0 and the value is integer"""
        try:
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if not value >= 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        except Exception as e:
            print(e)

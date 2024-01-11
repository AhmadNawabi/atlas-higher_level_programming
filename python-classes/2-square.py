#!/usr/bin/python3

'''
This module create a Square class
'''


class Square:

    """
       This class represents a square.

       Attributes:
           __size (int): Private attribute
           representing the size of the square.

       Methods:
           __init__(self, size):
               Initializes a new instance of the Square
               class with a specified size.

       Example:
           # Create a square with a size of 5
           square_instance = Square(5)

       Note:
           The size attribute (__size) is marked as
           private with a double underscore.
       """

    def __init__(self, size=0):
        self.__size = size

        """
            Initializes a new instance of the Square
            class with a specified size.

            Parameters:
                size (int): The size of the square.
               """

        if not isinstance(self.__size, int):
            '''
            Attribute size must be an integer
            Otherwise raises an exception "size must be an integer"
            '''
            raise TypeError("size must be an integer")
            '''
            Attribute size must be greater than 0
            Otherwise raises an exception "size must be >= 0"
            '''

        if self.__size < 0:
            raise ValueError("size must be >= 0")

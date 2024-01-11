#!/usr/bin/python3
'''
This module create a square class
'''


class Square:

    """
       This class represents a square.

       Attributes:
           __size (int): Private attribute
            representing the size of the square.

       Methods:
           __init__(self, size):
               Initializes a new instance of the
                Square class with a specified size.

       Example:
           # Create a square with a size of 5
           square_instance = Square(5)

       Note:
           The size attribute (__size) is marked
            as private with a double underscore.
       """

    def __init__(self, size=0):
        """
            Initializes a new instance of the Square class with a specified size.

            Parameters:
            size (int): The size of the square.
        """
        self.__size = size

        if not isinstance(self.__size, int):
            '''
            Attribute size must be an integer
            Otherwise raises an exception "size must be an integer"
            '''
            raise TypeError("size must be an integer")

        if self.__size < 0:
            '''
            Attribute size must be greater than 0
            Otherwise raises an exception "size must be >= 0"
            '''
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """
        Gets the size of the square.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square using the property.

        Parameters:
             value (int): The new size to be set.

        Raises:
           TypeError: If the provided value is not an integer.
           ValueError: If the provided value is less than 0.
        """
        if self.__size < 0:
            self.__size = 0
        elif self.__size > 1000:
            self.__size = 1000
        else:
            self.__size = value

        if not isinstance(value, int):
            '''
            Attribute size must be an integer
            Otherwise raises an exception "size must be an integer"
            '''
            raise TypeError("size must be an integer")
        if self.__size < 0:
            '''
            Attribute size must be greater than 0
            Otherwise raises an exception "size must be >= 0"
            '''
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints a representation of the square using '#' characters.

        This method iterates through the rows and columns of the square,
        printing '#' characters to represent the shape. Each row is printed
        on a new line.

        Example:
            square_instance = Square(3)
            square_instance.my_print()

            Output:
            ###
            ###
            ###

        Note:
            If the size of the square is 0, an empty line is printed.
        """

        for height in range(self.__size):
            for width  in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()

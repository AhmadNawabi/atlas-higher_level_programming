'''
This module defines a Square class.
'''

class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): Private attribute representing the size of the square.

    Methods:
        __init__(self, size):
            Initializes a new instance of the Square class with a specified size.

    Example:
        # Create a square with a size of 5
        square_instance = Square(5)

    Note:
        The size attribute (__size) is marked as private with a double underscore.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class with a specified size.

        Parameters:
            size (int): The size of the square.
        """

        self.__size = size

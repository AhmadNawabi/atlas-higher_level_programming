#!/usr/bin/python3
"""This class defines a square and includes
methods for size manipulation,
    position management, area calculation,
    and printing the square pattern."""


class Square:
    """
    This class defines a square and includes
     methods for size manipulation,
    position management, area calculation,
     and printing the square pattern.

    Attributes:
    - size (int): The size of the square's sides.
    - position (tuple): The position of the
     square on the grid.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Methods:
    - __init__(self, size=0, position=(0, 0)):
     Initializes a Square instance with a given
      size and position.
    :param size: The size of the square's
     sides (default is 0).
    :param position: The position of the square
     on the grid (default is (0, 0))."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """- size(self): Getter method for
         retrieving the size of the square.
        :return: The size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """- size(self, value): Setter method
         for setting the size of the square.
        :param value: The new size to be set.
        :raises TypeError: If the provided size is not an integer.
        :raises ValueError: If the provided size is less than 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """- position(self): Getter method for
         retrieving the position of the square.
        :return: The position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """- position(self, value): Setter method for
         setting the position of the square.
            :param value: The new position to be set.
            :raises TypeError: If the provided position
             is not a tuple of two positive integers."""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) for i in value) or \
           not all(i >= 0 for i in value):
            raise TypeError("position must be a"
                            " tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """- area(self): Calculates and returns
         the area of the square.
            :return: The area of the square."""
        return self.__size ** 2

    def my_print(self):
        """- my_print(self): Prints the square
         pattern to the console."""
        if self.__size == 0:
            """If size is equal to 0, prints an empty line."""
            print()
        else:
            for _ in range(self.__position[1]):
                """Uses position to add spaces
                 when position[1] > 0."""
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

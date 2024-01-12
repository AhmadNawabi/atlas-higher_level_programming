#!/usr/bin/python3

class Square:
    """A class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Parameters:
        - size (int): The size of the square (default is 0).
        - position (tuple): The position
        of the square (default is (0, 0)).

        Raises:
        - TypeError: If size is not an integer
        or position is not a tuple.
        - ValueError: If size is less than 0.
        """
        self.__size = size
        self.__position = position

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """Getter method for the size property."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size property.

        Parameters:
        - value (int): The new size value.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than
        0 or greater than 1000.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        if value > 1000:
            self.__size = 1000
        else:
            self.__size = value

    @property
    def position(self):
        """Getter method for the position property."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position property.

        Parameters:
        - value (tuple): The new position value.

        Raises:
        - TypeError: If value is not a tuple or
        if it doesn't contain 2 positive integers.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square.

        If size is 0, prints an empty line. Otherwise,
        prints the square with the given position.

        The square is printed using "_" for the position's
        horizontal offset and "#" for the square itself.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print("_" * self.__position[0] + "#" * self.__size)

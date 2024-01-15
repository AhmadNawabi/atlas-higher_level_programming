#!/usr/bin/python3
"""This class represents a rectangular"""


class Rectangle:
    """This class represents a rectangle"""
    """And number of rectangle attributes in this class"""
    number_of_instances = 0
    """print_symbol is used to print any symbol on the screen"""
    print_symbol = "#"
    """Initialize a rectangular object"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        """Add a rectangle attribute to this class"""
        Rectangle.number_of_instances += 1

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle and make sure the
        height is greater than 0 and the value is integer"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Check if two rectangles are equal
         and is instance of Rectangle class"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """Print the rectangle with the width and height"""
        if self.__width == 0 or self.__height == 0:
            return ""

        result = ""
        """Iterate through the width and height of the rectangle
            and print the result as a string with the (#) character"""
        for i in range(self.__height):
            result += str(self.print_symbol) * self.__width
            if i < self.__height - 1:
                result += "\n"
        return result

    def __repr__(self):
        """Print the rectangle with the width and height"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Delete the rectangle from the class"""
        print("Bye rectangle...")
        """remove the rectangle from the class"""
        Rectangle.number_of_instances -= 1

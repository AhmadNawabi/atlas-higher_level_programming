#!/usr/bin/python3
"""
This is a Base Geometry class
"""


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        """Raises an Exception with the message
        'area() is not implemented'"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates the value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

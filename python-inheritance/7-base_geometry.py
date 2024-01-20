#!/usr/bin/python3
"""
This is an empty class
"""


class BaseGeometry:
    """an empty class"""
    pass

    def area(self):
        """This is an empty method
        that raise an Exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """This function is used to validate
        an integer"""
        """It checks if the value is an integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an
                    integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater
            than 0".format(name))

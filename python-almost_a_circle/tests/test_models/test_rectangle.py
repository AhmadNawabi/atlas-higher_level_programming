#!/usr/bin/python3
# test_rectangle.py
"""Defines unittests for rectangle.py."""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_is_class(self):
        """ obj id increments """
        r1 = Rectangle(2, 2, 3, 1)
        self.assertTrue(type(r1) is Rectangle and issubclass(Rectangle, Base))

        r2 = Rectangle(2, 6, 4, 2)
        self.assertIsInstance(r2, Rectangle)

    def test_2_values(self):
        """checks for valid input """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(1, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_3_values(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(2, 7)
        r3 = Rectangle(10, 2, 16)
        self.assertEqual(r1.id, r3.id - 2)

    def test_4_values(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(2, 7)
        r3 = Rectangle(10, 2, 16)
        r4 = Rectangle(10, 2, 16, 5)
        self.assertEqual(r1.id, r4.id - 3)

    def test_5_values(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(2, 7)
        r3 = Rectangle(10, 2, 16)
        r4 = Rectangle(10, 2, 16, 5)
        r5 = Rectangle(10, 2, 16, 5, 53)
        self.assertEqual(53, Rectangle(10, 2, 16, 5, 53).id)

    def test_one_arg_int_n(self):
        r1 = Rectangle(10, 2, 16, 4, -17)
        self.assertEqual(r1.id, -17)

    def test_one_arg_int_p(self):
        r1 = Rectangle(10, 2, 16, 4, 34)
        self.assertEqual(r1.id, 34)

    def test_str_arg(self):
        r7 = Rectangle(1, 11, 1, 1, "Holberton")
        self.assertEqual(r7.id, "Holberton")

    def test_type_error(self):
        """
        Test for check Type Error
        """
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Hello", 2)
            Rectangle(True, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "Hello")
            Rectangle(2, True)
            Rectangle(6, "2")

    def test_value_error(self):
        """
        Test for checking value error
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 2)
            Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -2)
            Rectangle(1, 0)

    def test_one_arg(self):
        """checks for valid error"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_none_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(7, None)
            Rectangle(None, 6)

    def test_str_two_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "4")

    def test_str_zero_arg(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_str_zero_arg(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_str_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 16, "Holberton")
            Rectangle(10, 2, 16, "Betty", "Holberton")

    def test_zero_arg(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 0, 0, 0, 0)

    def test_float_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2.0, 1, 1, 12)

    def test_six_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, 1, 12, 5)


if __name__ == "__main__":
    unittest.main()


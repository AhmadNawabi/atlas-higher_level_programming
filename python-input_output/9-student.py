#!/usr/bin/python3
"""
This Student class defines a student by:

Public instance attributes:
first_name
last_name
age
"""


class Student:
    """initialize first name, last name and age"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """that retrieves a dictionary representation
     of a Student instance"""
    def to_json(self):
        return self.__dict__

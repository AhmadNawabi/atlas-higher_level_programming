#!/usr/bin/python3
"""
Import required modules from json
"""
import json
"""
Writes the JSON representation of the
object to a text file.
"""


def save_to_json_file(my_obj, filename):
    """
    Writes the JSON representation of the object to a text file.
    :param my_obj: The object to be serialized.
    :param filename: The name of the file to write to.
    :return: True if successful, False otherwise.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
    return file

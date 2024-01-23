#!/usr/bin/python3
"""
import json
"""
from flask import json
"""
This function creates an Object from a “JSON file”
"""


def load_from_json_file(filename):
    """Load an object from a JSON file"""
    with open(filename) as file:
        json_data = json.load(file)
        return json_data

#!/usr/bin/python3
"""
Import json
"""


import json
"""
Define a function that takes a json string
"""
def to_json_string(my_obj):
    """Returns the JSON representation
     of the given object."""
    return json.dumps(my_obj)

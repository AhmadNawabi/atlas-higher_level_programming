#!/usr/bin/python3
"""Load, add, save"""


import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_items_to_list_and_save(arguments):
    try:
        """Load existing items from file"""
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        """If file doesn't exist, create an empty list"""
        items = []

    """Add new arguments to the list"""
    items.extend(arguments)

    """Save the updated list to the file"""
    save_to_json_file(items, "add_item.json")

if __name__ == "__main__":
    """Get command-line arguments excluding the script name"""
    arguments = sys.argv[1:]

    if arguments:
        add_items_to_list_and_save(arguments)
        print("Items added successfully and saved to add_item.json.")
    else:
        print("No items provided.")

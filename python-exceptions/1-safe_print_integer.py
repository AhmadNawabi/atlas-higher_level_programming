#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print(int(value))
    except ValueError:
         print("{} is not an integer".format(value))
         return False
    return True

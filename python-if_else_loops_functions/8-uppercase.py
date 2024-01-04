#!/usr/bin/python3

def uppercase(str):
    for upper in str:
        upper_char = chr(ord(upper) - 32) if 97 <= ord(upper) <= 122 else upper
        print("{}".format(upper_char), end="")
    print()

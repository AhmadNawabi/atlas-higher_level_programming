#!/usr/bin/python3

def no_c(my_string):
    """Removing c and C from string """

    copyOfString = [copy for copy in my_string if "c" != copy != "C"]
    print(''.join(copyOfString))

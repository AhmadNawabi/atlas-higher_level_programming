#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for num in range(x):
            value = my_list[num]
            if isinstance(value, int):
                print("{:d}".format(value), end='')
                count = count + 1
    except (IndexError, TypeError, ValueError):
        pass
    print()
    return count

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count_ = 0
        for i in range(x):
            print(my_list[i], end="")
            count_ += 1
    except IndexError:
        pass
    except ValueError:
        pass
    print()
    return count_

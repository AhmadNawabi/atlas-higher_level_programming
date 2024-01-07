#!/usr/bin/python3

def only_diff_elements(set_1, set_2):

    onlyOneSet = set()

    for element in set_1:
        onlyOneSet.add(element)
        for element in set_2:
            onlyOneSet.add(element)

    return onlyOneSet

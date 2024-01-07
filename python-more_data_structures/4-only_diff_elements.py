#!/usr/bin/python3

def only_diff_elements(set_1, set_2):

    different_elements_set = set()

    different_elements_set.update(element for element in set_1 if element not in set_2)
    different_elements_set.update(element for element in set_2 if element not in set_1)

    return different_elements_set

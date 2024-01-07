#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    common_elements = set()

    for element in set_1:
        if element != set_2:
            common_elements.add(element)
            for other_element in set_2:
                common_elements.add(other_element)
    return common_elements

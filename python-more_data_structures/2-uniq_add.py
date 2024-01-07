#!/usr/bin/python3

def uniq_add(my_list=[]):

    unique_number = set()
    for number in my_list:
        unique_number.add(number)
    sumOfNumber = sum(unique_number)
    return sumOfNumber

#!/usr/bin/python3

def divisible_by_2(my_list=[]):
     # Create a new list to store True/False values
    result_list = []

    # Iterate through the original list
    for num in my_list:
        # Check if the number is a multiple of 2
        isDivisibleBy_2 = num % 2 == 0
        result_list.append(isDivisibleBy_2)
    return result_list

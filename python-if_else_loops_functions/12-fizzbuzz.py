#!/usr/bin/python3
def fizzbuzz():

    for number in range(1, 101):
        result = num(number)
        print("{} ".format(result), end="")


def num(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    else:
        return n

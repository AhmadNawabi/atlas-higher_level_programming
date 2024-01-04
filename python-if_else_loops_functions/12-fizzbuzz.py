#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 100):
        result = num(number)
        print(result, end=" ")

def num(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


fizzbuzz()

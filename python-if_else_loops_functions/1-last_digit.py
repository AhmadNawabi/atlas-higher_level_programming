import random as rd
number = rd.randint(-1000, 1000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
if digit > 5:
    print(f"Last digit of {number} is {digit} and grater than 5")
elif digit == 0:
    print(f"Last digit of {number} is {digit} and is 0")
else:
    print(f"Last digit of {number} is {digit} less than 6 but not 0") 

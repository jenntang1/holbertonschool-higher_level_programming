#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

""" change random number to positive """
positive = number * -1

""" retrieve the last digit of the now positive random number """
last = positive % 10

""" print statement for if last digit is 0 """
if last == 0:
    print("Last digit of", number, "is 0 and is 0")

elif number < 0:
    """
    1. if number is negative, change last digit back to negative
    2. print statement for if last digit is less than 6 but not 0
    3. print statement for if last digit is greater than 5
    """
    last = last * -1
    if last < 6:
        print("Last digit of", number, "is {:d} and is less than 6 and not 0\
                ".format(last))
    if last > 5:
        print("Last digit of", number, "is {:d} and is greater than 5\
                ".format(last))
elif number > 0:
    """
    1. if number is positive, do not use positive variable
    2. print statement for if last digit is less than 6 but not 0
    3. print statement for if last digit is greater than 5
    """
    last = number % 10
    if last < 6:
        print("Last digit of", number, "is {:d} and is less than 6 and not 0\
                ".format(last))
    if last > 5:
        print("Last digit of", number, "is {:d} and is greater than 5\
                ".format(last))

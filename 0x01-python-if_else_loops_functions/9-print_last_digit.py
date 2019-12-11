#!/usr/bin/python3
def print_last_digit(number):
    if number % 10 == 0:
        print("0", end="")
        return number % 10
    elif number < 0:
        number = number * -1
        last = number % 10
        print("{}".format(last), end="")
        return last
    elif number > 0:
        last = number % 10
        print("{}".format(last), end="")
        return last

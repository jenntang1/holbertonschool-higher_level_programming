#!/usr/bin/python3
def uppercase(str):
    for iterate in str:
        if ord(iterate) >= 97 and ord(iterate) <= 122:
            iterate = chr(ord(iterate) - 32)
        print("{}".format(iterate), end="")
    print()

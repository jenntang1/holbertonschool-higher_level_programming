#!/usr/bin/python3
def uppercase(str):
    for iterate in str:
        if iterate >= 'a' and iterate <= 'z':
            newstr = chr((ord(iterate) - 32))
        else:
            newstr = iterate
        print("{}".format(newstr), end="")
    print("{}".format(newstr))

#!/usr/bin/python3
for numbers in range(00, 100):
    if numbers <= 98:
        print("{:02d}, ".format(numbers), end="")
if numbers == 99:
    print("{:d}".format(numbers))

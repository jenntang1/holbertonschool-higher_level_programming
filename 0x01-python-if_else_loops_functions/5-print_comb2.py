#!/usr/bin/python3
""" loop through range and print up to 98, separated by comma and space """
for numbers in range(00, 100):
    if numbers <= 98:
        print("{:02d}".format(numbers), end=", ")

""" if number is 99, print it and a new line """
if numbers == 99:
    print("{:d}".format(numbers), end="\n")

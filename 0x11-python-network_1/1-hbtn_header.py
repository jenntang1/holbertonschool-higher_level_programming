#!/usr/bin/python3
""" Displays value of X-Request-Id """


import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.info()
        for key, value in header.items():
            if key == 'X-Request-Id':
                print("{}".format(value))

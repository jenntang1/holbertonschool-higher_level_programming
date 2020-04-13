#!/usr/bin/python3
""" Displays value of X-Request-Id """


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    header = response.headers['X-Request-Id']
    print("{}".format(header))

#!/usr/bin/python3
""" Displays value of X-Request-Id """


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print("{}".format(response.headers.get('X-Request-Id')))

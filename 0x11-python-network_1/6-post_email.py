#!/usr/bin/python3
""" POST Request """


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    response = requests.post(url, data=values)
    print("{}".format(response.text))

#!/usr/bin/python3
""" POST Request """


import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    request = urllib.parse.urlencode(values).encode('utf-8')
    with urllib.request.urlopen(url, data=request) as response:
        body = response.read().decode('utf-8')
        print("{}".format(body))

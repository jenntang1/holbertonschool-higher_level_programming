#!/usr/bin/python3
""" Error Code Handling """


import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read()
            print("{}".format(body.decode('utf-8')))
    except urllib.error.HTTPError as status:
            print("Error code: {}".format(status.code))

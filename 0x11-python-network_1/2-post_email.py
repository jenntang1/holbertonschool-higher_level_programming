#!/usr/bin/python3
""" POST Request """


import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    values = {}
    values['email'] = email

    data = urllib.parse.urlencode(values).encode('utf-8')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print("Your email is: {}".format(body))

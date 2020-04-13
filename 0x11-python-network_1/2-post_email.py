#!/usr/bin/python3
""" POST Request """


import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {}
    values['email'] = email
    request = urllib.request.Request(url, method='POST', headers=values)
    with urllib.request.urlopen(request) as response:
        response.read().decode('utf-8')
        print("Your email is: {}".format(email))

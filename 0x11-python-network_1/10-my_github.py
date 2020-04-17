#!/usr/bin/python3
""" Search in Github API """


import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    auth = {'Authorization': 'token {}'.format(password)}
    response = requests.get(url, headers=auth).json()
    if response.get('id'):
        print("{}".format(response.get('id')))
    else:
        print("None")

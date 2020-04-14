#!/usr/bin/python3
""" Search in Github API """


import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    github = 'https://api.github.com/users/'
    url = github + username
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    json_dict = response.json()
    for key, value in json_dict.items():
        if key == 'id':
            print("{}".format(value))
    else:
        print("None")

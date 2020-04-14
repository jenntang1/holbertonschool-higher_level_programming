#!/usr/bin/python3
""" Search in Github API """


import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    github = 'https://api.github.com/'
    url = github + username
    response = requests.get(url, auth=(username, password))
    json_dict = response.json()
    print("{}".format(json_dict["id"]))

#!/usr/bin/python3
""" Search for Last 10 Commits in a Github Repo """


import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    response = requests.get(url).json()
    if response:
        for item in range(0, 10):
            try:
                print("{}: {}".format(response[item].get('sha'),
                                      response[item].get('commit')
                                      .get('author').get('name')))
            except:
                pass

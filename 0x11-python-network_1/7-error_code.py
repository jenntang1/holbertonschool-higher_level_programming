#!/usr/bin/python3
""" Error Code Handling """


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("{}".format(response.text))
    except requests.HTTPError as status:
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))

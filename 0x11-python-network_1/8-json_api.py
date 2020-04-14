#!/usr/bin/python3
""" Search API """


import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
        print("No result")

    elif sys.argv[1].isalpha() is False:
        print("No result")

    else:
        url = 'http://0.0.0.0:5000/search_user'
        q = sys.argv[1]
        values= {'q': q}
        response = requests.post(url, data=values)
        try:
            json_dict = response.json()
            print("[{}] {}".format(json_dict["id"], json_dict["name"]))
        except ValueError:
            print("Not a valid JSON")
        else:
            print("No result")

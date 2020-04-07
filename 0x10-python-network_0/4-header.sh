#!/bin/bash
# This bash script takes in a URL, sends GET request and displays the body.
curl -sX GET "$1" -H "X-HolbertonSchool-User-Id: 98"

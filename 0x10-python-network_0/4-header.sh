#!/bin/bash
# This bash script takes in a URL, sends GET request and displays the body.
curl "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"

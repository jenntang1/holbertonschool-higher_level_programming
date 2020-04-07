#!/bin/bash
# This bash script takes in a URL, sends a request to that URL and displays the body of 200.
curl -sLX GET "$1"

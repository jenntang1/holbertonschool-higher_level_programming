#!/bin/bash
# This bash script takes in a URL, sends a request to that URL and displays the body of 200.
if curl -sI "$1" | grep -q '200 OK'
then
	curl -s "$1"
fi

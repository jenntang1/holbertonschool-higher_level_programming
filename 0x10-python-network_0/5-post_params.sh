#!/bin/bash
# This bash script takes in a URL, sends POST request and displays the body.
curl -sX POST "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"

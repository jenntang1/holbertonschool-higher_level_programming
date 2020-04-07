#!/bin/bash
# This bash script takes in a URL, sends POST request and displays the body.
curl "$1" -X POST -d "email: hr@holbertonschool.com&subject: I will always be here for PLD"

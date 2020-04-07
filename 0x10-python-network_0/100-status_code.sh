#!/bin/bash
# This bash script sends request and displays the status code.
curl -sLI "$1" -o /dev/null -w '%{http_code}\n'

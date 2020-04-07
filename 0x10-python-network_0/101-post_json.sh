#!/bin/bash
# This bash script sends a JSON POST request and displays the body.
curl -sd "$2" -H "Content-Type: application/json" -X POST "$1"

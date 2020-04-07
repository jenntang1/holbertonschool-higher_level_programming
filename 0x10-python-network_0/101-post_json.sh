#!/bin/bash
# This bash script sends a JSON POST request and displays the body.
curl -sH "Content-Type: application/json" -X POST -d "@$2" "$1"

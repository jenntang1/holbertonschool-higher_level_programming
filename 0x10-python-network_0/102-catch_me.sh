#!/bin/bash
# This bash script sends request to 0.0.0.0:5000/catch_me and follows its redirection.
curl -sLX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"

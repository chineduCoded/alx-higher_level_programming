#!/bin/bash
# Send a POST request with custom header
curl -sL -X PUT 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool" -d "user_id=98"

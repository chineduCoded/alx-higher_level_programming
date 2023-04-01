#!/bin/bash
# cURL a JSON file
curl -s -X POST -H "Content-Type: application/json" "$1" "@{$2}"

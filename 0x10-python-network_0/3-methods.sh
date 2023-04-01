#!/bin/bash
# Get all HTTP methods the server will accept
curl -i -sX OPTIONS "$1"

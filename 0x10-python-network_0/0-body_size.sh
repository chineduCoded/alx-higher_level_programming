#!/bin/bash
# shows the bytes size of the HTTP response header
curl -s "$1" | wc -c

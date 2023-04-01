#!/usr/bin/python3
"""
Post an Email
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    # Get the URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    values = {"email": email}
    data = urllib.parse.urlencode(values).encode("utf-8")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as r:
        print(r.read().decode("utf-8"))

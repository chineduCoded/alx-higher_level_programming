#!/usr/bin/python3
"""
Displays the value of the X-Request-Id
"""
import sys
import urllib.request


def fetch_x_request_id(url):
    """
    Returns X-Request-Id variable found in the header of the response.
    """
    with urllib.request.urlopen(url) as res:
        headers = res.info()
        print(headers['X-Request-Id'])


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_x_request_id(url)

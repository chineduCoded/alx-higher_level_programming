#!/usr/bin/python3
"""Fetches status from hhtps://intranet.hbtn.io/status"""
import urllib.request


def fetch_data():
    """
    Function to print a response of a url
    """
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        html = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))


if __name__ == "__main__":
    fetch_data()

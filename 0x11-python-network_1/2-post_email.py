#!/usr/bin/python3
"""
Post an Email
"""
import urllib.parse
import urllib.request
import sys


def send_post_request(url, email):
    """
    Sends POST request to an url
    Params:
        url(str): the url to send POST request
        email(str): to receive POST request
    Returns: Decoded email
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf8')
    with urllib.request.urlopen(url, data) as res:
        output = res.read().decode("utf-8")
        print(output)


if __name__ == "__main__":
    # Get the URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    print(f"Your email is: {email}")

    send_post_request(url, email)

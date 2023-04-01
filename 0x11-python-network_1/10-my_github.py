#!/usr/bin/python3
"""
Access Github and use user info
"""
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    auth = HTTPBasicAuth(username, password)

    res = requests.get(url, auth=auth)
    data = res.json()

    if 'id' in data:
        print(data['id'])
    else:
        print("None")

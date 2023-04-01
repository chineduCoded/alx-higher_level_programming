#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'

    res = requests.get(url, auth=(username, password))
    data = res.json()

    if 'id' in data:
        print(data['id'])
    else:
        print("Could not retrieve user ID")

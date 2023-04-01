#!/usr/bin/python3
"""
Takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    res = requests.post(url, data=data)

    try:
        json_dict = res.json()
        if json_dict:
            print("[{}] {}".format(json_dict.get("id"), json_dict.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

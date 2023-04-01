#!/usr/bin/python3
"""
List 10 commits (from the most recent to oldest)
of the repository
"""
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    res = requests.get(url)
    commits = res.json()

    for commit in commits[:10]:
        print(f"{commit['sha']}: {commit['commit']['author']['name']}")

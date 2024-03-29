#!/usr/bin/python3
"""Time for an interview!"""


if __name__ == "__main__":
    import requests
    import sys

    repo = sys.argv[1]
    user = sys.argv[2]
    url = "https://api.github.com/repos/" + user + "/" + repo + "/commits"
    r = requests.get(url)
    for commit in r.json()[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))

#!/usr/bin/python3
""" sends a request and displays the value of the X-Request-Id variable"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))

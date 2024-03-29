#!/usr/bin/python3
""" Takes a url and displays the value of the X-Request-Id variable"""


if __name__ == "__main__":
    import urllib.request
    from sys import argv

    url = argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))

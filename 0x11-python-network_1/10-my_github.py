#!/usr/bin/python3
""" Takes Github credentials and uses the Github API to display the user id"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(argv[1], argv[2]))
    print(r.json().get('id'))

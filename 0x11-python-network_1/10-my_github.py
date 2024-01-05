#!/usr/bin/python3
""" python script
    demonstrate urlib package
"""


if __name__ == '__main__':
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    username = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBasicAuth(username, password)
    res = requests.get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))

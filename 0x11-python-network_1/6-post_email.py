#!/usr/bin/python3
""" python script
    demonstrate urlib package
"""


if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as res:
        print(dict(res.headers).get("X-Request-Id"))

#!/usr/bin/python3
""" python script
    demonstrate urlib package
"""


if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    dic_val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(dic_val).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as res:
        print(res.read().decode("utf-8"))

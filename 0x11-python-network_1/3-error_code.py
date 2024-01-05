#!/usr/bin/python3
""" python script
    demonstrate urlib package
"""


if __name__ == '__main__':
    from urllib import parse, error, request
    import sys

    url = sys.argv[1]

    try:
        with request.urlopen(url) as res:
            print(res.read().decode("utf-8"))
    except error.HTTPError as error:
        print("Error code:", error.code)

#!/usr/bin/python3
""" python script
    demonstrate urlib package
"""


if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]

    re = requests.get(url)
    print(re.headers.get("X-Request-Id"))

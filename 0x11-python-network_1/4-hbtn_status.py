#!/usr/bin/python3
""" python script
    demonstrate urlib package
"""


if __name__ == '__main__':
    import requests

    request = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print(" - type: {}".format(type(request.text)))
    print(" - content: {}".format(request.text))

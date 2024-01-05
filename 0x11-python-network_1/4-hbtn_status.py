#!/usr/bin/python3
""" python script
    demonstrate urlib package
"""


if __name__ == '__main__':
    import requests

    response = requests.get("https://intranet.hbtn.io/status")
    result = (
            "Body response:\n"
            f"\t- type: {type(response.text)}\n"
            f"\t- content: {response.text}"
            )
    print(result)

#!/usr/bin/python3
""" python script
    demonstrate urlib package
"""


if __name__ == '__main__':
    import requests
    import sys

    repository = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
            repository, owner)
    res = requests.get(url)
    commits = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass

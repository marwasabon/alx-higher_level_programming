#!/usr/bin/python3
"""
This is a Python script..

"""


def append_write(filename=“”, text=“”):

    count = 0

    with open(filename, “a”, encoding=“utf-8”) as file:

        file.write(text)

        count = len(text)

        return count

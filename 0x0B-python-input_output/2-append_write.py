#!/usr/bin/python3
"""
This is a Python script..

"""


def append_write(filename="", text=""):
    '''
    Write a function that appends a string at the
    end of a text file (UTF8) and returns
    the number of characters added:
    '''

    count = 0

    with open(filename, "a", encoding="utf-8") as file:

        file.write(text)

        count = len(text)

        return count

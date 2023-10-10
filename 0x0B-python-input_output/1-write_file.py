#!/usr/bin/python3
"""
This is a Python script..

"""


def write_file(filename="", text=""):
    '''
    unction that writes a string to a text file (UTF8)
    returns the number of characters written:
    '''

    with open(filename, "w", encoding="utf-8") as file:
        return (file.write(text))

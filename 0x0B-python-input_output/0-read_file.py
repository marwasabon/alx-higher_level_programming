#!/usr/bin/python3
"""
This is a Python script..

"""


def read_file(filename=""):
    '''
    Write a function that reads a text file (UTF8) and prints it to stdout:
    '''
    with open(filename, "r", encoding="utf8") as file:
        for line in file:
            print(line, end="")

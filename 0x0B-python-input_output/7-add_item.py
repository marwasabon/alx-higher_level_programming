#!/usr/bin/python3
"""
This is a Python script..

"""

import json


def load_from_json_file(filename):
    '''
    Write a script that adds all arguments to a
    Python list, and then save them to a file:
    '''

    with open(filename, 'r') as file:

        json_string = file.read()

        obj = json.loads(json_string)

        return obj

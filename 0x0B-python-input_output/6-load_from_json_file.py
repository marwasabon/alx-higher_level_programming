#!/usr/bin/python3
"""
This is a Python script..

"""

import json


def load_from_json_file(filename):
    '''
    Write a function that creates an Object from a “JSON file”
    '''

    with open(filename, 'r') as file:

        json_string = file.read()

        obj = json.loads(json_string)

        return obj

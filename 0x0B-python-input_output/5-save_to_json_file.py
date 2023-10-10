#!/usr/bin/python3
"""
This is a Python script..

"""


import json


def save_to_json_file(my_obj, filename):

    with open(filename, ‘w’) as file:

        json.dump(my_obj, file)

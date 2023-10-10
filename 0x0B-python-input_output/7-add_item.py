#!/usr/bin/python3
"""
This is a Python script..

"""

import json
import sys


from 5-save_to_json_file.py import *
from 6-load_from_json_file.py import *


def load_from_json_file(filename):
    '''
    Write a script that adds all arguments to a
    Python list, and then save them to a file:
    '''
    with open(filename, 'r') as file:
        json_string = file.read()
        obj = json.loads(json_string)
        return obj


def save_to_json_file(my_obj, filename):
    '''
    this is save to json file
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
        filename = "add_item.json"
        my_list = load_from_json_file(filename)
        my_list.extend(sys.argv[1:])
        save_to_json_file(my_list, filename)

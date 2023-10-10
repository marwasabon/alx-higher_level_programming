#!/usr/bin/python3
"""
This is a Python script..

"""

import json
import sys


def load_from_json_file(filename):
    '''
    Write a script that adds all arguments to a
    Python list, and then save them to a file:
    '''

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
        except FileNotFoundError:
            return []

        def save_to_json_file(my_obj, filename):
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(my_obj, f)
                filename = "add_item.json"
                my_list = load_from_json_file(filename)
                my_list.extend(sys.argv[1:])
                save_to_json_file(my_list, filename)

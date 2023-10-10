#!/usr/bin/python3
"""
This is a Python script..

"""

import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
'''
this os new
'''

try:
    my_list = load_from_json_file(filename)

except FileNotFoundError:
    my_list = []

# Add all arguments to the list
    my_list.extend(sys.argv[1:])

# Save the updated list to the file
    save_to_json_file(my_list, filename)

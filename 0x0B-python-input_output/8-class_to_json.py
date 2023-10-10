#!/usr/bin/python3
"""
This is a Python script..

"""

import json


def class_to_json(obj):
    '''
    Write a function that returns the dictionary
    description with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object:
    '''

    if isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, bool):
        return obj
    elif hasattr(obj, '__dict__'):
        return class_to_json(obj.__dict__)
    else:
        return None

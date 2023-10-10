#!/usr/bin/python3
"""
This is a Python script..

"""


def class_to_json(obj):
    '''
    Write a function that returns the dictionary
    description with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object:
    '''
    if isinstance(obj, list):
        return obj
    elif isinstance(obj, dict):
        return obj
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, bool):
        return obj
    elif hasattr(obj, '__dict__'):
        return {
                key: class_to_json(value)
                for key, value in obj.__dict__.items()
                }
    else:
        return None
    else:
        return None

#!/usr/bin/python3
"""
This is a Python script..

"""


class Student:
    '''
    this is student class
    '''

    def __init__(self, first_name, last_name, age):
        '''
        this instializing this class
        '''

        self.first_name = first_name

        self.last_name = last_name

        self.age = age

    def to_json(self, attrs=None):

        '''
        function that returns the dictionary
        description with simple data structure (list, dictionary, string,
        integer and boolean) for JSON serialization of an object:
        '''
        if attrs is None:
            return self.__dict__
        else:
            return {
                    attr: getattr(self, attr)
                    for attr in attrs
                    if hasattr(self, attr)
                    }

    def reload_from_json(self, json):
        for attr, value in json.items():
            setattr(self, attr, value)

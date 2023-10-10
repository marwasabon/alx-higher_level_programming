#!/usr/bin/python3
"""
This is a Python script..

"""


class Student:
    '''
    this is student class
    '''

    def init(self, first_name, last_name, age):
        '''
        this instializing this class
        '''

        self.first_name = first_name

        self.last_name = last_name

        self.age = age

    def to_json(self):
        '''
        function that returns the dictionary
        description with simple data structure (list, dictionary, string,
        integer and boolean) for JSON serialization of an object:
        '''
        return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }

#!/usr/bin/python3
""" base class """

import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
        first class Base:
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
         returns the JSON string representation of list_dictionaries:
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
         writes the JSON string representation of list_objs to a file:
         '''
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        json_dict = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(json_dict)
        with open(filename, 'w') as file:
            file.write(json_str)

    def from_json_string(json_string):
        '''
        returns the list of the JSON 
        string representation json_string:
        '''
        if json_string is None or json_string == '':
            return []
        else:
            return eval(json_string)

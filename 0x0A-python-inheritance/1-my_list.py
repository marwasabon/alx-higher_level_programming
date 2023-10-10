#!/usr/bin/python3
"""
This is a Python script that defines a class named mylist..

"""


class MyList(list):
    '''
    Write a class MyList that inherits from list:
    '''
    def print_sorted(self):
        '''
        this is my first function that sorts
        '''
        print(sorted(self))

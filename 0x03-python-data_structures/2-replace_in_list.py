#!/usr/bin/python3
def replace_in_list(my_list, inx, element):
    if 0 <= inx < len(my_list):
        my_list[inx] = element
    return my_list

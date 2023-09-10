#!/usr/bin/python3
def new_in_list(my_list, inx, element):
    new_list = my_list.copy()
    if inx >= len(my_list) or inx < 0:
        return new_list

    new_list[inx] = element
    return new_list

#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list or len(my_list) == 0:
        return None

    the_max = my_list[0]

    for i in my_list:
        if the_max < i:
            the_max = i
    return the_max

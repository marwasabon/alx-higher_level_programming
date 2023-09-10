#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is '' or len(my_list) is 0:
        return None

    max = my_list[0]

    for i in my_list:
        if max < i:
            max = i
    return max

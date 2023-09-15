#!/usr/bin/python3
def best_score(a_dictionary):

    if a_dictionary is None or len(list(a_dictionary.keys())) is 0:

        return None
    start = 0

    for key in my_dict:
        if start is 0:
            holder = key
            score = a_dictionary[key]
            start = 1

        if a_dictionary[key] > score:
            score = a_dictionary[key]
            holder = key

    return holder

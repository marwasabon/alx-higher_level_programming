#!/usr/bin/python3
def best_score(a_dictionary):

    if (not a_dictionary or len(list(a_dictionary.keys())) == 0):

        return None

    start = 0

    for key in a_dictionary:
        if start == 0:
            holder = key
            score = a_dictionary[key]
            start = 1

        if a_dictionary[key] > score:
            score = a_dictionary[key]
            holder = key

    return holder

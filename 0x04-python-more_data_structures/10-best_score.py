#!/usr/bin/python3
def best_score(a_dictionary):

    if a_dictionary is None or len(list(my_dict.keys())) is 0:

        return None
    start = 0

    for key in my_dict:
        if start is 0:
            holder = key
            score = my_dict[key]
            start = 1

        if my_dict[key] > score:
            score = my_dict[key]
            holder = key

    return holdergg

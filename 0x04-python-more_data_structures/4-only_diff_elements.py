#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    temp = list(set_1) + list(set_2)
    new_set = set()

    for i in range(len(temp)):
        if temp_list.count(temp[i]) == 1:
            new_set.append(temp[i])

    return set(new_set)

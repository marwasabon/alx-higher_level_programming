#!/usr/bin/python3
def roman_to_int(roman_string):
    if not (isinstance(roman_string, str)):
        return 0

    roman_dict = dict(M=1000, C=100, D=500, X=10, L=50, V=5, I=1)
    result = 0

    for i in range(len(roman_string)):
        if i > 0 and roman_dict[roman_string[i]] > roman_dict[roman_string[i-1]]:
            result += roman_dict[roman_string[i]] - 2 * roman_dict[roman_string[i-1]]
        else:
            result += roman_dict[roman_string[i]]

    return result

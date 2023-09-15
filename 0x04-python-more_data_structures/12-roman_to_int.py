#!/usr/bin/python3
def roman_to_int(roman_string):
    if not (isinstance(roman_string, str)):
        return 0
    roman_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    result = 0
    prev = 0

    for i in range(len(roman_string)-1, -1, -1):
        current = roman_dict[roman_string[i]]
        if current >= prev:
            result += current
        else:
            result -= current
            prev = current
    return result

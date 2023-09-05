#!/usr/bin/python3
def uppercase(str):
    for ca in str:
        if 'a' <= ca <= 'z':
            ca = (chr(ord(ca) - 32))
        print("{}".format(ca), end="")
    print()

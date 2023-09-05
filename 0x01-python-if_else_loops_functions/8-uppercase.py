#!/usr/bin/python3
def uppercase(str):
    for ca in str:
        if ord('a') <= ord(ca) <= ord('z'):
            ca = (chr(ord(ca) - 32))
        print("{}".format(ca), end="")
    print()

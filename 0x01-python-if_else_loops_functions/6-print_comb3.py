#!/usr/bin/python3
# fix indent
for i in range(80):
    if i / 10 < i % 10:
        print("{:02}, ".format(i), end="")
print("89")

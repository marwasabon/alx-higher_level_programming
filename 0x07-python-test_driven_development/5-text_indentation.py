#!/usr/bin/python3
"""
This is a Python script that defines add_integer(a, b)
"""

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".:?":
        text = text.replace(char, char + "\n\n")
        lines = [line.strip() for line in text.split("\n")]
        text = "\n".join(lines)
        print(text)

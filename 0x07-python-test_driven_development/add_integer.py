#!/usr/bin/python3
"""
This is a Python script that defines add_integer(a, b)
"""


def add_integer(a, b=98):
    """
    add_integer:
    Returns the sum of a and b, cast as int if float
    raise error if not int or float types
    >>> add_integer(2, 3)
    5

    >>> add_integer(-5, 10)
    5

    >>> add_integer(0, 0)
    0

    >>> add_integer(100, -50)
    50

    >>> add_integer(0, 5)
    5
    """

    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

#!/usr/bin/python3
'''
    Integer addition module
'''


def add_integer(a, b=98):
    """
    A Function that adds two integers
    """

    a_type = type(a)
    b_type = type(b)

    if (a_type is not int):
        if (a_type is float):
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if (b_type is not int):
        if (b_type is float):
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return (a + b)

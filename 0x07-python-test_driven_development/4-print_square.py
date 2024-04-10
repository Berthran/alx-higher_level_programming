#!/usr/bin/python3
"""
    A simple python module for printing a square

    Functions:
    print_square: prints a square with the character "#"
"""


def print_square(size):
    """
    Prints a square with the character "#"

    Parameters:
        size: the length of the square

    Returns: Nothing
    """

    err_msg_1 = "size must be an integer"
    err_msg_2 = "size must be >= 0"

    if (type(size) is not int):
        raise TypeError(err_msg_1)

    if (size < 0):
        raise ValueError(err_msg_2)

    for i in range(size):
        print("{}".format("#" * size))

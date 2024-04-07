#!/usr/bin/python3
"""
    A simple module for name printing

    Functions:
        say_my_name: displays a name in <first name> <last name> format
"""


def say_my_name(first_name, last_name=""):
    """
    Prints [My name is <first name> <last name>]

    Parameters:
        first_name: a string character of the first name
        last_name: a string character of the last name

    Return: nothing
    """

    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    if (type(last_name) is not str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

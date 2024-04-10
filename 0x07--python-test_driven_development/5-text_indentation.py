#!/usr/bin/python3
"""
    A simple Python module to perform customized text printing

    Functions:
    text_indentation: prints a text with 2 new lines after some
                      special characters
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after a ".", "?" and ":"

    Parameters:
        text: the text to custom print

    Return: Nothing
    """

    sepChar = [".", "?", ":"]
    line = ""

    if (type(text) is not str):
        raise TypeError("text must be a string")
    for letter in text:
        if (letter in sepChar):
            line += letter 
            print(line.lstrip(), end="")
            line = ""
            print("\n")
        else:
            line += letter 

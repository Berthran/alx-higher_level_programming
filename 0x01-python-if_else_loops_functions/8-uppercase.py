#!/usr/bin/python3

def uppercase(str_):
    '''Prints a string in upper case'''
    a = ord("a")
    z = ord("z")
    A = ord("A")
    switch_value = a - A

    for char in str_:
        char_val = ord(char)
        if ((char_val >= a) & (char_val <= z)):
            char = chr(char_val - switch_value)
        print("{}".format(char), end="")
    print()

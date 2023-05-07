#!/usr/bin/python3

def islower(c):
    '''Checks for lowercase character'''
    c_value = ord(c)
    a_value = ord('a')
    z_value = ord('z')

    if (c_value >= a_value) & (c_value <= z_value):
        return (True)
    else:
        return (False)

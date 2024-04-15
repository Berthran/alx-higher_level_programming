#!/usr/bin/python3
'''Module to show a list of available attributes and methods of an object

Functions:
    lookup: returns the list of available attributes and methods of an object
'''


def lookup(obj):
    '''Returns the list of available attributes and methods of an object

    Parameters:
        obj: the object to lookup
    '''
    return (dir(obj))

#!/usr/bin/python3
'''
A simple demonstration of the use of `isinstance` function

Functions:
    is_same_class: returns true if an object is an instance
    of a specified object
'''


def is_same_class(obj, a_class):
    '''
    returns true if an object is an instance of a specified object

    Parameters:
        obj: the object to check if its an instance
        a_class: the name of the specified object to check obj against
    '''

    if (type(obj).__name__ == a_class.__name__):
        return (True)
    return (False)

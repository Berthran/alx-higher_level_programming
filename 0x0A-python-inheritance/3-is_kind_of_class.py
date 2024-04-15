#!/usr/bin/python3
'''
A module to demonstrate the use of `instance` function to
determine if an object is an instance of a class or its sub-classes

Functions:
    is_kind_of_class: returns true for an instance or subclass of a
    specified class
'''


def is_kind_of_class(obj, a_class):
    '''
    is_kind_of_class: returns true for an instance or subclass of a
    specified class

    Parameters:
        obj: the object to check if its an instance of the speicified object
        a_class: the name of the specified object to check obj against
    '''
    # Obj is an instance of a_class or an instance of a class that inherits
    # directly or indirectly form a_class
    return (isinstance(obj, a_class))

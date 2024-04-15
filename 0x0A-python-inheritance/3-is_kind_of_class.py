#!/usr/bin/python3
'''
A module to demonstrate an instance of a class or a subclass

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
    return (isinstance(obj, a_class))

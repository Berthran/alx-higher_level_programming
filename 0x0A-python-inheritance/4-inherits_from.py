#!/usr/bin/python3
'''An instance object boolean checker III.

Methods:
    inherits_from  : Returns True is condition is met else False
'''


def inherits_from(obj, a_class):
    '''Returns True if "obj" is instance of "a_class"'''
    if (type(obj) is not a_class and isinstance(obj, a_class)):
        return (True)
    return (False)

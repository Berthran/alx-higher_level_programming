#!/usr/bin/python3
'''An instance object boolean checker

Methods:
    is_kind_of_class : Returns True if condition is met else False

'''


def is_kind_of_class(obj, a_class):
    '''Returns True if "obj" is an instance of "a_class"'''
    if (isinstance(obj, a_class)):
        return (True)
    return (False)

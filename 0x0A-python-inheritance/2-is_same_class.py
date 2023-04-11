#!/usr/bin/python3
'''An instance object boolean checker

Methods:
    is_same_class : Returns True if condition is met else False

'''


def is_same_class(obj, a_class):
    '''Returns True if "obj" is exactly an instance of "a_class"'''
    if (type(obj) is a_class):
        return (True)
    return (False)

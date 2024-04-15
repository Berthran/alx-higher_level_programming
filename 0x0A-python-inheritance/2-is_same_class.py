#!/usr/bin/python3
'''
A simple demonstration of the use of `type` function
to find if an object is an exact instance of a class

Functions:
    is_same_class: returns true if an object is an instance
    of a specified object
         return (self.sort
'''


def is_same_class(obj, a_class):
    '''
    returns true if an object is an instance of a specified object

    Parameters:
        obj: the object to check if its an exact instance of a_class
        a_class: the name of the specified object to check obj against
    '''
    # obj is an exact instance of a_class
    # obj is not an instance of a sub_class or a_class
    if (type(obj).__name__ == a_class.__name__):
        return (True)
    return (False)

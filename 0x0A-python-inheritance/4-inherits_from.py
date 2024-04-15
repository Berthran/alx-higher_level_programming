#!/usr/bin/python3
'''
A module to show the use of `type` and `issubclass` functions to find out
if an object is an instance of only the sub_classes of a class

Functions:
    inherits_from: returns True if the object is an instance of a class
    that inherited directly or indirectly fron the specified class
'''


def inherits_from(obj, a_class):
    '''
    returns True if the object is an instance of a class
    that inherited directly or indirectly fron the specified class
    
    Parameters:
        obj: the object to check if its an instance of a subclass of
        the speicified object
        a_class: the name of the parent class the sub-class inhetited from
        to create the instance obj
    '''
    # Obj is not an instance of a_class but an instance of a sub_class
    # of a_class
    if (type(obj).__name__ != a_class.__name__):
        return (issubclass(type(obj), a_class))

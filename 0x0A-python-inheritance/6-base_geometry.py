#!/usr/bin/python3

'''An illustration of class inheritance II

Classes:
    BaseGeometry : representation of basic Geometry

'''


class BaseGeometry:
    '''A class with one method.

    Methods:
        area : raises an Exception
    '''
    def area(self):
        '''Raises an Exception when method is created'''
        raise Exception("area() is not implemented")

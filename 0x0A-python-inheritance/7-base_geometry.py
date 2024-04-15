#!/usr/bin/python3
'''
A module containing a BaseGeometry class that will serve as the parent class
which other classes can inherit.

Classes:
    BaseGeometry: a class that defines basic features of geometric shapes
'''


class BaseGeometry:
    '''
    A class that defines basic features of geometric shapes

    Methods:
        add: raises an exception
        integer_validator: validates a value
    '''

    def area(self):
        '''
        Raises an exception notifying that the add() method has
        not been implemented for the BaseGeomety class
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Validates a vaue

        Parameters:
            name: a string
            value: an integer value
        '''
        if (type(value).__name__ != int.__name__):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))

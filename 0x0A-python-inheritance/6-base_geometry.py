#!/usr/bin/python3
'''
A module containing a BaseGeometyr class that will serve as the
the parent class from which other classes can inherit

Classes:
    BaseGeometry: a class that defines basic features of geometric shapes
'''


class BaseGeometry:
    '''
    A class that defines basic features of geometric shapes

    Methods:
        add: raises an exception
    '''

    def area(self):
        '''
        Raises an exception notifying that the add() method has
        not been implemented for the BaseGeomety class
        '''
        raise Exception("area() is not implemented")

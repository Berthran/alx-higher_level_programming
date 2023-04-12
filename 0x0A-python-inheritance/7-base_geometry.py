#!/usr/bin/python3

'''An illustration of class inheritance III

Classes:
    BaseGeometry : representation of basic Geometry

'''


class BaseGeometry:
    '''A class with one method.

    Methods:
        area : raises an Exception
        integer_validator : validates an integer value
    '''
    def area(self):
        '''Raises an Exception when method is created'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validates that 'value' is an integer

        Exceptions:
            TypeError : if 'value' is not an integer
            ValueError : if 'value' is less than or equal to zero
        '''

        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))

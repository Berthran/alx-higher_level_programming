#!/usr/bin/python3
'''
A module that demonstrates inheritance of a Python builtin type

Classes:
    MyInt: inherits the attribute of the `int` class
'''


class MyInt(int):
    '''
    inherits the attribute of the `int` class
    '''

    def __eq__(self, value):
        '''
        Returns True if self is not equal to value
        '''
        return super().__ne__(value)

    def __ne__(self, value):
        '''
        Returns True if self is equal to value
        '''
        return (super().__eq__(value))

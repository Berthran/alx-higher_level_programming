#!/usr/bin/python3
'''
Module to show how to limit dynamic instance creation in Python
'''


class LockedClass():
    '''
    A simple Class representation of how the __setattr__ function works
    '''

    def __setattr__(self, name, value):
        '''
        A function that handles dynamic setting of instance attributes
        '''
        if (name != "first_name"):
            err_msg = f"'LockedClass' object has no attribute '{name}'"
            raise AttributeError(err_msg)
        super().__setattr__(name, value)

    def __getattribute__(self, name):
        '''
        A function that handles extracting the value of attributes
        '''
        if (name != "first_name"):
            err_msg = f"'LockedClass' object has no attribute '{name}'"
            raise AttributeError(err_msg)
        else:
            super().__getattribute__(name)

#!/usr/bin/python3
'''
A simple demonstration of Inheritance in Python 

Classes:
    MyList: inherits from a list
'''


class MyList(list):
    '''
    A sub-class of Python's in-built list class

    Class methods:
        print_sorted: prints the list in ascending order
    '''

    def print_sorted(self):
        '''
        prints the MyList object in ascending order without
        changing the order of the MyList Object
        '''
        new_list = self.copy()
        new_list.sort()
        print(new_list)

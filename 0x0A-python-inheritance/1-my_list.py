#!/usr/bin/python3
'''Inheritance in OOP.

Classes:
    MyList

Example Usage:
    sorted_list = Mylist()

'''


class MyList(list):
    '''
    A class inheriting from builtin type 'list'.

    Methods:
        print_sorted : prints a list in ascending order
    '''

    def print_sorted(self):
        '''Prints a list in ascending order'''
        list_to_sort = self.copy()
        list_to_sort.sort()
        print(list_to_sort)

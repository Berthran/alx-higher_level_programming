#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    ''' Deletes key in a dictionary '''
    a_dictionary.pop(key, a_dictionary)
    return (a_dictionary)

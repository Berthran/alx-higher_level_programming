#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    ''' Delete keys with specific value in a dictionary '''
    keys_to_del = []
    for key in a_dictionary:
        spec_val = a_dictionary[key]
        if spec_val == value:
            keys_to_del.append(key)
    for key in keys_to_del:
        a_dictionary.pop(key)
    return (a_dictionary)

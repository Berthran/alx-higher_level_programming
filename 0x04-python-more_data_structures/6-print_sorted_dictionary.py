#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    ''' sorts a dictionary by ordered keys '''
    sorted_keys = sorted(a_dictionary)
    sorted_dict = {}
    for key in sorted_keys:
        sorted_dict[key] = a_dictionary.get(key)
    for key, value in sorted_dict.items():
        print("{}: {}".format(key, value))

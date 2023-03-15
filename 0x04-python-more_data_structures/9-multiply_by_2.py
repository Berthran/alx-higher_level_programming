#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    ''' multiply dict values b 2 '''
    new_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return (new_dict)

#!/usr/bin/python3

def best_score(a_dictionary):
    ''' returns the key of the dictionary with the highest value '''
    if a_dictionary is None:
        return (None)
    first_key = list(a_dictionary)[0]
    prev_score = a_dictionary[first_key]
    best_key = ""
    for key, value in a_dictionary.items():
        if value >= prev_score:
            best_key = key
            prev_score = value
    return (best_key)

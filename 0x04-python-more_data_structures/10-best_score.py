#!/usr/bin/python3

def best_score(a_dictionary):
    ''' returns the key of the dictionary with the highest value '''
    if a_dictionary is None:
        return (None)
    first_key = list(a_dictionary)[0]
    prev_score = a_dictionary.get(first_key)
    if prev_score is None:
        return (None)
    best_key = ""
    for key in a_dictionary:
        if a_dictionary.get(key) is None:
            return(None)
        value = a_dictionary.get(key)
        if value >= prev_score:
            best_key = key
            prev_score = value
    return (best_key)

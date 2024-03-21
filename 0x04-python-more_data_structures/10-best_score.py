#!/usr/bin/python3

def best_score(a_dictionary):
    ''' Returns dictionary key with highes value'''
    dic = a_dictionary
    if dic is None:
        return (None)

    keys = list(dic)
    vals = [dic[key] for key in keys if type(dic[key]) is int]
    if (len(vals) == 0):
        return (None)
    vals.sort()
    max_val = vals[-1]

    for key in dic:
        val = dic[key]
        if val == max_val:
            return (key)

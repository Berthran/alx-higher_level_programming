#!/usr/bin/python3

def fill_tups(a_tuple):
    tup_len = len(a_tuple)

    if tup_len == 0:
        return((0, 0))
    elif tup_len == 1:
        return(a_tuple + (0, ))
    else:
        return(a_tuple)

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    tuple_a = fill_tups(tuple_a)
    tuple_b = fill_tups(tuple_b)

    for i in range(2):
        tuple_c += (tuple_a[i] + tuple_b[i], )
    return(tuple_c)


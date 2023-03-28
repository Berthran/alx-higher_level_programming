#!/usr/bin/python3

def safe_print_integer(value):
    ''' prints a formatted integer '''
    try:
        print("{:d}".format(value))
    except ValueError:
        return (False)
    return (True)

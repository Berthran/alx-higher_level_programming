#!/usr/bin/python3

import sys

# 8 11 14

def safe_print_integer_err(value):
    try:
        print("Number: {:d}".format(value))
        return (True)
    except ValueError as vexc:
        print("Exception: ", vexc, file=sys.stderr)
        return (False)
    except TypeError as texc:
        print("Exception: ", texc, file=sys.stderr)
        return (False)

#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError as vexc:
        print("Exception: ", vexc, file=sys.stderr)
    except TypeError as texc:
        print("Exception: ", texc, file=sys.stderr)
    return (False)

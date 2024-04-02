#!/usr/bin/python3

import sys

# 8 11 14 pass
# 6 7 9 10 12 13 fail

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as exc:
        print("Exception: ", exc, file=sys.stderr)
        return (False)

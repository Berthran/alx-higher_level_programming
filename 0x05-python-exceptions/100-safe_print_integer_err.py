#!/usr/bin/python3

import sys
from contextlib import redirect_stdout


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as exc:
        with redirect_stdout(sys.stderr):
            print("Exception: ", exc)
        return (False)

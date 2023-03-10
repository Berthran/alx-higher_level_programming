#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
import os


def main():
    no_argv = len(sys.argv)
    if no_argv != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    op_list = {"+": add(a, b), "-": sub(a, b), "*": mul(a, b), "/": div(a, b)}

    if op in op_list.keys():
        print("{} {} {} = {}".format(a, op, b, op_list[op]))
        sys.exit(0)

    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)


if __name__ == "__main__":
    main()

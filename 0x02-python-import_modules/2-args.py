#!/usr/bin/python3
import sys

def main():
    argv = sys.argv
    no_argv = len(argv) - 1
    i = 1
    if no_argv == 0:
        print("0 arguments.")
    elif no_argv == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(no_argv))
        for i in range(1, no_argv + 1):
            print("{}: {}".format(i, argv[i]))
            i += 1

if __name__ == "__main__":
    main()

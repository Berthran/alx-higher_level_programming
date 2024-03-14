#!/usr/bin/python3
import sys


def main():
    argv = sys.argv
    no_argv = len(sys.argv) - 1

    i = 1
    sum = 0

    if no_argv > 0:
        for i in range(1, no_argv + 1):
            sum += int(argv[i])

    print("{}".format(sum))


if __name__ == "__main__":
    main()

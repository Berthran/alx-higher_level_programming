#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list != None:
        list_range = len(my_list)
        for i in range(1, list_range + 1):
            print("{:d}".format(my_list[-i]))


if __name__ == "__main__":
    print_reversed_list_integer()

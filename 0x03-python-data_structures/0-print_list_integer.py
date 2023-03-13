#!/usr/bin/python3


def print_list_integer(my_list=[]):
    no_elements = len(my_list)
    for i in range(no_elements):
        print("{:d}".format(my_list[i]))
    return (0)


if __name__ == "__main__":
    print_list_integer()

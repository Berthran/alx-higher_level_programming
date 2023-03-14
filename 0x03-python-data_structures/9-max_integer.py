#!/usr/bin/python3


def max_integer(my_list=[]):
    len_of_list = len(my_list)
    max_num = 0

    if len_of_list == 0:
        return(None)

    max_num = my_list[0]
    for i in range(1, len_of_list):
        if max_num < my_list[i]:
            max_num = my_list[i]
    return(max_num)


if __name__ == "__main__":
    max_integer()

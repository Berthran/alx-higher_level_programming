#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_length = len(my_list)
    new_list = []

    for i in range(list_length):
        by_2 = my_list[i] % 2
        if by_2 == 0:
            new_list += [True]
        else:
            new_list += [False]
    return (new_list)


if __name__ == "__main__":
    divisible_by_2()

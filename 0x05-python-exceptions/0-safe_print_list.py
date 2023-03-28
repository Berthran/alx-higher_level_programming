#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    ''' prints x elements of a list '''
    int_counter = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (IndexError, ValueError):
            continue
        int_counter += 1
    print()
    return (int_counter)

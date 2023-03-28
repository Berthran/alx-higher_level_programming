#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ''' Prints the first x elements of a list,
    printing only integers '''
    num_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except ValueError:
            continue
        num_printed += 1
    print()
    return (num_printed)

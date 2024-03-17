#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    list_idx_range = len(my_list) - 1

    if idx < 0 or idx > list_idx_range:
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)


if __name__ == "__main__":
    replace_in_list()

#!/usr/bin/python3


def element_at(my_list, idx):
    list_idx_range = len(my_list) - 1
    if idx < 0:
        return(None)
    if idx > list_idx_range:
        return(None)
    return(my_list[idx])


if __name__ == "__main__":
    element_at()

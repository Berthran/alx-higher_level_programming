#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    list_idx_range = len(my_list) - 1
    new_list = []

    if idx < 0 or idx > list_idx_range:
        return (my_list)
    else:
        my_list[:] = my_list[:idx] + my_list[idx + 1:]
    return (my_list)


if __name__ == "__main__":
    delete_at()

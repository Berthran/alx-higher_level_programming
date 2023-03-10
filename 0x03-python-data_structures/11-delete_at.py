#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    list_idx_range = len(my_list) - 1
    new_list = []

    if idx < 0 or idx > list_idx_range:
        return(my_list)
    else:
        for i in range(list_idx_range + 1):
            if i != idx:
                my_list[i] = my_list[i]
            else:
                my_list[i] = my_list[i + 1]
    return(my_list)


if __name__ == "__main__":
    delete_at()

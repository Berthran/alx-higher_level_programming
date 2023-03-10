#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_idx_range = len(my_list) - 1
    new_list = []

    if idx < 0 or idx > list_idx_range:
        return(my_list)
    else:
        for i in range(list_idx_range + 1):
            if i == idx:
                new_list = new_list + [element]
            else:
                new_list = new_list + [my_list[i]]
    return(new_list)


if __name__ == "__main__":
    new_in_list()

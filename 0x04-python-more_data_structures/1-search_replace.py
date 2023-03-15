#!/usr/bin/python3

def search_replace(my_list, search, replace):
    ''' Replaces all occurences of an element
    by another element in a new list '''
    new_list = []
    for ele in my_list:
        if ele == search:
            new_list.append(replace)
        else:
            new_list.append(ele)
    return (new_list)

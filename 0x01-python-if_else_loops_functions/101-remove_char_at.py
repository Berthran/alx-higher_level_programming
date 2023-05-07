#!/usr/bin/python3

def remove_char_at(str_, n):
    '''Creates copy of str_ and removes the char at position n'''
    new_str = ""
    for i, char in enumerate(str_):
        if (i != n):
            new_str += char
    return (new_str)

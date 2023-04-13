#!/usr/bin/python3
'''Append to file.
'''


def append_write(filename="", text=""):
    '''Writes 'text' to file "filename at the end position"'''
    with open(filename, "a", encoding="utf-8") as f:
        char_appended = f.write(text)
    return (char_appended)

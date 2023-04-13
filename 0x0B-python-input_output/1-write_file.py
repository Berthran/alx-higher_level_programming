#!/usr/bin/python3
'''Write file.
'''


def write_file(filename="", text=""):
    '''Writes to file "filename"'''
    with open(filename, "w", encoding="utf-8") as f:
        char_written = f.write(text)
    return (char_written)

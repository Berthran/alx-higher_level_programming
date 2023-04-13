#!/usr/bin/python3
'''Read file.
'''


def read_file(filename=""):
    '''Reads file "filename and prints the content"'''
    with open(filename, "r") as f:
        file_contents = f.read()
    print(file_contents)

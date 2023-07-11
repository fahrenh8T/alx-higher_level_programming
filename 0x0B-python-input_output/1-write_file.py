#!/usr/bin/python3
'''module: 1-write_file
    function that writes a string to a text file
    (UTF8) and returns the number of characters written
'''


def write_file(filename="", text=""):
    '''function: write_file
        write a string to a text file
    '''
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

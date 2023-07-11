#!/usr/bin/python3
'''module: 2-append_write
    defines a file-appending function.
'''


def append_write(filename="", text=""):
    '''function: append_write
        appends a string to the end of a UTF8 text file.
        Args:
            filename (str): The name of the file to append to.
            text (str): The string to append to the file.
    '''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

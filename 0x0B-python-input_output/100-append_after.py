#!/usr/bin/python3
'''module: 100-append_after
    defines a text file insertion function
'''


def append_after(filename="", search_string="", new_string=""):
    '''function: append_after
        Inserts text after each line containing a given string in a file

        Args:
            filename (str): name of the file to modify
            search_string (str): string to search for each line
            new_string (str): string to insert after
                each line containing the search_string
    '''
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)

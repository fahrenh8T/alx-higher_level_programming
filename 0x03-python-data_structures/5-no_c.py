#!/usr/bin/python3
def no_c(my_string):
    cp = []
    for c in my_string:
        if c != 'c' and c != 'C':
            cp.append(c)
    return ("".join(cp))

#!/usr/bin/python3
'''module: 101-lazy_matrix_mul
finds the max integer in a list
'''


def max_integer(list=[]):
    '''function: max_integer
    finds and return the max integer in a list of integers
    If the list is empty, the function returns None
    '''
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

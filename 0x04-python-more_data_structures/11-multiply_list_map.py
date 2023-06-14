#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    '''function returns a list with all values multiplied by a number'''
    return list(map(lambda dict: dict * number, my_list))

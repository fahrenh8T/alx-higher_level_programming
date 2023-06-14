#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    ''' function returns a set of all elements present in only one set'''
    symmetric_diff = set_1 ^ set_2
    return (symmetric_diff)

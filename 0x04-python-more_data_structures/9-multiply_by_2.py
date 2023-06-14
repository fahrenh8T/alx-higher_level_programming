#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''function returns a new dictionary with all values multiplied by 2'''
    dict = a_dictionary.copy()
    for tempo in dict.keys():
        dict[tempo] *= 2
    return (dict)

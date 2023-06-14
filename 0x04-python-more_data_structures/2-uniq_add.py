#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''function adds all unique integers in a list (once for each)'''
    num = 0
    for element in set(my_list):
        num += element
    return num

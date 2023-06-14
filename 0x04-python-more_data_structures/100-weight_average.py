#!/usr/bin/python3
def weight_average(my_list=[]):
    '''returns wighted average of all integers tuple'''
    if my_list == [] or my_list is None:
        return (0)
    sum = 0
    size = 0
    for tuple in my_list:
        sum += (tuple[0] * tuple[1])
        size += tuple[1]
    return (sum/size)

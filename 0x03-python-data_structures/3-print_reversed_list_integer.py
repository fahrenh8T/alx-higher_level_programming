#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    if isinstance(my_list, list):
        my_list.reverse()
        for r in my_list:
            print("{:d}".format(r))

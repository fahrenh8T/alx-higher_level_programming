#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda dict: dict * number, my_list))

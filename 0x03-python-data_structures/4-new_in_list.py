#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tmp = my_list[:]
    if idx < 0 or idx > (len(my_list) - 1):
        tmp[idx] = element
        return(tmp)
    return(my_list)

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    indx = 0
    while True:
        try:
            if indx < x:
                print(my_list[indx], end='')
                indx += 1
            else:
                print()
                return (indx)
        except IndexError:
            print()
            return (indx)

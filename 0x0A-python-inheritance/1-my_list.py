#!/usr/bin/python3
'''module: 1-my_list
'''


class MyList(list):
    '''represents a custom list class
        derived from the built-in list class
    '''

    def print_sorted(self):
        '''function: print_sorted
            prints the elements of the list in sorted order
        '''
        print(sorted(self))

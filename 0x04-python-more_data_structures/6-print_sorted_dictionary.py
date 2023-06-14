#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''' function sorts the dictionary in order'''
    for dict in sorted(a_dictionary.keys()):
        print('{}: {}'.format(dict, a_dictionary[dict]))

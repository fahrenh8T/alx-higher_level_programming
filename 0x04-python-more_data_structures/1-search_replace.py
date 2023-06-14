#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ''' function replaces all occurrence of an element
    by another in a new list '''
    def find_search(element):
        if element != search:
            return (element)
        else:
            return (replace)
    return list(map(find_search, my_list))

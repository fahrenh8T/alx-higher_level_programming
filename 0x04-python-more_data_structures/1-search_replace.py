#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def find_search(element):
        if element != search:
            return (element)
        else:
            return (replace)
    return list(map(find_search, my_list))

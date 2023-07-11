#!/usr/bin/python3
''' module: 2-is_same_class
'''


def is_kind_of_class(obj, a_class):
    '''function: is_kind_of_class
    checks if an object is an instance or
    a subclass instance of a given class
    Args:
        obj: object to check
        a_class: class to compare the type of obj to
    '''
    return isinstance(obj, a_class)

#!/usr/bin/python3
'''module: class_checking
defines a class-checking function.
'''


def is_same_class(obj, a_class):
    '''check if an object is exactly an instance of a given class.
    Args:
        obj (any): The object to check
        a_class (type): The class to match the type of obj to
    '''
    if type(obj) == a_class:
        return True
    return False

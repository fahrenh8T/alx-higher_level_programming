#!/usr/bin/python3
''' module: 4-inherits_from
'''


def inherits_from(obj, a_class):
    '''function: inherits_from
    check if an object is an instance of a class that inherited
    (directly or indirectly) from a given class
    obj: object to check
    a_class: class to compare the type of obj to
    '''
    return type(obj) != a_class and isinstance(obj, a_class)

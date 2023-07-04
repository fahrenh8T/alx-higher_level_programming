#!/usr/bin/python3
'''defines a locked class
'''


class LockedClass:
    '''method: LockedClass
    only allows instantiation of an attribute called first_name
    '''
    __slots__ = ["first_name"]

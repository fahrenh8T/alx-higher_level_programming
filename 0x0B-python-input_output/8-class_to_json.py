#!/usr/bin/python3
'''module: 8-class_to_json
    defines a python class-to-JSON function
'''


def class_to_json(obj):
    '''function: class_to _json
        converts a Python object to a JSON compatible dictionary
        Args:
            obj (object): object to convert
    '''
    return obj.__dict__

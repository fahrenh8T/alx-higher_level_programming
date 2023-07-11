#!/usr/bin/python3
'''module: 101-add_attribute
'''


def add_attribute(obj, att, value):
    '''function: add_attribute
        add a new attribute to an object if possible
        Args:
            obj (object): The object to add an attribute to
            att (str): The name of the attribute to add
            value (any): The value of the attribute

        Raises:
            TypeError: If the attribute cannot be added to the object
    '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("Cannot add new attribute")
    setattr(obj, att, value)

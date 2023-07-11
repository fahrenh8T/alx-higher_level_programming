#!/usr/bin/python3
'''module: 101-add_attribute
'''


def add_attribute(objt, attri, value):
    '''function: add_attribute
        add a new attribute to an object if possible
        Args:
            obj (object): The object to add an attribute to
            att (str): The name of the attribute to add
            value (any): The value of the attribute

        Raises:
            TypeError: If the attribute cannot be added to the object
    '''
    if not hasattr(objt, "__dict__"):
        raise TypeError("Cannot add new attribute")
    if (not hasattr(objt, attri)):
        objt.__setattr__(attri, value)

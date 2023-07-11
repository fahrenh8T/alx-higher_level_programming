#!/usr/bin/python3
'''module: 7-base_geometry
    defines a base geometry class BaseGeometry
    with area calculation and integer validation methods.
'''


class BaseGeometry:
    '''class: BaseGeometry
        representing geometric entities
    '''

    def area(self):
        '''function: area
            calculate the area of the geometric entity
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''function: ineteger_validator
        validate a parameter as an integer
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

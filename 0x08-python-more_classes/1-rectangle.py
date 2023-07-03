#!/usr/bin/python3
'''A Rectangle class'''


class Rectangle:
    '''class: represent a rectangle'''
    def __init__(self, width=0, height=0):
        '''method: __init__
        initialize a new Rectangle.
            height (int): The height of the new rectangle
            width (int): The width of the new rectangle
        '''
        self.height = height
        self.width = width

    @property
    def height(self):
        '''method: get/set the height of the rectangle
            returns: (int)height of rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''method: set the height of the rectangle.
        Args:
            value (int): The height value to set.'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        '''method: get/set the width of the rectangle
            int: width of rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''method: set the width of the rectangle.
        Args:
            value (int): The width value to set.'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

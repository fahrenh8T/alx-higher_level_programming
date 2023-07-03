#!/usr/bin/python3
'''module: Defines a Rectangle class.'''


class Rectangle:
    '''class: represents a rectangle.'''

    def __init__(self, width=0, height=0):
        '''method: initialize a new Rectangle instance.
                width (int): The width of the new rectangle.
                height (int): The height of the new rectangle.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''method: get or set the width of the Rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''method: get the width of the Rectangle.
                value (int): The width value to set.
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''method: get or set the height of the Rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''method: get the height of the Rectangle.
                value (int): The height value to set.
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''method: calculate and return the area of the Rectangle.'''
        return self.__width * self.__height

    def perimeter(self):
        '''method: calculate and return the perimeter of the Rectangle.'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        '''return the printable representation of the Rectangle.
        represents the rectangle with the # character.
        Returns:
            str: The printable representation of the Rectangle.
        '''
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

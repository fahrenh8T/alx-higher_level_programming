#!/usr/bin/python3
'''module: 9-rectangle
    contains the definition of a Rectangle class
    derived from the BaseGeometry class
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class: Rectangle
        represents a rectangle object
    '''
    def __init__(self, width, height):
        '''function: __init__
            Initialize a Rectangle instance.

            Args:
                width (int): The width of the rectangle.
                height (int): The height of the rectangle.
        '''
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        '''function: area
            calculate the area of the rectangle
        '''
        return self.__width * self.__height

    def __str__(self):
        '''function: __str__
            return a string representation of the rectangle
        '''
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))

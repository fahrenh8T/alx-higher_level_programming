#!/usr/bin/python3
'''module: 8-rectangle
    implementing a Rectangle class derived
    from the BaseGeometry class
'''


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''class: Rectangle
        represents a rectangle object
    '''
    def __init__(self, width, height):
        '''function: __init__
            initialize a Rectangle instance
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

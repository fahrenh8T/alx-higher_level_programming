#!/usr/bin/python3
'''module: 7-rectangle
This module contains the Rectangle class ...
'''


class Rectangle:
    '''class: Rectangle
    represent a rectangle.
    attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (#): The symbol used for string representation.
    '''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''method: __init__
        initialize a new Rectangle.
        args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        '''
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        '''method: width
        get/set the width of the Rectangle.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''method: height
        get/set the height of the Rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''method: area
        return the area
        '''
        return (self.__width * self.__height)

    def perimeter(self):
        '''method: perimeter
        return the perimeter
        '''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''method: bigger_or_equal
        return the Rectangle with the greater area.
        args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
      '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        '''method: __str__
        return the printable representation of the Rectangle.
        represents the rectangle with the # character.
        '''
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        '''method: __repr__
        return the string representation
        '''
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"

    def __del__(self):
        '''method: __del__
        print a message for every deletion
        '''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

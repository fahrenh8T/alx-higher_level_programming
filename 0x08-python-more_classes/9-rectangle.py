#!/usr/bin/python3
'''module: 9-rectangle
module contains class Rectangle
'''


class Rectangle:
    '''class: Rectangle
    attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (#): The symbol used for string representation.
    '''

    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size):
        '''class method: square
        creates a square
        '''
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''static method: bigger_or_equal
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return True
        else:
            return False

    def __init__(self, width=0, height=0):
        '''method: __init__
        initializes an instance
        '''
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''method: width
        get the width of the Rectangle
        '''
        if ((not isinstance(self.__width, int))
                or isinstance(self.__width, bool)):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @width.setter
    def width(self, width):
        '''method: width
        sets the width of the Rectangle
        '''
        if (not isinstance(self.__width, int)
                or isinstance(self.__width, bool)):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("with must be >= 0")
        self.__width = width

    @property
    def height(self):
        '''method: height
        gets the height
        '''
        if ((not isinstance(self.__height, int))
                or isinstance(self.__height, bool)):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    @height.setter
    def height(self, height):
        '''method: height
        sets the height
        '''
        if (not isinstance(self.__height, int)
                or isinstance(self.__height, bool)):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        '''method: area
        returns area of rectangle
        '''
        return self.__height * self.__width

    def perimeter(self):
        '''method: perimeter
        returns perimeter
        '''
        if self.__height == 0 or self.width == 0:
            return 0
        return ((self.__height + self.width) * 2)

    def __str__(self):
        '''method: __str__
        returns nice string representation of the rectangle
        '''
        rect_str = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for idx in range(self.__height):
            rect_str += str(self.print_symbol) * self.width
            if idx + 1 < self.__height:
                rect_str += '\n'
        return rect_str

    def __repr__(self):
        '''method: __repr__
        return a representation of rectangle
        that can be used by eval() to create new object
        '''
        rect_str = "Rectangle(" + str(self.__width) + ","
        rect_str += str(self.__height) + ")"
        return rect_str

    def __del__(self):
        '''method: __del__
        deletes instance of class and prints
        '''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

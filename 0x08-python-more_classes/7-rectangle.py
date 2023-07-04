#!/usr/bin/python3
'''module: 7-rectangle
contains the Rectangle class
'''


class Rectangle:
    '''class: Rectangle
    an empty class, further additions will be made in subsequent assignments.
    '''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''method: __init__
        initialize an instance of the Rectangle class.
        '''
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''method: width getter
        '''
        if ((not isinstance(self.__width, int))
                or isinstance(self.__width, bool)):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @width.setter
    def width(self, width):
        '''method: width setter
        '''
        if (not isinstance(self.__width, int)
                or isinstance(self.__width, bool)):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        '''method: height getter
        '''
        if ((not isinstance(self.__height, int))
                or isinstance(self.__height, bool)):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    @height.setter
    def height(self, height):
        '''method: height setter
        '''
        if (not isinstance(self.__height, int)
                or isinstance(self.__height, bool)):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        '''method: area
        Return the area of the rectangle.
        '''
        return self.__height * self.__width

    def perimeter(self):
        '''method: perimeter
        Return the perimeter of the rectangle.
        '''
        if self.__height == 0 or self.width == 0:
            return 0
        return (self.__height + self.width) * 2

    def __str__(self):
        '''method: __str__
        Return a nice string representation of the rectangle.
        '''
        ret_str = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for idx in range(self.__height):
            ret_str += str(self.print_symbol) * self.width
            if idx + 1 < self.__height:
                ret_str += '\n'
        return ret_str

    def __repr__(self):
        '''method: __repr__
        Return a representation of the rectangle
        that can be used by eval() to create a new object.
        '''
        ret_str = "Rectangle(" + str(self.__width) + ","
        ret_str += str(self.__height) + ")"
        return ret_str

    def __del__(self):
        '''method: __del__
        Delete an instance of the Rectangle class and print "bye" message.
        '''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

#!/usr/bin/python3
'''module: rectangle
'''
from models.base import Base


class Rectangle(Base):
    '''class:Rectangle
        representing a Rectangle
        Inherits from:
            Base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''function: __init__
            Initializes an instance of the Rectangle class.
            Args:
                - width (int): Width of the rectangle.
                - height (int): Height of the rectangle
                - x (int): x-coordinate of the rectangle
                - y (int): y-coordinate of the rectangle
                - id (int): ID of the rectangle
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''
            getter method for the width attribute
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            setter method for the width attribute
        '''
        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        '''
            getter method for the height attribute
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            setter method for the height attribute
        '''
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        '''
            getter method for the x attribute
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
            setter method for the x attribute
        '''
        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        '''
            getter method for the y attribute
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
            setter method for the y attribute
        '''
        self.setter_validation("y", value)
        self.__y = value

    def area(self):
        '''
            calculates and returns the area of the rectangle
        '''
        return (self.height * self.width)

    def display(self):
        '''
            prints the rectangle representation to stdout
        '''
        rectangle = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")

    def update(self, *args, **kwargs):
        '''
            Updates the attributes of the rectangle
            Args:
                - args: Variable length argument list
                - kwargs: Arbitrary keyword arguments
        '''
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        '''
            returns a dictionary representation of the rectangle
        '''
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}

    @staticmethod
    def setter_validation(attribute, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def __str__(self):
        '''
            returns a string representation of the rectangle
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

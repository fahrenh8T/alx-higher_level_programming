#!/usr/bin/python3
'''module: square
    define Rectangle Class
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''class: Square
        represents a Square
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        Initializes a Square instance
        Args:
            - size (int): Size of the square.
            - x (int): x-coordinate of the square.
            - y (int): y-coordinate of the square.
            - id (int): ID of the square.
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''
        getter method for the size attribute.
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        setter method for the size attribute.
        '''
        self.width = value
        self.height = value

    def __str__(self):
        '''
        returns a string representation of the square.
        '''
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        '''
        Updates the attributes of the square
        Args:
            - args: Variable length argument list
            - kwargs: Arbitrary keyword arguments
        '''

        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''
        returns a dictionary representation of the square.
        '''
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

#!/usr/bin/python3
'''Module: square
    contains the definition of a Square class derived from the Rectangle class.
'''


Rectangle = __import__('9-rectangle').Rectangle
'''square class
'''


class Square(Rectangle):
    '''class: Square
        represents a square object
    '''

    def __init__(self, size):
        '''function: __init__
        initialize a Square instance.
        Args:
            size (int): The size of the square.
        '''
        self.__size = size
        super().__init__(self.__size, self.__size)
        self.integer_validator("size", size)

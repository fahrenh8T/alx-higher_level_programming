#!/usr/bin/python3
'''module: square
    contains the definition of a
    Square class derived from the Rectangle class
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class: Square
        represents a square object.
    '''

    def __init__(self, size):
        '''function: __init__
            initialize a Square instance.
            Args:
        size (int): The size of the square.
        '''
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        '''function: __str__
            return a string representation of the square.
        '''
        return "[Square] {}/{}".format(self.__size, self.__size)

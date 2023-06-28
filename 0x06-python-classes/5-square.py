#!/usr/bin/python3
'''define a class square'''


class Square:
    '''represent a square'''
    def __init__(self, size):
        '''initialize the size of the square
        size: is the size of the square'''
        self.size = size

    @property
    def size(self):
        '''set current size of the square'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''return the current area of the square'''
        return (self.__size * self.__size)

    def my_print(self):
        '''prints square with # character'''
        for r in range(0, self.__size):
            for w in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")

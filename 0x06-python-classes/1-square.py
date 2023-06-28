#!/usr/bin/python3
'''defines a class square'''


class Square:
    '''represent a square'''
    def __init__(self, size=None):
        '''initializing this square class
        Args:
            size (int): represents the size of the square defined
        '''
        self.__size = size

#!/usr/bin/python3
'''module: 4-print_square
contain a function that prints a square
'''


def print_square(size):
    '''function: print_square
    function prints a square with the character #
    Args:
        size (int): represents the length of the square
    '''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for row in range(0, size):
        for col in range(size):
            print("#", end="")
        print("")

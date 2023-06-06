#!/usr/bin/python3
def uppercase(str):
    for char in str:
        ascii_val = ord(char)
        if 97 <= ascii_val <= 122:
            uppercase_char = chr(ascii_val - 32)
            print(uppercase_char, end='')
        else:
            print(char, end='')
    print()

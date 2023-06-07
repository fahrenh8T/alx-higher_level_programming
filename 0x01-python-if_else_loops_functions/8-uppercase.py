#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <=122:
            uppercase_char = chr(ord(char) -32)
            result += "{}".format(uppercase_char)
        else:
            result += "{}".format(char)
    print("{}".format(result))

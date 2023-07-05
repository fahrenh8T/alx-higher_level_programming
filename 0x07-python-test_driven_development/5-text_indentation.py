#!/usr/bin/python3
'''module: 5-text_indentation
contains a function that indents texts
'''


def text_indentation(text):
    '''function: text_indentation
    function prints a text with 2 new lines after each ".", "?", or ":"
    Args:
        text (str): The string to be printed
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indx = 0
    while indx < len(text) and text[indx] == " ":
        indx = indx + 1

    while indx < len(text):
        print(text[indx], end="")
        if text[indx] == "\n" or text[indx] in ".?:":
            if text[indx] in ".?:":
                print("\n")
            indx = indx + 1
            while indx < len(text) and text[indx] == " ":
                indx += 1
            continue
        indx += 1

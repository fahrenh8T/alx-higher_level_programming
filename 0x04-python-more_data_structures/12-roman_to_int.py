#!/usr/bin/python3
def roman_to_int(roman_string):
    '''convers Roman numeral to integer'''
    if not roman_string or type(roman_string) != str:
        return 0
    dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    num = 0
    for i in range(len(roman_string)):
        if i > 0 and dict[roman_string[i]] > dict[roman_string[i - 1]]:
            num += dict[roman_string[i]] - 2 * \
                        dict[roman_string[i - 1]]
        else:
            num += dict[roman_string[i]]
    return num

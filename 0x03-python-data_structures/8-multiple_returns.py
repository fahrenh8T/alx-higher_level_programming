#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_c = sentence[0] if length > 0 else "None"
    t_len = length, first_c
    return(t_len)

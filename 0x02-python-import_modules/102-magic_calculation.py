#!/usr/bin/python3
"""match bytecode provided"""
def magic_calculation(a, b):
    from magic_calculation_102 import add , sub
    if a < b:
        rslt = add(a, b)
        for i in range(4, 6):
            rslt = add(rslt, i)
        return (rslt)
    else:
        return (sub(a, b))

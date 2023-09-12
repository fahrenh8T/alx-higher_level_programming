#!/usr/bin/python3
"""prints the sum of 1 and 2 """
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    rslt = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, rslt))

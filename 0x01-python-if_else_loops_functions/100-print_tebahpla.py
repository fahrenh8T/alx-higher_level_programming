#!/usr/bin/python3
for n in range(0, 26):
    r = ord('z') -n
    if (n % 2 == 1):
        r = chr(r - ord('a') + ord('A'))
    else:
        r = chr(r)
    print("{}".format(r), end='')

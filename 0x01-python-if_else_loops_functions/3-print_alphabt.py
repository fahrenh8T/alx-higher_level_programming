#!/usr/bin/python3
for ascii_val in range(97, 123):
    if chr(ascii_val) not in ['q', 'e']:
        print('{}'.format(chr(ascii_val)), end='')

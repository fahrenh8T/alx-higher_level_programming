#!/usr/bin/python3
""" script fetches https://alx-intranet.hbtn.io/status

    usage: ./0-hbtn_status.py | cat -e
"""
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        shape = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(shape)))
        print("\t- content: {}".format(shape))
        print("\t- utf8 content: {}".format(shape.decode('utf-8')))

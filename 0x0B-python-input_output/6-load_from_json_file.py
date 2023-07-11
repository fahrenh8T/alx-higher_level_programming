#!/usr/bin/python3
'''module: 6-load_from_json_file
    defines a JSON file-reading function
'''
import json


def load_from_json_file(filename):
    '''function: load_from_json_file
        creates a Python object from a given JSON file
    '''
    with open(filename) as fl:
        return json.load(fl)

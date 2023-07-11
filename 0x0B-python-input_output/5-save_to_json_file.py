#!/usr/bin/python3
'''module: 5-save_to_json_file
    writes an object to a txt file, using JSON  representation
'''

import json


def save_to_json_file(my_obj, filename):
    '''function: save_to_json_file
        accepts object and sends JSON repsenatation to file
    '''
    with open(filename, 'w') as seen:
        json.dump(my_obj, seen)

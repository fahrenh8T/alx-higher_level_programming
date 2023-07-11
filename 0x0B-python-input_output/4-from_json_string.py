#!/usr/bin/python3
'''module: 4-from_json_string
    function that returns an object
    (Python data structure) represented by a JSON string
'''

import json


def from_json_string(my_str):
    '''function: from_json_string
        module from_json_string
    '''
    return json.loads(my_str)

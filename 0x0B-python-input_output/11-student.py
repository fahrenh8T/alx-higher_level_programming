#!/usr/bin/python3
'''module: 11-student
    defines a class Student
'''


class Student:
    '''class: Student
        Represent a student.
    '''

    def __init__(self, first_name, last_name, age):
        '''function: __init__
            Initializes a new Student
            Args:
                first_name (str): The first name of the student.
                last_name (str): The last name of the student.
                age (int): The age of the student.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''function: to_json
            Gets a dictionary representation of the Student.
            If attrs is a list of strings, represents only those attributes
            included in the list
            Args:
                attrs (list): List of attribute names (strings)
                to include in the dictionary representation.
        '''
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        '''function: reload_from_json
            Replaces all attributes of the Student
            Args:
                json (dict): diictionary containing the new attribute values
        '''
        for k, v in json.items():
            setattr(self, k, v)

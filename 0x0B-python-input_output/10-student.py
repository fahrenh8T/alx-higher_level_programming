#!/usr/bin/python3
'''module: 10-student
    defines a class Student
'''


class Student:
    '''class: Student
        Represent a student.
    '''
    def __init__(self, first_name, last_name, age):
        '''function: __init__
            initializes a new student
            Args:
                first_name (str): The first name of the student
                last_name (str): The last name of the student
                age (int): The age of the student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''function: to_json
            Get a dictionary representation of the Student.
            If attrs is a list of strings, represents only those attributes
            included in the list.

            Args:
                attrs (list): List of attribute names (strings)
                to include in the dictionary representation.
        '''
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

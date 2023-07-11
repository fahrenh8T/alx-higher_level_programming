#!/usr/bin/python3
'''module: 9-student
    defines a class Student
'''

class Student:
    '''class: Student
        represent a student
    '''
    def __init__(self, first_name, last_name, age):
        '''function: __init__
            initializes a new student
            Args:
                first_name (str): first name of the student
                last_name (str): last name of the student
                age (int): age of the student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''function: to_json
            gets a dictionary representation of the Student
        '''
        return self.__dict__

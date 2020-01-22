#!/usr/bin/python3
'''
Class Student that defines a student
'''


class Student:
    '''Description of a student'''

    def __init__(self, first_name, last_name, age):
        '''Student contructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Dictionary representation of a student'''
        return self.__dict__

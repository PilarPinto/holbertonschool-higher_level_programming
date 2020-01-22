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

    def to_json(self, attrs=None):
        '''Dictionary representation of a student'''
        if type(attrs) is list:
            for ele in attrs:
                if type(ele) is str:
                    return {
                        x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

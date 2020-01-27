#!/usr/bin/python3
'''
class will be the “base” of all other classes
'''
import json


class Base:
'''
Clase Base
'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = '{}.json'.format(cls.__name__)
        if list_objs is None:
            return '[]'
        else:
            with open(filename, 'w') as f:
                f.write(cls.to_json_string(
                    [cls.to_dictionary(x) for x in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return '[]'
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        inst = cls(1, 1)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        filename = '{}.json'.format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                lst = cls.from_json_string(f.read())
                return [cls.create(**ind) for ind in lst]
        except IOError:
            return []
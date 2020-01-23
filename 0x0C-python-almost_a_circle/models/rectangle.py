#!/usr/bin/python3
'''
class Rectangle that inherits from Base
'''

from models.base import Base


class Rectangle(Base):
    '''Class rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @width.setter
    def height(self, value):
        self.__height = value

#!/usr/bin/python3
'''
class Rectangle that inherits from Base
'''

from models.base import Base


class Rectangle(Base):
    '''Class rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, valuew):
        if not isinstance(valuew, int):
            raise TypeError('width must be an integer')
        elif valuew <= 0:
            raise ValueError('width must be > 0')
        self.__width = valuew

    @property
    def height(self):
        return self.__height

    @width.setter
    def height(self, valueh):
        if not isinstance(valueh, int):
            raise TypeError('height must be an integer')
        elif valueh <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = valueh

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        if self.__width == 0 or self.__height == 0:
            print()
        else:
            if self.__y != 0:
                for row in range(self.__y):
                    print('\n', end='')
            for row in range(self.__height):
                print('{}{}'.format(' '*self.__x, '#'*self.__width))

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.__x, self.__y, self.__width, self.__height)

#!/usr/bin/python3
'''
class Rectangle that inherits from Base
'''

from models.base import Base


class Rectangle(Base):
    '''Class rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        '''String print function'''
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    @property
    def width(self):
        '''Set of width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter of width'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''getter of height'''
        return self.__height

    @width.setter
    def height(self, value):
        '''setter of height'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''getter of x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter of x'''
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''getter of y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter of y'''
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''Area function'''
        return self.__width * self.__height

    def display(self):
        '''Display hastags function'''
        if self.__y != 0:
            for row in range(self.__y):
                print('\n', end='')
        for row in range(self.__height):
            print('{}{}'.format(' '*self.__x, '#'*self.__width))

    def update(self, *args, **kwargs):
        '''Args function'''
        lst = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) is not 0:
            for i in range(len(args)):
                setattr(self, lst[i], args[i])
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        '''Dictionary function'''
        dic_a = {'id': self.id, 'x': self.__x, 'y': self.__y,
                 'height': self.__height, 'width': self.__width}
        return dic_a

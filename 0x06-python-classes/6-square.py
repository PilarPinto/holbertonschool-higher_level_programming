#!/usr/bin/python3
class Square:
    """
    Class to find an square area
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        This is the constructor
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        if not isinstance(position, tuple):
            if not position[0] >= 0 and position[1] >= 0:
                raise TypeError('position must be a tuple\
                of 2 positive integers')
        self.__position = position



    @property
    def size(self):
        """
        Action to obtain the atribute value
        """
        return(self.__size)

    @property
    def position(self):
        """
        Obtain the atribute position value
        """
        return(self.__position)

    @size.setter
    def size(self, value):
        """
        Put the value and handle the errors
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """
        Put the value and handle the errors
        """
        if not isinstance(value, tuple):
            if not value[0] >= 0 and value[1] >= 0:
                raise TypeError('position must be a tuple\
                of 2 positive integers')
            else:
                self.__position = position


    def area(self):
        """
        Function to find a square area
        """
        return(self.__size**2)


    def my_print(self):
        """
        Function to print an square
        """
        if self.size == 0:
            print()
        for x in range(self.size):
            print(' '*self.position[0], end='')
            print('#'*self.size)

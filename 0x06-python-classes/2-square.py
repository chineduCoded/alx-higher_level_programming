#!/usr/bin/python3
''' Define a class Square '''

class Square:
    ''' Represent a Square '''

    def __init__(self, size=0):
        '''
            Initializes the class instance

        @self:
            A parameter used to refer to the class instance

        @size:
            The size of the square, must be +ve integer
        '''
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

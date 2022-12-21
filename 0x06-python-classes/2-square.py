#!/usr/bin/python3
"""A Module that create a Square object"""

class Square:
    """Creates an Object template"""

    def __init__(self, size=0):
        '''Initializes the class instance
        @self:
            a parameter used to refer to the class instance
        @size:
            The size of square, must be +ve integer
        '''
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

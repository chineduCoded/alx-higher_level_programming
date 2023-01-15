#!/usr/bin/python3
"""Defines Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherit from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        args:
            width(int): the width of the rectangle
            height(int): the height of the rectangle
            x(int): x-coordinate of the rectangle
            y(int): y-coordinate of the rectangle
            id(int): id assigned to each object
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter that returns the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width
        args:
            value(int): the new width of the rectangle
        raises:
            TypeError: if the value is not integer
            ValueError: if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter that returns the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height
        args:
            value(int): the new height of rectangle
        raises:
            TypeError: if the value is not integer
            ValueError: if value <= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x
        returns:
            the x-cooordinate of rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x
        args:
            value(int): the new value of x coordinate of rectangle
        raises:
            TypeError: if value is not integer
            ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("x must an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for y
        return:
            the y coordinate of rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y
        args:
            value(int): the new value of y coordinate of rectangle
        raises:
            TypeError: if value is not integer
            valueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of rectangle
        Return:
            the area of rectangle
        """
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with th character #"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns the string representattion of Rectangle instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

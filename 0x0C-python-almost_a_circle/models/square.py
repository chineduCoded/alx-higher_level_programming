#!/usr/bin/python3
""" Defines Square Class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """represents a square, inherits from Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        attrs:
            size(int): size of the square
            x(int): x-coordinate of the square
            y(int): y-coordinate of the square
            id(int): id for the object, assigned automatically
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

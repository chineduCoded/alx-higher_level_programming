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

    @property
    def size(self):
        """Getter for size that returns the size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """
        args:
            value(int): the new value of square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        attrs:
            args: tuple of positional arguments
            kwargs: dictionary of keyworded arguments
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns Square instance to dictionary representation"""
        return {name: getattr(self, name) for name in ["id", "size", "x", "y"]}

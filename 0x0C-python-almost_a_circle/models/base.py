#!/usr/bin/python3
""" Defines Base Class """


class Base:
    """
    Base class for managing id attribute and counting objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        args:
            id(int): id to be assigned to the object
        """
        if id is not None:
            # Assign the given id to the object
            self.id = id
        else:
            # Increment the object count and assign the new value as the id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

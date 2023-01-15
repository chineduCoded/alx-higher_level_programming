#!/usr/bin/python3
""" Defines Base Class """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        args:
            list_dictionaries: list of dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        param:
            list_objs: list of instances who inherits of Base
        """
        if list_objs is None:
            list_objs = []
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dictionaries)
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(json_string)

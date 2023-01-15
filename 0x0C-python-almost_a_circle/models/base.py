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
        :return: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        :param json_string: a string representing a list of dictionaries
        :return: list represented by json_string
        """
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

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

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        :param dictionary: key/value arguments to set the attributes of the instance.
        :return: an instance of the class with the attributes set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        :return: list of instances
        """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                json_string = f.read()
        except:
            return []
        list_dictionaries = cls.from_json_string(json_string)
        return [cls.create(**dic) for dic in list_dictionaries]

#!/usr/bin/python3
import json 

class Base:
    """Base class for object management."""

    __nb_objects = 0  # Class variable to keep track of the number of objects created

    def __init__(self, id=None):
        """Initialize a Base object."""
        if id is not None:
            self.id = id  # Set the id if provided
        else:
            Base.__nb_objects += 1  # Increment the count of objects
            self.id = Base.__nb_objects  # Set the id based on the count of objects 
    @staticmethod 
    def to_json_string(list_dictionaries): 
        if list_dictionaries is None or  len(list_dictionaries) == 0: 
            return "[]" 
        else: 
            return json.dumps(list_dictionaries)
    @classmethod 
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        with open(filename, 'w') as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))


    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a dummy instance with arbitrary width and height
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a dummy instance with arbitrary size
        else:
            raise TypeError("Unsupported class type")

        dummy_instance.update(**dictionary)  # Update the dummy instance with real values using kwargs
        return dummy_instance
#!/usr/bin/python3
"""Defines a Base class."""

import json
import csv
import turtle


class Base:
    """Base model.

    This class represents the base for all other classes in project 0x0C*.

    Private Class Attributes:
        __number_of_instances (int): Number of instantiated Base instances.
    """

    __number_of_instances = 0

    def __init__(self, identity=None):
        """Initialize a new Base instance.

        Args:
            identity (int): The identity of the new Base instance.
        """
        if identity is not None:
            self.identity = identity
        else:
            Base.__number_of_instances += 1
            self.identity = Base.__number_of_instances

    @staticmethod
    def to_json(data):
        """Return the JSON serialization of a list of dictionaries.

        Args:
            data (list): A list of dictionaries.
        """
        if data is None or data == []:
            return "[]"
        return json.dumps(data)

    @classmethod
    def save_to_file(cls, instances):
        """Write the JSON serialization of a list of instances to a file.

        Args:
            instances (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if instances is None:
                jsonfile.write("[]")
            else:
                data = [obj.to_dictionary() for obj in instances]
                jsonfile.write(Base.to_json(data))

    @staticmethod
    def from_json(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON string representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def instantiate(cls, **attributes):
        """Return an instance instantiated from a dictionary of attributes.

        Args:
            **attributes (dict): Key/value pairs of attributes to initialize.
        """
        if attributes and attributes != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
            new_instance.update(**attributes)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated instances.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                data = Base.from_json(jsonfile.read())
                return [cls.instantiate(**d) for d in data]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, instances):
        """Write the CSV serialization of a list of instances to a file.

        Args:
            instances (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if instances is None or instances == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["identity", "width", "height", "x_coord", "y_coord"]
                else:
                    fieldnames = ["identity", "size", "x_coord", "y_coord"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for instance in instances:
                    writer.writerow(instance.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated instances.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["identity", "width", "height", "x_coord", "y_coord"]
                else:
                    fieldnames = ["identity", "size", "x_coord", "y_coord"]
                data = csv.DictReader(csvfile, fieldnames=fieldnames)
                data = [dict([k, int(v)] for k, v in d.items()) for d in data]
                return [cls.instantiate(**d) for d in data]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rectangle in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rectangle.x_coord, rectangle.y_coord)
            turt.down()
            for _ in range(2):
                turt.forward(rectangle.width)
                turt.left(90)
                turt.forward(rectangle.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for square in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(square.x_coord, square.y_coord)
            turt.down()
            for _ in range(2):
                turt.forward(square.width)
                turt.left(90)
                turt.forward(square.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

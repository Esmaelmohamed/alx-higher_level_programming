#!/usr/bin/python3

"""Defines a BaseModel class."""
import json
import csv
import turtle


class BaseModel:
    """Base model.

    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_objects (int): Number of instantiated BaseModels.
    """

    __nb_objects = 0

    def __init__(self, identity=None):
        """Initialize a new BaseModel.

        Args:
            identity (int): The identity of the new BaseModel.
        """
        if identity is not None:
            self.identity = identity
        else:
            BaseModel.__nb_objects += 1
            self.identity = BaseModel.__nb_objects

    @staticmethod
    def to_json(list_dicts):
        """Return the JSON serialization of a list of dictionaries.

        Args:
            list_dicts (list): A list of dictionaries.
        """
        if list_dicts is None or list_dicts == []:
            return "[]"
        return json.dumps(list_dicts)

    @classmethod
    def save_to_file(cls, list_instances):
        """Write the JSON serialization of a list of instances to a file.

        Args:
            list_instances (list): A list of inherited BaseModel instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_instances is None:
                jsonfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_instances]
                jsonfile.write(BaseModel.to_json(list_dicts))

    @staticmethod
    def from_json(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def instantiate(cls, **dictionary):
        """Return an instance instantiated from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
            new_instance.update(**dictionary)
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
                list_dicts = BaseModel.from_json(jsonfile.read())
                return [cls.instantiate(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_instances):
        """Write the CSV serialization of a list of instances to a file.

        Args:
            list_instances (list): A list of inherited BaseModel instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_instances is None or list_instances == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["identity", "width", "height", "x_coord", "y_coord"]
                else:
                    fieldnames = ["identity", "size", "x_coord", "y_coord"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for instance in list_instances:
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
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.instantiate(**d) for d in list_dicts]
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


#!/usr/bin/python3

"""Defines a Base class for serialization and deserialization."""
import json
import csv
import turtle


class Base:
    """Base class for serialization and deserialization.

    This class serves as the base for all other classes in the project.
    """

    __number_of_instances = 0

    def __init__(self, identity=None):
        """Initialize a new instance of the Base class.

        Args:
            identity (int): The identity of the new instance.
        """
        if identity is not None:
            self.identity = identity
        else:
            Base.__number_of_instances += 1
            self.identity = Base.__number_of_instances

    @staticmethod
    def to_json(data):
        """Serialize data to JSON format.

        Args:
            data (list): A list of dictionaries to be serialized.

        Returns:
            str: The JSON representation of the data.
        """
        if data is None or data == []:
            return "[]"
        return json.dumps(data)

    @classmethod
    def save_to_file(cls, instances):
        """Write instances to a JSON file.

        Args:
            instances (list): A list of instances to be serialized.
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
        """Deserialize JSON string to Python objects.

        Args:
            json_string (str): The JSON string to be deserialized.

        Returns:
            list: The Python list represented by the JSON string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def instantiate(cls, **attributes):
        """Instantiate an object from a dictionary of attributes.

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
        """Load instances from a JSON file.

        Returns:
            list: A list of instantiated instances.
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
        """Write instances to a CSV file.

        Args:
            instances (list): A list of instances to be serialized.
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
        """Load instances from a CSV file.

        Returns:
            list: A list of instantiated instances.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["identity", "width", "height", "x_coord", "y_coord"]
                else:
                    fieldnames = ["identity", "size", "x_coord", "y_coord"]
                data = csv.DictReader(csvfile, fieldnames=fieldnames)
                data = [dict([k, int(v)] for k, v in d.items())
                        for d in data]
                return [cls.instantiate(**d) for d in data]
        except IOError:
            return []

    @staticmethod
    def draw(rectangles, squares):
        """Draw rectangles and squares using the turtle module.

        Args:
            rectangles (list): A list of Rectangle objects to draw.
            squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rectangle in rectangles:
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
        for square in squares:
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

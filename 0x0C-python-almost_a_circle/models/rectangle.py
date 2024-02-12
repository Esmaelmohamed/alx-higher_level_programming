#!/usr/bin/python3
"""
Defines a Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle.
    """

    def __init__(self, width, height, x_coord=0, y_coord=0, identity=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x_coord (int): The x coordinate of the new Rectangle.
            y_coord (int): The y coordinate of the new Rectangle.
            identity (int): The identity of the new Rectangle.

        Raises:
            TypeError: If width, height, x_coord, or y_coord is not an int.
            ValueError: If width, height, x_coord, or y_coord is less than 0.
        """
        super().__init__(identity)
        self.width = width
        self.height = height
        self.x_coord = x_coord
        self.y_coord = y_coord

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x_coord(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x_coord

    @x_coord.setter
    def x_coord(self, value):
        if type(value) != int:
            raise TypeError("x_coord must be an integer")
        if value < 0:
            raise ValueError("x_coord must be >= 0")
        self.__x_coord = value

    @property
    def y_coord(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y_coord

    @y_coord.setter
    def y_coord(self, value):
        if type(value) != int:
            raise TypeError("y_coord must be an integer")
        if value < 0:
            raise ValueError("y_coord must be >= 0")
        self.__y_coord = value

    def area_calculation(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def rectangle_display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for _ in range(self.y_coord)]
        for _ in range(self.height):
            [print(" ", end="") for _ in range(self.x_coord)]
            [print("#", end="") for _ in range(self.width)]
            print("")

    def rectangle_update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x_coord attribute
                - 5th argument represents y_coord attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            attributes = ['id', 'width', 'height', 'x_coord', 'y_coord']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dict(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x_coord": self.x_coord,
            "y_coord": self.y_coord
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x_coord, self.y_coord,
                                                       self.width, self.height)


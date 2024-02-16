#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    """A class representing a Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle object."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width of the rectangle."""
        if not isinstance(width, int):
            raise ValueError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height of the rectangle."""
        if not isinstance(height, int):
            raise ValueError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        """Set the x-coordinate of the rectangle."""
        if not isinstance(x, int):
            raise ValueError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, y):
        """Set the y-coordinate of the rectangle."""
        if not isinstance(y, int):
            raise ValueError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} {self.__width}/{self.__height}"

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Display the rectangle."""
        for _ in range(self.__height):
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle."""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        
        for key, value in kwargs.items():
            if key == "id": 
                self.id = value
            if key == "width":
                self.width = value
            if key == "height":
                self.height = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value

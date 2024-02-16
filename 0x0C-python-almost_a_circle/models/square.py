#!/usr/bin/python3
from models.base import Base 
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class representing a Square."""

    def __init__(self, size, x=0, y=0 , id =None):
        """Initialize a Square object."""
        super().__init__(size, size, x, y ,id)
        self.__size = size

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the size of the square."""
        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        self.__size = size

    def update(self, *args, **kwargs):
        """Update attributes of the square."""
        if args:
            if len(args) > 1:
                super().__init__(args[0], args[0], self.x, self.y, self.id)
            if len(args) > 2:
                self.size = args[1]
            if len(args) > 3:
                self.x = args[2]
            if len(args) > 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
    def to_dictionary(self):
        return {'id': self.id, 'x': self.x, 'size': self.size,  'y': self.y}

    

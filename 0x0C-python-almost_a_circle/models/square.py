#!/usr/bin/python3
'''Module for Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A Square class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor for Square class.

        Args:
            size (int): Size of the square (both width and height).
            x (int, optional): x-coordinate of the square. Defaults to 0.
            y (int, optional): y-coordinate of the square. Defaults to 0.
            id (int, optional): ID of the square. Defaults to None.
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns string information about this square.

        Returns:
            str: String representation of the square.
        '''
        return '[{}] ({}) {}/{} - {}'.format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''Getter for the size of this square.

        Returns:
            int: Size of the square.
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter for the size of this square.

        Args:
            value (int): Size of the square.
        '''
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''Internal method that updates instance attributes.

        Args:
            id (int, optional): ID of the square.
            size (int, optional): Size of the square.
            x (int, optional): x-coordinate of the square.
            y (int, optional): y-coordinate of the square.
        '''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates instance attributes via non-keyword and keyword args.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        '''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns dictionary representation of this class.

        Returns:
            dict: Dictionary representation of the square.
        '''
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}


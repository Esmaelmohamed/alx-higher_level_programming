#!/usr/bin/python3
"""Defines a Rectangle"""

class Rectangle:
    """Represent a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle

        Arguments:
        width (int): the width of the rectangle
        height (int): the height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter and Setter to take the width of the rectangle and return it"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("the Width should be an int")
        if value < 0:
            raise ValueError("the width should be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter and Setter of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

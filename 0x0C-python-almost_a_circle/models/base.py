#!/bin/bash/python3

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

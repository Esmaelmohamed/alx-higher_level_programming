# Classes Description

## Base Class

### Description:
The `Base` class serves as the base class for object management. It provides functionality to assign unique identifiers to objects created from classes that inherit from it.

### Attributes:
- `__nb_objects`: A private class variable that keeps track of the number of objects created.

### Methods:
- `__init__(self, id=None)`: Initializes a `Base` object. If an identifier (`id`) is provided, it assigns that value to the object's `id` attribute. If no identifier is provided, it automatically generates a unique identifier based on the number of objects created.

---

## Rectangle Class

### Description:
The `Rectangle` class represents a rectangle object with width, height, x-coordinate, y-coordinate, and an identifier. It inherits from the `Base` class for object management.

### Attributes:
- `__width`: Private attribute representing the width of the rectangle.
- `__height`: Private attribute representing the height of the rectangle.
- `__x`: Private attribute representing the x-coordinate of the rectangle.
- `__y`: Private attribute representing the y-coordinate of the rectangle.

### Methods:
- `__init__(self, width, height, x=0, y=0, id=None)`: Initializes a `Rectangle` object with the specified width, height, x-coordinate, y-coordinate, and identifier.
- `width`: Getter and setter methods for the width attribute.
- `height`: Getter and setter methods for the height attribute.
- `x`: Getter and setter methods for the x-coordinate attribute.
- `y`: Getter and setter methods for the y-coordinate attribute.
- `area(self)`: Calculates and returns the area of the rectangle.
- `display(self)`: Displays the rectangle using '#' characters.
- `update(self, *args, **kwargs)`: Updates the attributes of the rectangle. It accepts both positional and keyword arguments.

---

## Square Class

### Description:
The `Square` class represents a square object with side length, x-coordinate, y-coordinate, and an identifier. It inherits from the `Rectangle` class.

### Attributes:
- `__size`: Private attribute representing the side length of the square.

### Methods:
- `__init__(self, size, x=0, y=0, id=None)`: Initializes a `Square` object with the specified size, x-coordinate, y-coordinate, and identifier.
- `size`: Getter and setter methods for the size attribute.
- `update(self, *args, **kwargs)`: Updates the attributes of the square. It accepts both positional and keyword arguments.

---


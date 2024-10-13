import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override the area method")  # Ensures this method is overridden

# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  # Override area to calculate rectangle area

# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2  # Override area to calculate circle area

from shape import Shape, InvalidDimensionError
from math import pi

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise InvalidDimensionError("Radius must be a positive number!")
        super().__init__("Circle")
        self.radius = radius
        
        
    def get_area(self):
        return pi * self.radius ** 2
    
    def get_perimeter(self):
        return 2 * pi * self.radius
    
    def __str__(self):
        return f"Circle(radius={self.radius}): Area={self.get_area():.2f}, Perimeter={self.get_perimeter():.2f}"
